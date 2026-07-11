# Data Directory

This folder contains the datasets used throughout the project.

## Dataset Source

The analysis is based on the **Multiple Indicator Cluster Survey (MICS) 2018–19 Pakistan (Round 6)** conducted by **UNICEF** in collaboration with the Pakistan Bureau of Statistics.

The project integrates household- and child-level survey data from the following provinces:

- Punjab
- Sindh
- Khyber Pakhtunkhwa
- Balochistan

These datasets were merged, cleaned, and transformed before being used for feature engineering and machine learning.

---

## Repository Data

To keep this repository lightweight and compliant with data sharing practices:

- Only sample and processed datasets are included where appropriate.
- Intermediate files generated during preprocessing are omitted.
- Large raw survey files (`.sav`, `.dta`) are **not included**.

---

## Raw Data Availability

The original MICS survey data can be requested from the official UNICEF MICS program:

https://mics.unicef.org/

---

## Data Processing Pipeline

```
Raw Provincial Survey Files (.sav)
            │
            ▼
Household & Child Data Merge
            │
            ▼
Province-wise Consolidation
            │
            ▼
Data Cleaning
            │
            ▼
Feature Selection
            │
            ▼
Final Machine Learning Dataset
```

---

## Notes

The datasets included in this repository are intended solely for demonstrating the preprocessing and machine learning workflow implemented in this project.

Please refer to the project's main `README.md` for a complete explanation of the methodology, feature engineering process, model development, and evaluation.
