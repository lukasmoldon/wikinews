import numpy as np
import matplotlib.pyplot as plt

def getVariance(dataset):
    return np.var(dataset)

def findOutliers(dataset):  
    mean = np.mean(dataset)
    std = np.std(dataset)
    out = std*3
    lowerLimit = mean-out
    upperLimit = mean+out
    
    outliers=[]
    for datapoint in dataset:
        if datapoint > upperLimit or datapoint < lowerLimit:
            outliers.append(datapoint)
    return outliers

def plot(word,dataset,timepoints):
    print(timepoints)
    if timepoints != [] and dataset != []:
        plt.figure(figsize=(10,10))
        plt.plot(timepoints,dataset)
        plt.title(word)
        plt.show()