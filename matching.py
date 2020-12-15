import logging
import json
import datetime
from datetime import timedelta
import api_wikipedia as wiki
import manage_articles as mng
import time


def match(keyword, articles, restore_keyword=False, date=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    # only for single keywords!
    # restore_keyword: specifies whether keyword neighbors should additionally be searched
    # date: specifies when the keyword popped up in the news (None = search without this info)
    # cooc_daterange: symmetric date range around "date" for searching co-occurring keywords (None = search in whole article data)
    # cooc_wordcount: specifies how many most co-occurring keywords will be used for searchig related wiki articles
    # nmax: specifies the maximum number of related wikipedia articles which should be returned
    # timeout: specifies the maximum time in seconds for searching (exeeding the limit will result in returning the intermediate result)
    # useAbstract: specifies whether the abstract should be included for searching co-occurring keywords (NYT only)
    if cooc_daterange == None:
        cooc = mng.get_cooccurrences(keyword, articles, useAbstract=useAbstract)
        if restore_keyword:
            restored = mng.restore_keyword(keyword, articles)[0][0]
    else:
        start = date - timedelta(days=cooc_daterange)
        end = date + timedelta(days=cooc_daterange)
        cooc = mng.get_cooccurrences(keyword, articles, start=start, end=end, useAbstract=useAbstract)
        if restore_keyword:
            restored = mng.restore_keyword(keyword, articles, start=start, end=end, useAbstract=useAbstract)[0][0]
    cooc = cooc[:cooc_wordcount]
    if restore_keyword:
        query = set(restored.split())
        for el in cooc:
            query.add(el[0])
        query = " ".join(query)
    else:
        query = keyword
        for el in cooc:
            query += " " + el[0]
    matching = {
                "query": query,
                "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
    }

    return matching

def groupmatch(keywords, articles, dates=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    matching = {}
    if dates != None and cooc_daterange != None:
        starts = {}
        ends = {}
        for keyword in keywords:
            date = dates[keywords.index(keyword)]
            start = date - timedelta(days=cooc_daterange)
            end = date + timedelta(days=cooc_daterange)
            starts[keyword] = start
            ends[keyword] = end
        coocs = mng.get_group_cooccurrences(keywords, articles, starts, ends, useAbstract)
    else:
        coocs = mng.get_group_cooccurrences(keywords, articles, useAbstract=useAbstract)
    for keyword in keywords:
        if dates != None and cooc_daterange != None:
            date = dates[keywords.index(keyword)]
        else:
            date = None
        matching[keyword] = {}
        cooc = coocs[keyword][:cooc_wordcount]
        query = keyword
        for el in cooc:
            query += " " + el[0]
        time.sleep(1)
        matching[keyword] = {
            "query": query, 
            "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
        }
    return matching

def groupmatch_old(keywords, articles, restore_keyword=False, dates=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    matching = {}
    done = set()
    for keyword in keywords:
        skip = False
        for el in done:
            if keyword in el:
                skip = True
        if not skip:
            if cooc_daterange == None:
                date = None
                cooc = mng.get_cooccurrences(keyword, articles, useAbstract=useAbstract)
                if restore_keyword:
                    restored = mng.restore_keyword(keyword, articles)[0][0]
            else:
                date = dates[keywords.index(keyword)]
                start = date - timedelta(days=cooc_daterange)
                end = date + timedelta(days=cooc_daterange)
                cooc = mng.get_cooccurrences(keyword, articles, start=start, end=end, useAbstract=useAbstract)
                if restore_keyword:
                    restored = mng.restore_keyword(keyword, articles, start=start, end=end, useAbstract=useAbstract)[0][0]
            cooc = cooc[:cooc_wordcount]
            if restore_keyword:
                query = set(restored.split())
                for el in cooc:
                    query.add(el[0])
                query = " ".join(query)
            else:
                query = keyword
                for el in cooc:
                    query += " " + el[0]
            done.add(query)
            time.sleep(1)
            matching[keyword] = {
                "query": query, 
                "link": wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
            }
    return matching
    

#nyt2019 = mng.load_articles("C:/Users/lukas/Documents/GitHub/wikinews/nyt2019.json")
#print(match("trump", nyt2019))
#print(match("trump", nyt2019, restore_keyword=True))