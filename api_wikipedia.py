from datetime import date
import requests
import matplotlib.pyplot as plt

def get_counts(title, start, end, language_edition="en"):
    timestamp_list = []
    viewcount_list = []
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{}.wikipedia/all-access/all-agents/{}/daily/{}/{}" # https://www.mediawiki.org/wiki/API:Etiquette
    url_start = str(start).replace("-","")
    url_end = str(end).replace("-","")
    response = requests.get(url.format(language_edition, title, url_start, url_end))
    if response.status_code == 200:
        try:
            for item in response.json()["items"]:
                timestamp_str = item["timestamp"]
                datetime = date(int(timestamp_str[:4]), int(timestamp_str[4:6]), int(timestamp_str[6:8]))
                timestamp_list.append(datetime)
                viewcount_list.append(item["views"])
        except KeyError:
            return [], []
    else:
        print(response.status_code, response.reason)
        return []
    return timestamp_list, viewcount_list

def search_articles(keywords):
    url = "https://en.wikipedia.org/w/api.php"
    if type(keywords) == list:
        keywords = " ".join(keywords)
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": keywords
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        ranking = {}
        i = 1
        try:
            for item in response.json()["query"]["search"]:
                if "disambiguation" not in item["title"]:
                    ranking[i] = item["title"].replace(" ", "_")
                    i += 1
        except KeyError:
            return []
    else:
        print(response.status_code, response.reason)
        return []
    return ranking

def get_creationdates(articlename):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": articlename,
        "rvdir": "newer",
        "rvlimit": 1,
        "rvprop": "timestamp|user",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json"
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        i = 1
        try:
            return response.json()["query"]["pages"][0]["revisions"][0]["timestamp"]
        except KeyError:
            return None
    else:
        print(response.status_code, response.reason)
        return None

def plot_counts(title, start, end, language_edition="en"):
    x, y = get_counts(title,start,end)
    if x != [] and y != []:
        plt.figure(figsize=(10,10))
        plt.plot(x,y)
        plt.title("{} ({})".format(title, language_edition))
        plt.show()


# seasonality pattern
# plot_counts("Santa_Claus", date(2015,7,1), date(2018,12,31))

# random pattern
# plot_counts("Berlin", date(2015,7,1), date(2018,12,31))

# repetitive (but not seasonal) pattern
# plot_counts("UEFA_European_Championship", date(2015,7,1), date(2018,12,31))

# Influence of trigger events / historical incidents
# plot_counts("Coronavirus", date(2015,7,1), date(2020,10,20))

# Influence of complex / not trivial connections
# -> "Stellar corona" is an aura of plasma that surrounds the sun (but has nothing to do with the coronavirus besides naming)
# plot_counts("Stellar_corona", date(2015,7,1), date(2020,10,20))

#plot_counts("Moon", date(2019,1,1), date(2019,12,31))

#print(search_articles(["corona", "virus"]))
print(get_creationdates("2020_United_States_presidential_election"))