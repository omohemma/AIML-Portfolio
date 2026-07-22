import os

import pandas as pd
import requests
import streamlit as st


DEFAULT_BACKEND_URL = os.getenv("BACKEND_URL", "").rstrip("/")

st.set_page_config(page_title="ExtraaLearn Lead Conversion", page_icon="EL", layout="centered")
st.title("ExtraaLearn Lead Conversion")

backend_url = st.sidebar.text_input("Backend URL", value=DEFAULT_BACKEND_URL)

tab_single, tab_batch = st.tabs(["Single Lead", "Batch Scoring"])

with tab_single:
    age = st.number_input("Age", min_value=18, max_value=80, value=35, step=1)
    current_occupation = st.selectbox("Current Occupation", ["Professional", "Unemployed", "Student"])
    first_interaction = st.selectbox("First Interaction", ["Website", "Mobile App"])
    profile_completed = st.selectbox("Profile Completed", ["Low", "Medium", "High"], index=2)
    website_visits = st.number_input("Website Visits", min_value=0, max_value=50, value=5, step=1)
    time_spent_on_website = st.number_input(
        "Time Spent on Website", min_value=0, max_value=5000, value=700, step=10
    )
    page_views_per_visit = st.number_input(
        "Page Views per Visit", min_value=0.0, max_value=25.0, value=3.0, step=0.1
    )
    last_activity = st.selectbox(
        "Last Activity", ["Website Activity", "Email Activity", "Phone Activity"]
    )
    print_media_type1 = st.selectbox("Newspaper Ad", ["No", "Yes"])
    print_media_type2 = st.selectbox("Magazine Ad", ["No", "Yes"])
    digital_media = st.selectbox("Digital Media Ad", ["No", "Yes"])
    educational_channels = st.selectbox("Educational Channels", ["No", "Yes"])
    referral = st.selectbox("Referral", ["No", "Yes"])

    payload = {
        "age": age,
        "current_occupation": current_occupation,
        "first_interaction": first_interaction,
        "profile_completed": profile_completed,
        "website_visits": website_visits,
        "time_spent_on_website": time_spent_on_website,
        "page_views_per_visit": page_views_per_visit,
        "last_activity": last_activity,
        "print_media_type1": print_media_type1,
        "print_media_type2": print_media_type2,
        "digital_media": digital_media,
        "educational_channels": educational_channels,
        "referral": referral,
    }

    if st.button("Predict Conversion", type="primary"):
        if not backend_url:
            st.error("Backend URL is required.")
        else:
            response = requests.post(f"{backend_url}/predict", json=payload, timeout=30)
            if response.ok:
                result = response.json()["results"][0]
                probability = result.get("conversion_probability")
                st.metric("Prediction", result["prediction_label"])
                if probability is not None:
                    st.metric("Conversion Probability", f"{probability:.1%}")
            else:
                st.error(response.json().get("error", response.text))

with tab_batch:
    uploaded_file = st.file_uploader("Upload Leads CSV", type=["csv"])
    if uploaded_file is not None:
        batch_data = pd.read_csv(uploaded_file)
        st.dataframe(batch_data.head(), use_container_width=True)

        if st.button("Score Batch"):
            if not backend_url:
                st.error("Backend URL is required.")
            else:
                records = batch_data.to_dict(orient="records")
                response = requests.post(f"{backend_url}/predict", json={"data": records}, timeout=60)
                if response.ok:
                    results = pd.DataFrame(response.json()["results"])
                    scored_data = pd.concat([batch_data.reset_index(drop=True), results], axis=1)
                    st.dataframe(scored_data, use_container_width=True)
                    st.download_button(
                        "Download Scores",
                        scored_data.to_csv(index=False).encode("utf-8"),
                        "extraalearn_predictions.csv",
                        "text/csv",
                    )
                else:
                    st.error(response.json().get("error", response.text))
