# 📊 Smart EDA & Statistics Python Library

## 🔹 Project Overview

In real-world AI and data science projects, datasets are rarely clean or ready for modeling.  
They often contain **missing values, outliers, irrelevant features**, and **unclear relationships** with the target variable.  

This project is a **reusable Python library** that performs **full Exploratory Data Analysis (EDA) and statistical analysis** on any dataset.  
It automatically handles **data quality, outliers, feature-target relationships**, and prepares datasets for AI/ML models.



## 🎯 Objectives

- Build reusable Python functions for **statistics**:
  - Mean, Median, Mode 🧮
  - Variance, Standard Deviation 📈
  - Z-score, Z-test, T-test, Chi-square test
  - Probability calculations, Normal distribution functions

- Handle **data quality**:
  - Detect missing values and duplicates 📝
  - Handle missing data using mean/median/mode or row deletion
  - Detect and handle outliers (Z-score / IQR method)

- Analyze **features vs target**:
  - Numeric features: correlation and top important features
  - Categorical features: group statistics and chi-square tests
  - Automatically generate **categorical bar plots** 📊

- **Auto-detect target column** for faster workflow ⚡

- Return:
  - Cleaned dataset ✅
  - Summary of insights 💡
  - Visualizations 📈

---

## ⚙️ How It Works

1. **Load Dataset**  
   The library works on any CSV dataset.

2. **Run Full EDA**  
   - Automatically detects the target column  
   - Handles missing values and duplicates  
   - Detects outliers and caps them  
   - Computes statistics on the target: mean, median, mode, std, skewness  
   - Computes numeric feature correlations and ranks top features  
   - Computes categorical feature relations using chi-square tests  
   - Normalizes the target for modeling  
   - Plots categorical features vs target  

3. **Get Insights and Cleaned Dataset**  
   - Summary of relationships between features and target  
   - List of top important features  
   - Dataset cleaned, normalized, and ready for ML

---

## ✅ Features Implemented

| Feature | Status |
|---------|--------|
| Mean, Median, Mode 🧮 | ✅ |
| Variance & Standard Deviation 📈 | ✅ |
| Z-score | ✅ |
| Z-test, T-test, Chi-square test | ✅ |
| Missing Value Detection & Handling 📝 | ✅ |
| Duplicate Rows Detection | ✅ |
| Outlier Detection & Handling (Z-score / IQR) | ✅ |
| Numeric Feature vs Target Analysis | ✅ |
| Categorical Feature vs Target Analysis | ✅ |
| Auto-detect Target Column ⚡ | ✅ |
| Normalize / Transform Target | ✅ |
| Top Important Features 💡 | ✅ |
| Plots: Categorical Features vs Target 📊 | ✅ |

---

## 💡 Benefits

- **Data Cleaning:** Handles missing values and outliers automatically  
- **Feature Insights:** Identifies features most correlated with the target  
- **Statistical Testing:** Provides hypothesis testing functions  
- **Visualization:** Helps understand categorical feature relationships  
- **Ready for Modeling:** Returns cleaned, normalized dataset for AI/ML  

---

## 📝 Notes / Tips

- Ensure categorical columns are of object type for plotting.  
- Numeric columns with ≤10 unique values are treated as categorical automatically.  
- Target column can be auto-detected or manually specified.  

---

## 🚀 Conclusion

This library provides a **fully automated, reusable EDA pipeline** for any dataset.  
It simplifies understanding data quality, feature importance, and statistical relationships, while preparing datasets for AI/ML modeling.  

Hackathon-ready: quick insights, clean data, and visualizations in one run. 🎉
