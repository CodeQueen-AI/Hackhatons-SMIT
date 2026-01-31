import numpy as np

# Normalization (Z-score)
def normalize(series):
    return (series - series.mean()) / series.std()

# Log Transformation (Skewed Data)
def log_transform(series):
    return np.log1p(series)  