# import pandas as pd
# from full_eda import full_eda

# # 1️⃣ Load CSV
# df = pd.read_csv("Student_Performance.csv")  # replace with your file

# # 2️⃣ Run Full EDA
# clean_df, insights = full_eda(df, target="Previous Scores")

# # 3️⃣ Print Insights
# print("Insights:")
# for k, v in insights.items():
#     print(k, ":", v)

# # 4️⃣ Show Cleaned Dataset
# print("\nCleaned DataFrame:")
# print(clean_df)


# # import pandas as pd

# # # Load CSV
# # df = pd.read_csv("Student_Performance.csv")

# # # Strip spaces from column names
# # df.columns = df.columns.str.strip()

# # # Check columns
# # print("Columns:", df.columns)



# import pandas as pd
# from full_eda import full_eda, auto_detect_target

# # -----------------------------
# # 1️⃣ Load Dataset
# # -----------------------------
# df = pd.read_csv("Student_Performance.csv")  # Replace with your CSV
# df.columns = df.columns.str.strip()     # Remove extra spaces

# # -----------------------------
# # 2️⃣ Auto-detect target column
# # -----------------------------
# target_col = auto_detect_target(df)
# print("Auto-detected target column:", target_col)

# # -----------------------------
# # 3️⃣ Run Full EDA
# # -----------------------------
# clean_df, insights = full_eda(df, target=target_col)

# # -----------------------------
# # 4️⃣ Print Insights
# # -----------------------------
# print("\n===== Insights =====")
# for k, v in insights.items():
#     print(k, ":", v)

# # -----------------------------
# # 5️⃣ Show Cleaned Dataset
# # -----------------------------
# print("\n===== Cleaned DataFrame =====")
# print(clean_df.head())







# import pandas as pd
# from full_eda import full_eda

# # Load dataset
# df = pd.read_csv("Student_Performance.csv")
# df.columns = df.columns.str.strip()  # remove extra spaces

# # Run Full EDA (plots auto)
# clean_df, insights = full_eda(df)

# # Print insights
# print("\n===== Insights =====")
# for k, v in insights.items():
#     print(k, ":", v)

# # Show cleaned DataFrame
# print("\n===== Cleaned DataFrame =====")
# print(clean_df.head())






import pandas as pd
from full_eda import full_eda

# Load dataset
df = pd.read_csv("Student_Performance.csv")
df.columns = df.columns.str.strip()

# Run full EDA (numeric + categorical plots included)
clean_df, insights = full_eda(df)

# Print insights
print("\n===== Insights =====")
for k, v in insights.items():
    print(k, ":", v)

# Show cleaned data
print("\n===== Cleaned DataFrame =====")
print(clean_df.head())
