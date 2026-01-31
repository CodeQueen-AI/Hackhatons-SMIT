import pandas as pd
from scipy.stats import pearsonr, chi2_contingency

# Numerical Features vs Target (Correlation)
def numeric_target_relation(df, target):
    correlations = {}
    for col in df.select_dtypes(include="number"):
        if col != target:
            corr, _ = pearsonr(df[col], df[target])
            correlations[col] = abs(corr)
    return correlations


# Categorical Features vs Target (Chi-Square Test)
def categorical_target_relation(df, target):
    relations = {}
    for col in df.select_dtypes(include="object"):
        table = pd.crosstab(df[col], df[target])
        chi2, p, _, _ = chi2_contingency(table)
        relations[col] = p
    return relations

