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
import concurrent.futures

results_random = []
result_original = None
articles_original = None

def single_run(pid):
    logging.info("Starting PID ".format(pid))
    global articles_original
    if pid == 0:
        # compute correlation of original data
        articles = articles_original.copy()
    else:
        # create random sample and compute correlation
        articles = mng.shuffle_publicationdates(articles_original)
    #Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    #List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    #List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    #Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        words.append(wpy.Word(c[0],ts_articles=timeseries.Timeseries(c[1])))
    interestingWords = mng.filter_interestingness(articles, 10, 5)
    keywords = []
    for k in interestingWords:
        keywords.append(k)
    m = matching.groupmatch(keywords, articles)
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
    words_analyze = [x for x in words if x.wikipediaSite != ""]
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
    if pid == 0:
        global result_original
        result_original = numpy.mean(corr)
    else:
        global results_random
        results_random.append(numpy.mean(corr))
    logging.info("Finished PID ".format(pid))

def run(n, max_workers=72):
    logging.info("Loading initial data ...")
    # Load all articles from 2019
    global articles_original
    articles_original = mng.load_articles("nyt2019.json")
    logging.info("Done.")

    logging.info("Starting ...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(single_run, range(n+1))
    logging.info("Done with all tasks.")

    global result_original
    print("Mean correlation in original data: {}".format(result_original))
    global results_random
    print("Mean correlation in {} random samples: {}".format(n-1, statistics.mean_confidence_interval(results_random)))
    print("Correlation of each sample:")
    print(results_random)


run(1000)