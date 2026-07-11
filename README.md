# 📊 Determinants of Child Enrollment in Pakistan using Machine Learning

> An end-to-end machine learning project analyzing the determinants of child enrollment in Pakistan using the Multiple Indicator Cluster Survey (MICS) 2018-19 dataset.

---

## 📌 Project Overview

Educational enrollment remains a major socioeconomic challenge in Pakistan. Traditional econometric models often struggle to capture the complex, non-linear relationships between household characteristics, wealth, parental education, and child enrollment.

This project applies modern machine learning techniques to identify the key determinants of school enrollment and compare their predictive performance against traditional statistical approaches.

The project demonstrates a complete data science workflow, including:

- Data acquisition and preprocessing
- Feature engineering
- Data cleaning and validation
- Machine learning model development
- Model evaluation
- Feature importance analysis
- Policy-oriented interpretation

---

## 🎯 Objectives

- Identify the most influential factors affecting child enrollment.
- Compare traditional econometric models with machine learning models.
- Evaluate predictive performance using multiple evaluation metrics.
- Generate insights that can support evidence-based educational policy.

---

## 📂 Dataset

**Source:** UNICEF Multiple Indicator Cluster Survey (MICS) 2018-19 Pakistan

The project combines provincial datasets from:

- Punjab
- Sindh
- Khyber Pakhtunkhwa
- Balochistan

After merging and preprocessing, the final dataset contains approximately **65,000 observations**.

> **Note:** Raw survey files are not included due to dataset size and licensing restrictions. They can be obtained from the official UNICEF MICS website.

---

# 🛠 Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy
- PyReadStat

### Machine Learning

- Scikit-learn
- XGBoost
- LightGBM
- Random Forest

### Visualization

- Matplotlib

### Statistical Analysis

- Stata

### Development Environment

- Jupyter Notebook

---

# 📁 Repository Structure

```
Determinants-of-Child-Enrollment-ML/

│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_merging-data-files.ipynb
│   ├── 03_feature-engineering-&-machine_learning_models.ipynb
│   └── 04_model_evaluation.ipynb
│
├── scripts/
│   └── merge_province_datasets.py
│
├── data/
│   ├── sample_dataset.csv
│   └── README.md
|
├── poster/
│   └── Research_Poster.pdf
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```
Raw MICS Survey Data
        │
        ▼
Province-wise Data Merge
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Feature Engineering
        │
        ▼
Train/Test Split
        │
        ▼
Model Training
        │
        ▼
Performance Evaluation
        │
        ▼
Feature Importance Analysis
        │
        ▼
Policy Insights
```

---

# 🤖 Machine Learning Models

The following models were implemented and evaluated:

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

Performance was evaluated using:

- ROC-AUC
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 📈 Key Findings

- Machine learning models outperformed traditional econometric approaches.
- Wealth Index was one of the strongest predictors of enrollment.
- Child age and previous education history significantly influenced predictions.
- Household educational background played an important role in enrollment decisions.
- Gradient boosting models achieved the best predictive performance.

---

# 💡 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Machine Learning
- Model Evaluation
- Survey Data Processing
- Statistical Analysis
- Data Visualization

---

# 📚 Future Improvements

- Hyperparameter optimization using Optuna.
- Cross-validation with additional folds.
- SHAP interaction analysis.
- Automated ML pipeline.
- Model deployment using Streamlit or Flask.

---

# ⚠ Disclaimer

This project was developed for academic and research purposes using publicly available survey data from the UNICEF Multiple Indicator Cluster Survey (MICS).


Email: *(Add your email here)*

---
