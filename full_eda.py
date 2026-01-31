# from data_quality import missing_percentage, handle_missing, duplicate_rows
# from outliers import cap_outliers
# from feature_analysis import numeric_target_relation, categorical_target_relation
# from preprocessing import normalize

# def full_eda(df, target):
#     insights = {}

#     # 1️⃣ Data Quality
#     insights["missing_percent"] = missing_percentage(df)
#     insights["duplicates"] = duplicate_rows(df)
#     df = handle_missing(df, strategy="mean")

#     # 2️⃣ Outliers – cap numerical features
#     for col in df.select_dtypes(include="number"):
#         df[col] = cap_outliers(df[col])

#     # 3️⃣ Target analysis
#     insights["target_mean"] = df[target].mean()
#     insights["target_std"] = df[target].std()
#     insights["target_skew"] = df[target].skew()

#     # 4️⃣ Feature vs Target
#     numeric_rel = numeric_target_relation(df, target)
#     cat_rel = categorical_target_relation(df, target)

#     insights["numeric_relationships"] = numeric_rel
#     insights["categorical_relationships"] = cat_rel

#     # 5️⃣ Top 10 important features (numeric)
#     top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
#     insights["top_features"] = top_features

#     # 6️⃣ Normalize target
#     df[target] = normalize(df[target])

#     return df, insights




# import pandas as pd
# from data_quality import missing_percentage, handle_missing, duplicate_rows
# from outliers import cap_outliers
# from feature_analysis import numeric_target_relation, categorical_target_relation
# from preprocessing import normalize

# # Import custom statistics
# from statistics import mean, median, mode, standard_deviation, chi_square_test

# # -----------------------------
# # Auto-target detection
# # -----------------------------
# def auto_detect_target(df):
#     numeric_cols = df.select_dtypes(include='number').columns
#     keywords = ['score','marks','target','price','y']
#     for col in numeric_cols:
#         for kw in keywords:
#             if kw in col.lower():
#                 return col
#     return numeric_cols[-1]

# # -----------------------------
# # Full EDA function
# # -----------------------------
# def full_eda(df, target=None):
#     df = df.copy()
    
#     # Auto detect target if None
#     if target is None:
#         target = auto_detect_target(df)
    
#     insights = {}
    
#     # 1️⃣ Data Quality
#     insights["missing_percent"] = missing_percentage(df)
#     insights["duplicates"] = duplicate_rows(df)
#     df = handle_missing(df, strategy="mean")
    
#     # 2️⃣ Outliers
#     for col in df.select_dtypes(include="number"):
#         df[col] = cap_outliers(df[col])
    
#     # 3️⃣ Target stats using custom functions
#     insights["target_mean"] = mean(df[target])
#     insights["target_median"] = median(df[target])
#     insights["target_mode"] = mode(df[target])
#     insights["target_std"] = standard_deviation(df[target])
#     insights["target_skew"] = df[target].skew()
    
#     # 4️⃣ Feature vs Target
#     numeric_rel = numeric_target_relation(df, target)
#     cat_rel = categorical_target_relation(df, target)
#     insights["numeric_relationships"] = numeric_rel
#     insights["categorical_relationships"] = cat_rel
    
#     # 5️⃣ Top 10 numeric features
#     top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
#     insights["top_features"] = top_features
    
#     # 6️⃣ Normalize target
#     df[target] = normalize(df[target])
    
#     return df, insights















# import pandas as pd
# from data_quality import missing_percentage, handle_missing, duplicate_rows
# from outliers import cap_outliers
# from feature_analysis import numeric_target_relation, categorical_target_relation
# from preprocessing import normalize

# # Custom statistics
# from custom_statistics import mean, median, mode, standard_deviation, chi_square_test

# # Plotting for categorical features
# import matplotlib.pyplot as plt
# import seaborn as sns

# # -----------------------------
# # Auto-target detection
# # -----------------------------
# def auto_detect_target(df):
#     numeric_cols = df.select_dtypes(include='number').columns
#     keywords = ['score','marks','target','price','y']
#     for col in numeric_cols:
#         for kw in keywords:
#             if kw in col.lower():
#                 return col
#     return numeric_cols[-1]

# # -----------------------------
# # Categorical Plots
# # -----------------------------
# def plot_categorical_vs_target(df, target):
#     cat_cols = df.select_dtypes(include='object').columns
#     if len(cat_cols) == 0:
#         print("No categorical columns found for plotting.")
#         return
    
#     for col in cat_cols:
#         plt.figure(figsize=(6,4))
#         sns.barplot(x=col, y=target, data=df)
#         plt.title(f"{col} vs {target}")
#         plt.xlabel(col)
#         plt.ylabel(target)
#         plt.tight_layout()
#         plt.show()

# # -----------------------------
# # Full EDA function
# # -----------------------------
# def full_eda(df, target=None):
#     df = df.copy()
    
#     # 1️⃣ Auto detect target
#     if target is None:
#         target = auto_detect_target(df)
#         print(f"Auto-detected target column: {target}")
    
#     insights = {}
    
#     # 2️⃣ Data Quality
#     insights["missing_percent"] = missing_percentage(df)
#     insights["duplicates"] = duplicate_rows(df)
#     df = handle_missing(df, strategy="mean")
    
#     # 3️⃣ Outliers – cap numerical features
#     for col in df.select_dtypes(include="number"):
#         df[col] = cap_outliers(df[col])
    
#     # 4️⃣ Target Stats (custom statistics)
#     insights["target_mean"] = mean(df[target])
#     insights["target_median"] = median(df[target])
#     insights["target_mode"] = mode(df[target])
#     insights["target_std"] = standard_deviation(df[target])
#     insights["target_skew"] = df[target].skew()
    
#     # 5️⃣ Feature vs Target
#     numeric_rel = numeric_target_relation(df, target)
#     cat_rel = categorical_target_relation(df, target)
#     insights["numeric_relationships"] = numeric_rel
#     insights["categorical_relationships"] = cat_rel
    
#     # 6️⃣ Top 10 Numeric Features
#     top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
#     insights["top_features"] = top_features
    
#     # 7️⃣ Normalize target
#     df[target] = normalize(df[target])
    
#     # 8️⃣ Categorical plots
#     plot_categorical_vs_target(df, target)
    
#     return df, insights

















# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Custom modules
# from data_quality import missing_percentage, handle_missing, duplicate_rows
# from outliers import cap_outliers
# from feature_analysis import numeric_target_relation, categorical_target_relation
# from preprocessing import normalize
# from custom_statistics import mean, median, mode, standard_deviation, chi_square_test

# # -----------------------------
# # Auto-detect target
# # -----------------------------
# def auto_detect_target(df):
#     numeric_cols = df.select_dtypes(include='number').columns
#     keywords = ['score', 'marks', 'target', 'price', 'y']
#     for col in numeric_cols:
#         for kw in keywords:
#             if kw in col.lower():
#                 return col
#     return numeric_cols[-1]  # fallback

# # -----------------------------
# # Categorical Plots
# # -----------------------------
# def plot_categorical_vs_target(df, target):
#     cat_cols = df.select_dtypes(include='object').columns
#     if len(cat_cols) == 0:
#         print("No categorical columns for plotting.")
#         return

#     for col in cat_cols:
#         plt.figure(figsize=(6,4))
#         sns.barplot(x=col, y=target, data=df)
#         plt.title(f"{col} vs {target}")
#         plt.xlabel(col)
#         plt.ylabel(target)
#         plt.tight_layout()
#         plt.show()

# # -----------------------------
# # Full EDA
# # -----------------------------
# def full_eda(df, target=None):
#     df = df.copy()
    
#     # Auto detect target
#     if target is None:
#         target = auto_detect_target(df)
#         print(f"Auto-detected target: {target}")

#     insights = {}

#     # 1️⃣ Data Quality
#     insights["missing_percent"] = missing_percentage(df)
#     insights["duplicates"] = duplicate_rows(df)
#     df = handle_missing(df, strategy="mean")

#     # 2️⃣ Outliers
#     for col in df.select_dtypes(include="number"):
#         df[col] = cap_outliers(df[col])

#     # 3️⃣ Target Stats
#     insights["target_mean"] = mean(df[target])
#     insights["target_median"] = median(df[target])
#     insights["target_mode"] = mode(df[target])
#     insights["target_std"] = standard_deviation(df[target])
#     insights["target_skew"] = df[target].skew()

#     # 4️⃣ Numeric vs Target
#     numeric_rel = numeric_target_relation(df, target)
#     insights["numeric_relationships"] = numeric_rel

#     # 5️⃣ Categorical vs Target
#     cat_rel = categorical_target_relation(df, target)
#     insights["categorical_relationships"] = cat_rel

#     # 6️⃣ Top 10 Numeric Features
#     top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
#     insights["top_features"] = top_features

#     # 7️⃣ Normalize Target
#     df[target] = normalize(df[target])

#     # 8️⃣ Categorical Plots
#     plot_categorical_vs_target(df, target)

#     return df, insights






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

# -----------------------------
# Auto-detect target column
# -----------------------------
def auto_detect_target(df):
    numeric_cols = df.select_dtypes(include='number').columns
    keywords = ['score', 'marks', 'target', 'price', 'y']
    for col in numeric_cols:
        for kw in keywords:
            if kw in col.lower():
                return col
    return numeric_cols[-1]  # fallback

# -----------------------------
# Plot categorical features vs target
# -----------------------------
def plot_categorical_vs_target(df, target):
    # Include both object type and low-cardinality numeric columns
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    # Numeric columns with <=10 unique values -> treat as categorical
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

# -----------------------------
# Full EDA function
# -----------------------------
def full_eda(df, target=None):
    df = df.copy()
    
    # Auto detect target
    if target is None:
        target = auto_detect_target(df)
        print(f"Auto-detected target: {target}")

    insights = {}

    # 1️⃣ Data Quality
    insights["missing_percent"] = missing_percentage(df)
    insights["duplicates"] = duplicate_rows(df)
    df = handle_missing(df, strategy="mean")

    # 2️⃣ Outliers – cap numeric features
    for col in df.select_dtypes(include="number"):
        df[col] = cap_outliers(df[col])

    # 3️⃣ Target statistics using custom functions
    insights["target_mean"] = mean(df[target])
    insights["target_median"] = median(df[target])
    insights["target_mode"] = mode(df[target])
    insights["target_std"] = standard_deviation(df[target])
    insights["target_skew"] = df[target].skew()

    # 4️⃣ Numeric features vs target
    numeric_rel = numeric_target_relation(df, target)
    insights["numeric_relationships"] = numeric_rel

    # 5️⃣ Categorical features vs target
    cat_rel = categorical_target_relation(df, target)
    insights["categorical_relationships"] = cat_rel

    # 6️⃣ Top 10 numeric features
    top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
    insights["top_features"] = top_features

    # 7️⃣ Normalize target
    df[target] = normalize(df[target])

    # 8️⃣ Plot categorical features
    plot_categorical_vs_target(df, target)

    return df, insights

# -----------------------------
# Example usage (optional)
# -----------------------------
if __name__ == "__main__":
    df = pd.read_csv("Student_Performance.csv")
    df.columns = df.columns.str.strip()
    clean_df, insights = full_eda(df)
    
    print("\n===== Insights =====")
    for k,v in insights.items():
        print(k, ":", v)
    
    print("\n===== Cleaned DataFrame =====")
    print(clean_df.head())
