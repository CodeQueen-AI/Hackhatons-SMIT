import pandas as pd
from full_eda import full_eda

# 1️⃣ Load CSV
df = pd.read_csv("Student_Performance.csv")  # replace with your file

# 2️⃣ Run Full EDA
clean_df, insights = full_eda(df, target="score")

# 3️⃣ Print Insights
print("Insights:")
for k, v in insights.items():
    print(k, ":", v)

# 4️⃣ Show Cleaned Dataset
print("\nCleaned DataFrame:")
print(clean_df)
