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

