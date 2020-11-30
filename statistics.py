import numpy as np
import matplotlib.pyplot as plt

def getVariance(dataset):
    return np.var(dataset)

def plot(word,dataset,timepoints):
    print(timepoints)
    if timepoints != [] and dataset != []:
        plt.figure(figsize=(10,10))
        plt.plot(timepoints,dataset)
        plt.title(word)
        plt.show()