import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Custom modules
from data_quality import missing_percentage, handle_missing, duplicate_rows
from outliers import cap_outliers
from feature_analysis import numeric_target_relation, categorical_target_relation
from preprocessing import normalize
from custom_statistics import mean, median, mode, standard_deviation, chi_square_test

# Auto-detect target column
def auto_detect_target(df):
    numeric_cols = df.select_dtypes(include='number').columns
    keywords = ['score', 'marks', 'target', 'price', 'y']
    for col in numeric_cols:
        for kw in keywords:
            if kw in col.lower():
                return col
    return numeric_cols[-1] 

# Plot categorical features vs target
def plot_categorical_vs_target(df, target):
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        if df[col].nunique() <= 10 and col != target:
            cat_cols.append(col)

    if len(cat_cols) == 0:
        print("No categorical columns for plotting.")
        return

    for col in cat_cols:
        plt.figure(figsize=(6,4))
        sns.barplot(x=col, y=target, data=df)
        plt.title(f"{col} vs {target}")
        plt.xlabel(col)
        plt.ylabel(target)
        plt.tight_layout()
        plt.show()

# Full EDA function
def full_eda(df, target=None):
    df = df.copy()
    
    # Auto detect target
    if target is None:
        target = auto_detect_target(df)
        print(f"Auto-detected target: {target}")

    insights = {}

    # Data Quality
    insights["missing_percent"] = missing_percentage(df)
    insights["duplicates"] = duplicate_rows(df)
    df = handle_missing(df, strategy="mean")

    # Outliers – cap numeric features
    for col in df.select_dtypes(include="number"):
        df[col] = cap_outliers(df[col])

    # Target statistics using custom functions
    insights["target_mean"] = mean(df[target])
    insights["target_median"] = median(df[target])
    insights["target_mode"] = mode(df[target])
    insights["target_std"] = standard_deviation(df[target])
    insights["target_skew"] = df[target].skew()

    # Numeric features vs target
    numeric_rel = numeric_target_relation(df, target)
    insights["numeric_relationships"] = numeric_rel

    # Categorical features vs target
    cat_rel = categorical_target_relation(df, target)
    insights["categorical_relationships"] = cat_rel

    # Top 10 numeric features
    top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
    insights["top_features"] = top_features

    # Normalize target
    df[target] = normalize(df[target])

    # Plot categorical features
    plot_categorical_vs_target(df, target)

    return df, insights