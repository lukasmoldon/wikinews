import api_nyt as nyt
import api_wikipedia as wiki
import manage_articles as mng
import statistics
import datetime
import pickle
import timeseries
import TextPreprocessing as txt
from datetime import date
import graphics
import matplotlib.pyplot as plt
import matching
import time
import word as wpy
import random
import numpy
import copy
from copy import deepcopy
import logging
import multiprocessing as mp

log_starttime = datetime.datetime.now()
logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)

output = mp.Queue()

def single_run(pid, articles):
    logging.info("Starting PID {}".format(pid))
    if pid > 0:
        # create random sample and compute correlation
        articles = mng.shuffle_publicationdates(articles)
    logging.debug("PID {}: A".format(pid))
    #Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    #List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    logging.debug("PID {}: B".format(pid))
    #List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    logging.debug("PID {}: C".format(pid))
    #Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        words.append(wpy.Word(c[0],ts_articles=timeseries.Timeseries(c[1])))
    logging.debug("PID {}: D".format(pid))
    interestingWords = mng.filter_interestingness(articles, 10, 5)
    logging.debug("PID {}: E".format(pid))
    keywords = []
    for k in interestingWords:
        keywords.append(k)
    m = matching.groupmatch(keywords, articles)
    logging.debug("PID {}: F".format(pid))
    for key in m.keys():
        #Following line from 
        #https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
        try:
            word = next((x for x in words if x.keyword == key), None)
            query = m[key]['query']
            page = m[key]['link'][1]
            wiki_counts = wiki.get_counts(page, word.ts_articles.getStartDate(), word.ts_articles.getEndDate(),"en")
            if wiki_counts is not None:
                #If wikipedia timeseries exists
                word.coocKeywords = query
                word.wikipediaSite = page
                word.ts_wiki = timeseries.parseWikipediaCounts(wiki_counts)
        except:
            print("ERROR: Key is invalid")
    logging.debug("PID {}: G".format(pid))
    words_analyze = [x for x in words if x.wikipediaSite != ""]
    logging.debug("PID {}: H".format(pid))
    #Drop all timepoints which are not contained in both article and wikipedia timeseries
    corr = []
    for w in words_analyze:
        w_timepointsordered = copy.deepcopy(w)
        w_timepointsordered.ts_articles.timepoints = sorted(w_timepointsordered.ts_articles.timepoints, key=lambda x: x.date, reverse=False)

        ts_a, ts_w = timeseries.alignTimeseries(w_timepointsordered.ts_articles,w_timepointsordered.ts_wiki)
        if len(ts_w.getCounts())<2 or len(ts_a.getCounts())<2:
            words_analyze.remove(w)
        else:
            corr.append(statistics.getCorrelation(ts_a.getCounts(),ts_w.getCounts()))
    logging.debug("PID {}: I".format(pid))
    output.put([pid,numpy.mean(corr)])
    logging.info("Finished PID {}".format(pid))

def run(n, max_workers=72):
    logging.info("Loading initial data ...")
    # Load all articles from 2019
    articles_original = mng.load_articles("nyt2019.json")
    logging.info("Done.")

    logging.info("Starting ...")
    processes = [mp.Process(target=single_run, args=(pid, deepcopy(articles_original))) for pid in range(n+1)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    results = [output.get() for p in processes]
    logging.info("Done with all tasks.")
    random_collection = []
    for el in results:
        if el[0] == 0:
            print("Mean correlation in original data: {}".format(el[1]))
        else:
            random_collection.append(el[1])
    print("Mean correlation in {} random samples: {}".format(n-1, statistics.mean_confidence_interval(random_collection)))
    print("Correlation of each sample:")
    print(random_collection)


run(10)

log_endtime = datetime.datetime.now()
log_runtime = (log_endtime - log_starttime)
logging.info("Total runtime: " + str(log_runtime))