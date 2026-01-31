import pandas as pd

def auto_detect_target(df):
    # Select numeric columns
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        raise ValueError("No numeric column found to use as target")

    # Check for keywords in column names
    keywords = ['score','marks','target','price','y']
    for col in numeric_cols:
        for kw in keywords:
            if kw in col.lower():
                return col  # Found target
    
    # Fallback: last numeric column
    return numeric_cols[-1]