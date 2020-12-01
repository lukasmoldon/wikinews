import numpy as np
import matplotlib.pyplot as plt

def getVariance(dataset):
    return np.var(dataset)

def findOutliers(dataset):
    outliers=[]
    threshold=3
    for y in dataset:
        zScore= (y - np.mean(dataset))/np.std(dataset) 
        if np.abs(zScore) > threshold:
            outliers.append(y)
    return outliers

def plot(word,dataset,timepoints):
    print(timepoints)
    if timepoints != [] and dataset != []:
        plt.figure(figsize=(10,10))
        plt.plot(timepoints,dataset)
        plt.title(word)
        plt.show()