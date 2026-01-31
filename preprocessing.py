import numpy as np

# Normalization (Z-score Standardization)
def normalize(series):
    """
    Standard scaling: mean = 0, std = 1
    """
    return (series - series.mean()) / series.std()

# Log Transformation (Skewed Data)
def log_transform(series):
    """
    Apply log transform to reduce skewness
    """
    return np.log1p(series)  # log(1 + x) to handle zero

