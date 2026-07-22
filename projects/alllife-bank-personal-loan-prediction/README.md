# AllLife Bank Personal Loan Prediction

## Overview

Supervised machine learning project to predict whether a liability customer is likely to purchase a personal loan. The project supports targeted marketing and helps the bank focus outreach on customers with the highest conversion potential.

## Business Problem

AllLife Bank has many deposit customers but wants to grow its borrower base. The goal is to identify customers who are likely to accept a personal loan offer and understand the features that influence that decision.

## Dataset

- File: `data/Loan_Modelling.csv`
- Rows: 5,000
- Columns: 14
- Target variable: `Personal_Loan`
- Key fields: age, experience, income, family size, credit card spending, education, mortgage, account ownership, online banking, credit card usage

## Approach

- Performed data inspection, preprocessing, and exploratory analysis
- Built classification models for loan purchase prediction
- Compared decision tree variants and model performance
- Evaluated business trade-offs between missed buyers and wasted outreach
- Interpreted feature importance

## Results

- Final selection: post-pruned Decision Tree
- The final model achieved strong generalization and balanced performance on test data.
- The most important driver was income, followed by family size, education, and credit card spending.

## Business Recommendations

- Prioritize high-income customers for personal loan campaigns.
- Use education level, family size, and credit card spending to refine targeting.
- Tailor offers around likely customer needs instead of sending broad campaigns.
- Use the model as a lead-prioritization tool for sales and marketing teams.

## Files

```text
alllife-bank-personal-loan-prediction/
  README.md
  notebooks/alllife_personal_loan_prediction.ipynb
  data/Loan_Modelling.csv
  reports/alllife_personal_loan_prediction.html
  models/
  assets/screenshots/
```
