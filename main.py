from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np  # Needed if using a real model
import joblib  # If loading an ML model

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["https://your-frontend.com"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the input data model
class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalachh: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Load the ML model (if you have one)
# model = joblib.load("heart_disease_model.pkl")  # Uncomment this if using a real model

@app.post("/predict")
def predict(data: HeartData):
    # Convert input to an array (needed for ML models)
    input_features = [
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalachh, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]

    # Dummy prediction logic (replace with ML model later)
    prediction = 1 if data.chol > 200 else 0  

    # If using an ML model, uncomment this:
    # prediction = model.predict([input_features])[0]  

    return {
        "prediction": prediction,  # 1 = Heart disease, 0 = No heart disease
        "status": "Heart Disease Present" if prediction == 1 else "Heart Disease Absent"
    }


