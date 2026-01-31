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
