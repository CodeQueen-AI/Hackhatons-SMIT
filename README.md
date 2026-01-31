# 🤖 Automatic & Generative EDA Tool for Any Dataset

A *fully automatic Python EDA & statistics library* that works on **any dataset**. Handles **missing values, outliers, feature-target analysis, and visualizations** in one run. Get **cleaned data, insights, and plots** ready for AI/ML modeling

## 🔹 Project Overview

Datasets are rarely clean—often containing **missing values, outliers, irrelevant features, and unclear target relationships**.
This **reusable library** performs **full EDA and statistical analysis**, automatically handling **data quality, outliers, and feature-target relationships**, with **automatic target detection** for faster preprocessing.


## 🎯 Objectives

- Build reusable Python functions for **statistics*:
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
  - Automatically identifies numeric target columns (like score, marks, target, y)
  - Fallback to last numeric column if no keyword match
  - Makes EDA faster and more efficient

- Return:
  - Cleaned dataset ✅
  - Summary of insights 💡
  - Visualizations 📈


## ⚙️ How It Works

1. **Load Dataset**  
   The library works on any CSV dataset

2. **Run Full EDA**  
   - Automatically detects the target column ⚡ ✅  
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

## Features Implemented

| Feature                                      | Status |
| -------------------------------------------- | ------ |
| Mean, Median, Mode                           | ✅      |
| Variance & Standard Deviation                | ✅      |
| Z-score                                      | ✅      |
| Z-test, T-test, Chi-square test              | ✅      |
| Missing Value Detection & Handling           | ✅      |
| Duplicate Rows Detection                     | ✅      |
| Outlier Detection & Handling (Z-score / IQR) | ✅      |
| Numeric Feature vs Target Analysis           | ✅      |
| Categorical Feature vs Target Analysis       | ✅      |
| **Auto-detect Target Column**                | ✅      |
| Normalize / Transform Target                 | ✅      |
| Top Important Features                       | ✅      |
| Plots: Categorical Features vs Target        | ✅      |



## 💡 Benefits

- **Data Cleaning:** Handles missing values and outliers automatically  
- **Feature Insights:** Identifies features most correlated with the target  
- **Automatic Target Detection:** Saves preprocessing time and ensures correct target selection ⚡  
- **Statistical Testing:** Provides hypothesis testing functions  
- **Visualization:** Helps understand categorical feature relationships  
- **Ready for Modeling:** Returns cleaned, normalized dataset for AI/ML  



## 🚀 Conclusion

This library provides a *fully automated, reusable EDA pipeline* for any dataset  
It simplifies understanding data quality, feature importance, and statistical relationships, while preparing datasets for AI/ML modeling.  
*Automatic target detection* makes it even faster and hackathon-ready.

Hackathon-ready: quick insights, clean data and visualizations in one run 🎉
