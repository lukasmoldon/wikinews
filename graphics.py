import matplotlib.pyplot as plt
import api_wikipedia as wiki
from datetime import date

def plot_wikipedia(title, start, end, language_edition="en"):
    x, y = wiki.get_counts(title,start,end)
    if x != [] and y != []:
        plt.figure(figsize=(10,10))
        plt.plot(x,y)
        plt.title("{} ({})".format(title, language_edition))
        plt.show()

def plot_dataset(word,dataset,timepoints):
    print(timepoints)
    if timepoints != [] and dataset != []:
        plt.figure(figsize=(10,10))
        plt.plot(timepoints,dataset)
        plt.title(word)
        plt.show()


# seasonality pattern
# plot_wikipedia("Santa_Claus", date(2015,7,1), date(2018,12,31))

# random pattern
# plot_wikipedia("Berlin", date(2015,7,1), date(2018,12,31))

# repetitive (but not seasonal) pattern
# plot_wikipedia("UEFA_European_Championship", date(2015,7,1), date(2018,12,31))

# Influence of trigger events / historical incidents
# plot_wikipedia("Coronavirus", date(2015,7,1), date(2020,10,20))

# Influence of complex / not trivial connections
# -> "Stellar corona" is an aura of plasma that surrounds the sun (but has nothing to do with the coronavirus besides naming)
# plot_wikipedia("Stellar_corona", date(2015,7,1), date(2020,10,20))