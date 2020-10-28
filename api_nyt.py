from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
import datetime
import requests
import logging
import json



def download_articles(api_key, path_results, start, end):
    logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    url = "https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}" # https://developer.nytimes.com/docs/archive-product/1/overview
    properties = ["headline", "pub_date", "web_url", "abstract", "snippet", "lead_paragraph", "keywords", "document_type", "type_of_material", "word_count", "section_name"]
    data = {}
    cur_date = start

    logging.info("Starting..")
    while cur_date != end + relativedelta(months=+1):
        log_starttime = datetime.datetime.now()
        logging.info("Downloading {}/{} ..".format(cur_date.year, cur_date.month))
        response = requests.get(url.format(cur_date.year, cur_date.month, api_key))
        if response.status_code == 200:
            if str(cur_date.year) not in data:
                data[str(cur_date.year)] = {}
            data[str(cur_date.year)][str(cur_date.month)] = {}
            cnt = 1
            for article in response.json()["response"]["docs"]:
                data[str(cur_date.year)][str(cur_date.month)][str(cnt)] = {}
                for el in properties:
                    if el in article:
                        if el == "headline":
                            data[str(cur_date.year)][str(cur_date.month)][str(cnt)]["headline"] = article["headline"]["main"]
                        else:
                            data[str(cur_date.year)][str(cur_date.month)][str(cnt)][el] = article[el]
                    else:
                        data[str(cur_date.year)][str(cur_date.month)][str(cnt)][el] = ""
                cnt += 1
        else:
            logging.error(response.status_code, response.reason)
        log_endtime = datetime.datetime.now()
        log_runtime = (log_endtime - log_starttime)
        if log_runtime < timedelta(seconds=6): 
            logging.debug("Waiting {} seconds".format(6-log_runtime.seconds)) # https://developer.nytimes.com/faq#a11 ( -> max 10 req/min AND 4000 req/day !!! )
            time.sleep(6-log_runtime.seconds)
        cur_date += relativedelta(months=+1)

    logging.info("Saving results as json..")
    with open(path_results, "w") as fp:
        json.dump(data, fp)

    logging.info("Done!")



def load_articles(path_data):
    with open("C:/Users/lukas/Downloads/nyt.json", "r") as fp:
        article_data = json.load(fp)
    return article_data



def get_article(article_data, year, month, count, article_property):
    return article_data[str(year)][str(month)][count][article_property]

def get_documentType(articles):
    docTypes = {}
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                doc_type = articles[y][m][a]["document_type"]
                if doc_type in docTypes:
                    docTypes[doc_type] += 1
                else:
                    docTypes[doc_type] = 1
    return docTypes

# download_articles("ldxpB4fi05f1WdxlQOPVKPYn9WaAgvry", "C:/Users/lukas/Downloads/nyt_month_response.json", date(2002, 1, 1), date(2002, 2, 1))
# download_articles("ldxpB4fi05f1WdxlQOPVKPYn9WaAgvry", "C:/Users/lukas/Downloads/nyt.json", date(2001, 1, 1), date(2020, 10, 1))

#d = load_articles("C:/Users/lukas/Downloads/nyt.json")

#print(get_article(d, 2001, 2, 29, "headline"))