import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def getVariance(dataset):
    """
    Computes the variance (see ``numpy.var``).

    """
    return np.var(dataset)

def findOutliers(dataset):
    """
    Returns all outliers in a given dataset, which are not within a symmetric range of 3 * standard deviation around the mean value.

    """
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

def getCorrelation(x,y):
    """
    Computes the pearson correlation coefficient (see ``scipy.stats.pearsonr``).

    """
    return stats.pearsonr(x,y)