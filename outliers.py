import numpy as np
import pandas as pd

# Detect outliers using IQR
def detect_outliers_iqr(series):
    if not isinstance(series, pd.Series):
        series = pd.Series(series)
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    outliers = series[(series < Q1 - 1.5*IQR) | (series > Q3 + 1.5*IQR)]
    return outliers

# Handle outliers by capping
def cap_outliers(series):
    if not isinstance(series, pd.Series):
        series = pd.Series(series)
    lower = series.quantile(0.05)
    upper = series.quantile(0.95)
    return np.clip(series, lower, upper)

# Detect outliers using Z-score
def detect_outliers_zscore(series, threshold=3):
    if not isinstance(series, pd.Series):
        series = pd.Series(series)
    z_scores = (series - series.mean()) / series.std()
    outliers = series[abs(z_scores) > threshold]
    return outliers