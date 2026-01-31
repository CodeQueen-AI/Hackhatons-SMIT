import pandas as pd

# Missing Values Detect
def missing_percentage(df):
    return df.isnull().mean() * 100

# Handle Missing Values
def handle_missing(df, strategy="mean"):
    df = df.copy()

    for col in df.select_dtypes(include="number"):
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)

    if strategy == "drop":
        df.dropna(inplace=True)

    return df

# Duplicate Rows Detect
def duplicate_rows(df):
    return df.duplicated().sum()