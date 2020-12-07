import logging
import json
import datetime
from datetime import date, timedelta
import api_wikipedia as wiki
import manage_articles as mng


def match(keyword, articles, restore_keyword=False, date=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
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
    matching = wiki.search_articles(query, nmax=nmax, date=date, timeout=timeout)
    return matching

def groupmatch(keywords, articles, dates=None, cooc_daterange=None, cooc_wordcount=2, nmax=1, timeout=10, useAbstract=True):
    pass # TODO

#nyt2019 = mng.load_articles("C:/Users/lukas/Documents/GitHub/wikinews/nyt2019.json")
#print(match("trump", nyt2019))
#print(match("trump", nyt2019, restore_keyword=True))