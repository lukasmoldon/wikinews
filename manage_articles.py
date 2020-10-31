import logging
import json



def load_articles(path_data):
    with open(path_data) as fp:
        articles = json.load(fp)
    return articles



def store_articles(articles, path_data):
    with open(path_data, "w") as fp:
        json.dump(articles, fp)



def get_article(articles, year, month, count, article_property):
    return articles[str(year)][str(month)][count][article_property]



def filter_articles(articles, restrictions):
    # resrictions:   {attribute_name: [values which pass the filter and remain in data]}
    result = {}
    for y in articles.keys():
        result[y] = {}
        for m in articles[y].keys():
            result[y][m] = {}
            for a in articles[y][m]:
                accept = True
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




#d_nyt = load_articles("/home/lmoldon/forschungspraktikum/nyt.json")
#d_theguardian = load_articles("/home/lmoldon/forschungspraktikum/theguardian.json")

#print(get_article(d_nyt, 2002, 2, 21, "headline"))

#print(count_attributes(d_nyt, "type_of_material"))
#print(count_attributes(d_theguardian, "document_type"))

#d_nyt_reduced = filter_articles(d_nyt, {"document_type": ["article"], "type_of_material": ["News"], "section_name": ["World"]})
#d_theguardian_reduced = filter_articles(d_theguardian, {"document_type": ["article"], "section_name": ["World news"]})

#store_articles(d_nyt_reduced, "/home/lmoldon/forschungspraktikum/nyt_reduced.json")
#store_articles(d_theguardian_reduced, "/home/lmoldon/forschungspraktikum/theguardian_reduced.json")
