import logging
import json
import datetime
import random
import regex
import TextPreprocessing as txt

def load_articles(path_data):
    with open(path_data) as fp:
        articles = json.load(fp)
    return articles

def store_articles(articles, path_data):
    with open(path_data, "w") as fp:
        json.dump(articles, fp)

def get_article(articles, year, month, count, article_property):
    return articles[str(year)][str(month)][count][article_property]

def filter_articles(articles, restrictions, start=None, end=None):
    # resrictions:   {attribute_name: [values which pass the filter and remain in data]}
    # start/end:     date(YEAR, MONTH, DAY) for searching articles between start and end
    result = {}
    for y in articles.keys():
        result[y] = {}
        for m in articles[y].keys():
            result[y][m] = {}
            for a in articles[y][m]:
                accept = True
                if start != None or end != None:
                    timestamp = articles[y][m][a]["pub_date"]
                    if timestamp.count("Z") == 1:
                        date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").date() # theguardian timestamp format
                    else:
                        date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+%f").date() # nyt timestamp format
                    if start != None:
                        if date < start:
                            accept = False
                    if end != None:
                        if date > end:
                            accept = False
                for restriction_attribute in restrictions:
                    if articles[y][m][a][restriction_attribute] not in restrictions[restriction_attribute]:
                        accept = False
                        break
                if accept:
                    result[y][m][a] = articles[y][m][a]
    return result

def get_attributes(articles, attribute):
    # Input: articles from download_articles and an attribute like "abstract"
    # Returns: list of all attributes of the given articles
    attributes = set()
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                attributes.add(articles[y][m][a][attribute])
    return attributes

def count_attributes(articles, attribute):
    # Input: articles from download_articles and an attribute like "abstract"
    # Returns: counts all attributes of the given articles
    attributes = {}
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                val = articles[y][m][a][attribute]
                if val in attributes:
                    attributes[val] += 1
                else:
                    attributes[val] = 1
    return {k: v for k, v in sorted(attributes.items(), key=lambda item: item[1], reverse=True)}

def generate_sample(articles, amount):
    result = {}
    while len(result) != amount:
        try:
            y = random.choice(list(articles.keys()))
            m = random.choice(list(articles[y].keys()))
            a = random.choice(list(articles[y][m].keys()))
            result[y+"-"+m+"-"+a] = articles[y][m][a]
            result[y+"-"+m+"-"+a]["ground_truth"] = [""]
        except:
            pass
    return result

def get_articles_as_list(articles):
    #returns a flat list of all articles given as input
    result = []
    for y in articles.keys():
        for m in articles[y].keys():
            for a in articles[y][m]:
                result.append(articles[y][m][a])
    return result

def getCalendarWeek(dat):
    match = regex.match(r"\d{4}-\d{2}-\d{2}", dat).group(0)
    return datetime.datetime.strptime(match,'%Y-%m-%d').isocalendar()[1]
    
def getYear(dat):
    match = regex.match(r"\d{4}-\d{2}-\d{2}", dat).group(0)
    return datetime.datetime.strptime(match,'%Y-%m-%d').year

def getWordCounts(articles,attribute='abstract'):
    #returns a dict of dicts with number of distinct words in each calendar week
    result = {}
    articles = get_articles_as_list(articles)
    for a in articles:
        key = (getYear(a['pub_date']),getCalendarWeek(a['pub_date']))
        if key not in result:
            result[key] = {}
        for w in txt.parseSentence(a['headline']):
            if w not in result[key]:
                result[key][w] = 1
            else: 
                result[key][w] += 1 
    return result

def getTopWordsForWeek(words, n=10):
    #words input is a dict returned by getWordCounts function
    #n is the number of top n words returned for each calendar week
    result = []
    for k in words.keys():
        result.append((k,sorted(words[k].items(), key=lambda x:x[1],reverse=True)[:n]))
    return result
    

def getDistinctWords(words):
    #words input is a dict returned by getWordCounts function
    #returns a list containing all distinct words occuring in the dict
    result = []
    for k in words.keys():
        for w in words[k].items():
            if w[0] not in result:
                result.append(w[0])
    return result

def getCountPerWeek(words, word):
    weeks = []
    for w in words.keys():
        if word in words[w]:
            weeks.append((w,words[w][word]))
        else:
            weeks.append((w,0))
    return weeks

def get_cooccurrences(keyword, articles, start=None, end=None, useAbstract=True):
    result = {}
    articles = get_articles_as_list(articles)
    for a in articles:
        match = True
        if "abstract" in a and useAbstract:
            content = txt.parseSentence(a["headline"] + " " + a["abstract"])
        else:
            content = txt.parseSentence(a["headline"])
        if keyword not in content:
            match = False
        if match and (start != None or end != None):
            timestamp = a["pub_date"]
            if timestamp.count("Z") == 1:
                date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").date() # theguardian timestamp format
            else:
                date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+%f").date() # nyt timestamp format
            if start != None:
                if date < start:
                    match = False
            if end != None:
                if date > end:
                    match = False
        if match:
            for cooccurrence in content:
                if cooccurrence != keyword:
                    if cooccurrence not in result:
                        result[cooccurrence] = 1
                    else:
                        result[cooccurrence] += 1
    return [(k, result[k]) for k in sorted(result, key=result.get, reverse=True)]


#d_nyt = load_articles("/home/lmoldon/forschungspraktikum/nyt.json")
#d_theguardian = load_articles("/home/lmoldon/forschungspraktikum/theguardian.json")

#print(get_article(d_nyt, 2002, 2, 21, "headline"))

#print(count_attributes(d_nyt, "type_of_material"))
#print(count_attributes(d_theguardian, "document_type"))

#d_nyt_reduced = filter_articles(d_nyt, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]})
#d_theguardian_reduced = filter_articles(d_theguardian, {"document_type": ["article"], "section_name": ["World news"]})
#store_articles(d_nyt_reduced, "/home/lmoldon/forschungspraktikum/nyt_reduced.json")
#store_articles(d_theguardian_reduced, "/home/lmoldon/forschungspraktikum/theguardian_reduced.json")

#d_nyt_ground_truth = generate_sample(filter_articles(d_nyt, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]}), 200)
#d_theguardian_ground_truth = generate_sample(filter_articles(d_theguardian, {"document_type": ["article"], "section_name": ["World news"]}), 200)
#store_articles(d_nyt_ground_truth, "/home/lmoldon/forschungspraktikum/nyt_ground_truth.json")
#store_articles(d_theguardian_ground_truth, "/home/lmoldon/forschungspraktikum/theguardian_ground_truth.json")

#nyt2019 = load_articles("C:/Users/lukas/Documents/GitHub/wikinews/nyt2019.json")
#print(get_cooccurrences("trump", nyt2019))