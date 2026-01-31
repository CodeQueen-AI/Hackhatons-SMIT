from .data_quality import missing_percentage, handle_missing, duplicate_rows
from .outliers import cap_outliers
from .feature_analysis import numeric_target_relation, categorical_target_relation
from .preprocessing import normalize

def full_eda(df, target):
    insights = {}

    # 1️⃣ Data Quality
    insights["missing_percent"] = missing_percentage(df)
    insights["duplicates"] = duplicate_rows(df)
    df = handle_missing(df, strategy="mean")

    # 2️⃣ Outliers – cap numerical features
    for col in df.select_dtypes(include="number"):
        df[col] = cap_outliers(df[col])

    # 3️⃣ Target analysis
    insights["target_mean"] = df[target].mean()
    insights["target_std"] = df[target].std()
    insights["target_skew"] = df[target].skew()

    # 4️⃣ Feature vs Target
    numeric_rel = numeric_target_relation(df, target)
    cat_rel = categorical_target_relation(df, target)

    insights["numeric_relationships"] = numeric_rel
    insights["categorical_relationships"] = cat_rel

    # 5️⃣ Top 10 important features (numeric)
    top_features = sorted(numeric_rel, key=numeric_rel.get, reverse=True)[:10]
    insights["top_features"] = top_features

    # 6️⃣ Normalize target
    df[target] = normalize(df[target])

    return df, insights
