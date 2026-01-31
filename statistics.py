import numpy as np
from scipy import stats

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

# Z-Test
def z_test(sample, population_mean):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)

    z = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
    return 

# T-Test
def t_test(sample1, sample2):
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value

# Chi Square Test
def chi_square_test(observed_data):
    chi2, p, dof, expected = stats.chi2_contingency(observed_data)
    return chi2, p

