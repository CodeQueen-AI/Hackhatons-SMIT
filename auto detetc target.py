import pandas as pd

def auto_detect_target(df):
    """
    Automatically detects a numeric target column in the dataset.
    Heuristics:
    1. Look for numeric columns whose name contains common keywords: 'score','marks','target','price','y'
    2. If multiple numeric columns, choose the last numeric column by default
    """
    # 1️⃣ Select numeric columns
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        raise ValueError("No numeric column found to use as target")

    # 2️⃣ Check for keywords in column names
    keywords = ['score','marks','target','price','y']
    for col in numeric_cols:
        for kw in keywords:
            if kw in col.lower():
                return col  # Found target
    
    # 3️⃣ Fallback: last numeric column
    return numeric_cols[-1]
