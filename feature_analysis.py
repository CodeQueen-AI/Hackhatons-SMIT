import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency

# -----------------------------
# Numeric Features vs Target
# -----------------------------
def numeric_target_relation(df, target):
    """
    Computes correlation of numeric features with the target.
    Returns a dictionary: {feature_name: absolute_correlation_value}
    """
    correlations = {}
    for col in df.select_dtypes(include="number"):
        if col != target:
            # Safe: if column is constant, pearsonr returns NaN
            try:
                corr, _ = pearsonr(df[col], df[target])
                correlations[col] = abs(corr) if not np.isnan(corr) else 0
            except:
                correlations[col] = 0
    return correlations

# -----------------------------
# Categorical Features vs Target
# -----------------------------
def categorical_target_relation(df, target):
    """
    Analyzes categorical features vs target using Chi-Square test.
    Returns a dictionary: {feature_name: p_value}
    """
    relations = {}
    for col in df.select_dtypes(include="object"):
        table = pd.crosstab(df[col], df[target])
        # Safe check: chi-square requires at least 2 rows and 2 columns
        if table.shape[0] > 1 and table.shape[1] > 1:
            try:
                chi2, p, _, _ = chi2_contingency(table)
            except:
                p = None
        else:
            p = None  # Not enough data
        relations[col] = p
    return relations

# -----------------------------
# Top N Numeric Features
# -----------------------------
def top_numeric_features(df, target, top_n=10):
    """
    Returns top N numeric features most correlated with target
    """
    corr_dict = numeric_target_relation(df, target)
    # Sort by absolute correlation
    sorted_features = sorted(corr_dict.items(), key=lambda x: x[1], reverse=True)
    return [feature for feature, corr in sorted_features[:top_n]]
