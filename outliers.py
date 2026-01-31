import numpy as np
import pandas as pd

# Outliers detect karo – IQR method
def detect_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    outliers = series[(series < Q1 - 1.5*IQR) | (series > Q3 + 1.5*IQR)]
    return outliers

# Handle Outliers
def cap_outliers(series):
    lower = series.quantile(0.05)
    upper = series.quantile(0.95)
    return np.clip(series, lower, upper)

