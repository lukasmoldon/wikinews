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
import word
import random
import numpy
import copy
from copy import deepcopy
import concurrent.futures

results_random = []
result_original = None
articles_original = None

def single_run(pid):
    global articles_original
    if pid == 0:
        # compute correlation of original data
        articles = articles_original.copy()
    else:
        # create random sample and compute correlation
        articles = mng.shuffle_publicationdates(articles_original)
    

def run(n, max_workers=72):
    # Load all articles from 2019
    global articles_original
    articles_original = mng.load_articles("nyt2019.json")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(single_run, range(n+1))

    global result_original
    print("Mean correlation in original data: {}").format(result_original)
    global results_random
    print("Mean correlation in {} random samples: {}").format(n-1, statistics.mean_confidence_interval(results_random))
    print("Correlation of each sample:")
    print(results_random)


run(10)