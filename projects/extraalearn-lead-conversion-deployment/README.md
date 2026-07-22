# ExtraaLearn Lead Conversion Deployment

## Overview

End-to-end machine learning deployment project for predicting whether an ExtraaLearn lead is likely to convert. The project includes model training, serialized model artifacts, a Flask backend API, and a Streamlit frontend.

## Business Problem

ExtraaLearn generates many leads and needs to identify which prospects are most likely to convert. A lead scoring model helps sales and marketing teams prioritize outreach and improve conversion efficiency.

## Dataset

- File: `data/ExtraaLearn.csv`
- Rows: 4,612
- Columns: 15
- Target variable: `status`
- Key fields: age, occupation, first interaction, profile completion, website visits, website time, page views, last activity, marketing channel flags, referral

## Approach

- Cleaned and inspected lead interaction data
- Built classification models for conversion prediction
- Tuned random forest and AdaBoost models
- Serialized the final model with Joblib
- Created a Flask prediction API
- Created a Streamlit interface for single-lead and batch scoring
- Prepared Docker files for deployment

## Results

Final selected model from `reports/training_summary.json`:

- Final model: Tuned AdaBoost
- Test accuracy: 86.42%
- Test recall: 75.79%
- Test precision: 78.05%
- Test F1-score: 76.90%

## App / Deployment

Backend:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Frontend:

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

The Flask backend exposes:

- `GET /` for health check
- `POST /predict` for single or batch lead scoring

## Files

```text
extraalearn-lead-conversion-deployment/
  README.md
  notebooks/extraalearn_model_deployment.ipynb
  data/ExtraaLearn.csv
  models/model.joblib
  backend/app.py
  backend/model.joblib
  backend/Dockerfile
  backend/requirements.txt
  frontend/app.py
  frontend/Dockerfile
  frontend/requirements.txt
  reports/training_summary.json
  reports/extraalearn_model_deployment.html
  reports/capstone_display.html
  assets/screenshots/
```
