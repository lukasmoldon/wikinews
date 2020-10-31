import logging
import json



def load_articles(path_data):
    with open(path_data) as fp:
        articles = json.load(fp)
    return articles



def get_article(articles, year, month, count, article_property):
    return articles[str(year)][str(month)][count][article_property]



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
    return attributes



#d_nyt = load_articles("/home/lmoldon/forschungspraktikum/nyt.json")
#d_theguardian = load_articles("/home/lmoldon/forschungspraktikum/theguardian.json")

#print(get_article(d_nyt, 2002, 2, 21, "headline"))

#print(count_attributes(d_nyt, "type_of_material"))

#print(count_attributes(d_theguardian, "document_type"))