import numpy as np

# Mean Function
def mean(data):
    return np.mean(data)

# Median Function
def median(data):
    return np.median(data)

# Mode Function
def mode(data):
    return max(set(data), key=data.count)

# Variance
def variance(data):
    return np.var(data, ddof=1)

# Standard Deviation
def standard_deviation(data):
    return np.std(data, ddof=1)
