import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/predict"  # Change this if running on a different server

# Streamlit UI
st.title("Heart Disease Prediction App")
st.markdown("Enter the patient details below and get a prediction.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.radio("Sex", [("Male", 1), ("Female", 0)])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol Level (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", [("Yes", 1), ("No", 0)])
restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
thalachh = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.radio("Exercise-Induced Angina", [("Yes", 1), ("No", 0)])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia Type", [1, 2, 3])

# Prepare data
data = {
    "age": age,
    "sex": sex[1],
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs[1],
    "restecg": restecg,
    "thalachh": thalachh,
    "exang": exang[1],
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

# Submit button
if st.button("Predict"):
    with st.spinner("Analyzing..."):
        try:
            response = requests.post(FASTAPI_URL, json=data)
            result = response.json()
            prediction = result["prediction"]
            status = result["status"]

            st.success(f"Prediction: {status}")
            st.subheader("Result Interpretation:")
            if prediction == 1:
                st.error("⚠️ High Risk of Heart Disease. Consult a Doctor.")
            else:
                st.success("✅ No Heart Disease Detected.")

        except Exception as e:
            st.error("Error connecting to the prediction API. Please ensure the FastAPI server is running.")

