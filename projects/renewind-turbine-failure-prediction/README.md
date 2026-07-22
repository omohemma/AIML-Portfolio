# ReneWind Turbine Failure Prediction

## Overview

Deep learning classification project for predictive maintenance in wind turbines. The project uses sensor-derived features to predict generator failure and help reduce operational downtime.

## Business Problem

ReneWind wants to improve wind turbine maintenance by identifying failures before they happen. Missing a real failure can be costly, so model evaluation must consider recall and business cost, not only accuracy.

## Dataset

- Training file: `data/Train.csv`
- Test file: `data/Test.csv`
- Training rows: 20,000
- Test rows: 5,000
- Columns: 41 in each file
- Target variable: `Target`
- Feature names are anonymized sensor variables from `V1` to `V40`

## Approach

- Loaded transformed sensor data
- Explored class balance and feature distributions
- Built and compared neural network models
- Tuned models with business-aware evaluation criteria
- Selected the final model based on validation and test performance

## Results

Final test summary from the notebook:

- Accuracy: 98.98%
- Precision: 95.65%
- Recall: 85.82%
- F1-score: about 0.90
- Confusion matrix: TN 4707, FP 11, FN 40, TP 242

## Business Recommendations

- Use the selected model for predictive maintenance prioritization.
- Favor recall when the cost of missing a failure is high.
- Monitor false positives because unnecessary maintenance also has cost.
- Re-train periodically as new sensor and maintenance data becomes available.

## Files

```text
renewind-turbine-failure-prediction/
  README.md
  notebooks/renewind_turbine_failure_prediction.ipynb
  data/Train.csv
  data/Test.csv
  reports/renewind_turbine_failure_prediction.html
  models/
  assets/screenshots/
```
