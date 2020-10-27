from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
import datetime
import requests
import logging
import json



def download_articles(api_key, path_results, start, end):
    logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.DEBUG)
    url = "https://content.guardianapis.com/search?from-date={}&to-date={}&order-by=oldest&page-size=200&api-key={}&page=" # https://open-platform.theguardian.com/documentation/
    properties = {"webTitle": "headline", "webPublicationDate": "pub_date", "webUrl": "web_url", "type": "document_type", "sectionName": "section_name"}
    data = {}
    cur_date = start
    cur_page = 1
    cnt = 1


    logging.info("Starting..")
    while cur_date != end + relativedelta(days=+1):
        log_starttime = datetime.datetime.now()
        if (cur_date.day == 1 or cur_date == start) and cur_page == 1:
            logging.info("Downloading {}/{} ..".format(cur_date.year, cur_date.month))
        response = requests.get(url.format(cur_date, cur_date, api_key) + str(cur_page))
        logging.debug("REQUEST for cnt {} on {} on page {}".format(str(cnt), str(cur_date), str(cur_page)))
        if response.status_code == 200:
            if str(cur_date.year) not in data:
                data[str(cur_date.year)] = {}
                if cur_date != start:
                    logging.info("Caching results as json..")
                    with open(path_results, "w") as fp:
                        json.dump(data, fp)
            if str(cur_date.month) not in data[str(cur_date.year)]:
                data[str(cur_date.year)][str(cur_date.month)] = {}
                cnt = 1
            for article in response.json()["response"]["results"]:
                data[str(cur_date.year)][str(cur_date.month)][str(cnt)] = {}
                for el in properties:
                    if el in article:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][properties[el]] = article[el]
                    else:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][properties[el]] = ""
                cnt += 1
        else:
            logging.error(response.status_code, response.reason)
        log_endtime = datetime.datetime.now()
        log_runtime = (log_endtime - log_starttime)
        if log_runtime < timedelta(seconds=18): 
            logging.debug("Waiting {} seconds".format(18-log_runtime.seconds)) # https://developer.nytimes.com/faq#a11 ( -> max every 17.28 sec a request = max 5000 req/day !!! )
            time.sleep(18-log_runtime.seconds)
        try:
            if response.json()["response"]["pages"] == response.json()["response"]["currentPage"]:
                cur_date += relativedelta(days=+1)
                cur_page = 1
            else:
                cur_page += 1
        except:
            cur_date += relativedelta(days=+1)
            cur_page = 1

    logging.info("Saving results as json..")
    with open(path_results, "w") as fp:
        json.dump(data, fp)

    logging.info("Done!")



def load_articles(path_data):
    with open("/home/lmoldon/forschungspraktikum/theguardian.json", "r") as fp:
        article_data = json.load(fp)
    return article_data



def get_article(article_data, year, month, count, article_property):
    return article_data[str(year)][str(month)][count][article_property]



# download_articles("f9f9bc35-de69-42ce-8089-3f786f325643", "/home/lmoldon/forschungspraktikum/theguardian.json", date(2002, 1, 29), date(2002, 2, 2))
download_articles("f9f9bc35-de69-42ce-8089-3f786f325643", "/home/lmoldon/forschungspraktikum/theguardian.json", date(2001, 1, 1), date(2020, 10, 1))

# d = load_articles("/home/lmoldon/forschungspraktikum/theguardian.json")

# print(get_article(d, 2002, 2, 21, "headline"))
