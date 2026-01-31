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

    # Treat numeric columns with <=10 unique values as categorical
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        if df[col].nunique() <= 10 and col != target:
            cat_cols.append(col)

    if len(cat_cols) == 0:
        print("No categorical columns for plotting.")
        return

    plt.style.use('dark_background')
    palette = sns.color_palette(["#FF6F61", "#6B5B95", "#982598", "#F075AE", "#FFD700"])  # bright colors

    for idx, col in enumerate(cat_cols):
        plt.figure(figsize=(7,5))
        color = palette[idx % len(palette)]
        ax = sns.barplot(x=col, y=target, data=df, color=color, edgecolor='white')

        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:.1f}', 
                        (p.get_x() + p.get_width() / 2., height), 
                        ha='center', va='bottom', fontsize=10, color='white', fontweight='bold')

        # Customize the plot
        plt.title(f"{col} vs {target}", fontsize=14, fontweight='bold', color='white')
        plt.xlabel(col, fontsize=12, color='white')
        plt.ylabel(target, fontsize=12, color='white')
        plt.xticks(rotation=30, color='white')
        plt.yticks(color='white')
        plt.tight_layout()
        plt.show()

# Full EDA Function
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
    
    # Outliers
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
