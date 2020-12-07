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