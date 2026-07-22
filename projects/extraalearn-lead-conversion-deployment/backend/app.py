from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request


MODEL_PATH = Path(__file__).with_name("model.joblib")
MODEL_BUNDLE = joblib.load(MODEL_PATH)
MODEL = MODEL_BUNDLE["model"]
FEATURES = MODEL_BUNDLE["features"]

app = Flask(__name__)


def _payload_to_frame(payload):
    if isinstance(payload, dict):
        records = payload.get("data", payload)
    elif isinstance(payload, list):
        records = payload
    else:
        raise ValueError("Payload must be a JSON object or a list of objects.")

    if isinstance(records, dict):
        records = [records]

    frame = pd.DataFrame(records)
    missing = [column for column in FEATURES if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")

    return frame[FEATURES]


@app.get("/")
def health_check():
    return jsonify(
        {
            "status": "ok",
            "model": MODEL_BUNDLE.get("model_name", "ExtraaLearn lead conversion model"),
            "features": FEATURES,
        }
    )


@app.post("/predict")
def predict():
    try:
        payload = request.get_json(force=True)
        input_data = _payload_to_frame(payload)
        predictions = MODEL.predict(input_data).astype(int).tolist()

        if hasattr(MODEL, "predict_proba"):
            probabilities = MODEL.predict_proba(input_data)[:, 1].round(4).tolist()
        else:
            probabilities = [None] * len(predictions)

        results = [
            {
                "prediction": prediction,
                "prediction_label": "Converted" if prediction == 1 else "Not Converted",
                "conversion_probability": probability,
            }
            for prediction, probability in zip(predictions, probabilities)
        ]
        return jsonify({"results": results})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
