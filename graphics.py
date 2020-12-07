import matplotlib.pyplot as plt
import api_wikipedia as wiki

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