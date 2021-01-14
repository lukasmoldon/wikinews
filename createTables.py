import logging
import manage_articles as mng
import datetime
from datetime import date, timedelta
import timeseries
import word as wpy
import json
import matching
import api_wikipedia as wiki


def createYearlyDatabase(path_source, path_result, year):
    data = mng.load_articles(path_source)
    if "guardian" in path_source.lower():
        data = mng.filter_articles(data, {"document_type": ["article"], "section_name": ["World news"]}, start=date(year,1,1), end=date(year,12,31))
    else:
        data = mng.filter_articles(data, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]}, start=date(year,1,1), end=date(year,12,31))
    mng.store_articles(data, path_result)

def compute_topKeywordsTable(path_source, path_result, n=50):
    articles = mng.load_articles(path_source)
    # Get a dict of dicts for each calendar week with word frequencies from getWordCounts
    wordCounts = mng.getWordCounts(articles)
    # List of distinct words 
    distinctWords = mng.getDistinctWords(wordCounts)
    # List of lists of tuples containing weekly word frequency
    countsPerWeek = []
    for w in distinctWords:
        countsPerWeek.append((w,mng.getCountPerWeek(wordCounts,w)))
    # Create list of word objects for each keyword
    words = []
    for c in countsPerWeek:
        yearCount = 0
        for el in c[1]:
            yearCount += el[1]
        words.append([c[0], yearCount])
    # Compute top keywords
    ts_sorted = sorted(words, key=lambda x: x[1], reverse=True)
    keywords = []
    for i in range(1,n+1):
        keywords.append(ts_sorted[i][0])
    m = matching.groupmatch(keywords, articles)
    writer = open(path_result,'a',encoding="utf-8")
    writer.write("| # | keyword | matching result (simple) | computed query (advanced)  | matching result (advanced) |")
    writer.write("\n|---|---|---|---|---|")
    for i in range(1,n+1):
        writer.write("\n| {}. | {} | {} | {} | {} |".format(i, ts_sorted[i][0], wiki.search_articles(ts_sorted[i][0], nmax=1)[1], m[ts_sorted[i][0]]["query"], m[ts_sorted[i][0]]["link"][1]))
    writer.close()

