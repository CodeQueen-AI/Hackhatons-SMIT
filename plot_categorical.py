# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # -----------------------------
# # Auto-detect target function
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
# # Plot Categorical Features vs Target
# # -----------------------------
# def plot_categorical_vs_target(df, target=None):
#     if target is None:
#         target = auto_detect_target(df)
#         print("Auto-detected target column:", target)
    
#     cat_cols = df.select_dtypes(include='object').columns
#     if len(cat_cols) == 0:
#         print("No categorical columns found.")
#         return
    
#     for col in cat_cols:
#         plt.figure(figsize=(6,4))
#         sns.barplot(x=col, y=target, data=df)
#         plt.title(f"{col} vs {target}")
#         plt.ylabel(target)
#         plt.xlabel(col)
#         plt.show()

# # -----------------------------
# # Example usage
# # -----------------------------
# if __name__ == "__main__":
#     # Load dataset
#     df = pd.read_csv("Student_Performance.csv")
#     df.columns = df.columns.str.strip()  # Remove extra spaces
    
#     # Plot categorical features vs target
#     plot_categorical_vs_target(df)











import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Auto-detect target function
# -----------------------------
def auto_detect_target(df):
    numeric_cols = df.select_dtypes(include='number').columns
    keywords = ['score', 'marks', 'target', 'price', 'y']
    for col in numeric_cols:
        for kw in keywords:
            if kw in col.lower():
                return col
    return numeric_cols[-1]  # fallback: last numeric column

# -----------------------------
# Plot Categorical Features vs Target
# -----------------------------
def plot_categorical_vs_target(df, target=None):
    if target is None:
        target = auto_detect_target(df)
        print(f"Auto-detected target column: {target}")

    # Select categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) == 0:
        print("No categorical columns found for plotting.")
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
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv("Student_Performance.csv")
    df.columns = df.columns.str.strip()  # Remove extra spaces
    
    # Run categorical plots
    plot_categorical_vs_target(df)
