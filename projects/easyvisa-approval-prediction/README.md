# EasyVisa Approval Prediction

## Overview

Classification project using ensemble methods and model tuning to predict visa application certification outcomes. The project focuses on identifying the applicant and employer attributes that influence approval decisions.

## Business Problem

Visa application review is time-consuming and high volume. The objective is to help identify applications likely to be certified or denied, enabling better prioritization and decision support.

## Dataset

- File: `data/EasyVisa.csv`
- Rows: 25,480
- Columns: 12
- Target variable: `case_status`
- Key fields: continent, education, job experience, training requirement, employer size, employer region, wage, wage unit, full-time position

## Approach

- Inspected and cleaned application data
- Explored applicant, employer, wage, and region patterns
- Built classification models with ensemble techniques
- Compared random forest, boosting, and tuned model variants
- Evaluated precision-recall trade-offs for approval prediction

## Results

- Random Forest on undersampled data gave strong accuracy and F1 performance in the notebook comparison.
- Boosting models on oversampled data improved recall but often reduced precision.
- XGBoost achieved very high recall but introduced more false positives.
- AdaBoost and Gradient Boosting offered more balanced precision-recall behavior.

## Business Recommendations

- Treat prior job experience as a major approval signal.
- Consider prevailing wage, employer size, and region as important review features.
- Use the model for triage and decision support, not as a replacement for final review.
- Monitor false positives and false negatives separately because each has a different business impact.

## Files

```text
easyvisa-approval-prediction/
  README.md
  notebooks/easyvisa_approval_prediction.ipynb
  data/EasyVisa.csv
  reports/easyvisa_approval_prediction.html
  models/
  assets/screenshots/
```
