import numpy as np
from scipy.stats import norm

# Z-Score function
def z_score(value, mean, std):
    return (value - mean) / std

# Normal Distribution – PDF
def normal_pdf(x, mean, std):
    return norm.pdf(x, mean, std)