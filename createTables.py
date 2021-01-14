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

def compute_mostInterestingKeywordsTable(path_source, path_result, min_weektotal=10, min_changerate=5):
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
        words.append(wpy.Word(c[0],ts_articles=timeseries.Timeseries(c[1])))
    # COmpute interestingness
    interestingWords = mng.filter_interestingness(articles, min_weektotal=min_weektotal, min_changerate=min_changerate)
    res = {}
    keywords = []
    for k in interestingWords:
        keywords.append(k)
        # Delete year but keep calendar week and round numbers:
        res[k] = {}
        for el in interestingWords[k]:
            res[k][el[1]] = [interestingWords[k][el][0], round(interestingWords[k][el][1],2)]
    m = matching.groupmatch(keywords, articles)
    writer = open(path_result,'a',encoding="utf-8")
    writer.write("|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |")
    writer.write("\n|---|---|---|---|---|")
    for i in range(1,len(keywords)+1):
        writer.write("\n| {}. | {} | {} | {} | {} |".format(i, keywords[i-1], res[keywords[i-1]], m[keywords[i-1]]["query"], m[keywords[i-1]]["link"][1]).replace("{","").replace("}",""))
    writer.close()


'''
# Create yearly database of world news articles for NYT and TheGuardian:
for year in range(2000,2021):
    createYearlyDatabase("/home/lmoldon/forschungspraktikum/nyt_reduced.json", "/home/lmoldon/forschungspraktikum/data/nyt{}.json".format(year), year)
    compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json", "/home/lmoldon/forschungspraktikum/results/nytTop{}.md".format(year, year))
    compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/nyt{}.json", "/home/lmoldon/forschungspraktikum/results/nytMostInteresting{}.md".format(year, year))
    createYearlyDatabase("/home/lmoldon/forschungspraktikum/theguardian_reduced.json", "/home/lmoldon/forschungspraktikum/theguardian{}.json".format(year), year)
    compute_topKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json", "/home/lmoldon/forschungspraktikum/results/theguardianTop{}.md".format(year, year))
    compute_mostInterestingKeywordsTable("/home/lmoldon/forschungspraktikum/data/theguardian{}.json", "/home/lmoldon/forschungspraktikum/results/theguardianMostInteresting{}.md".format(year, year))
'''