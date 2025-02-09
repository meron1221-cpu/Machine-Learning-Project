

---

# **🩺 Heart Disease Prediction - Machine Learning Project**  

## **📝 Course:** Fundamentals of Machine Learning  
## **📌 Assignment Title:** Personalized Machine Learning Project  

---

## **🎯 Objective**  
This project explores a real-world **machine learning problem**, guiding through the entire ML lifecycle—from **data acquisition and preprocessing to model training, evaluation, and deployment**. The goal is to build a **classification model** that predicts **heart disease** based on patient health indicators.  

---

## **📊 Dataset Information**  
- **📌 Source:** [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset/data)  
- **📜 License:** Open-source dataset for research purposes.  
- **📁 Format:** CSV  
- **🔑 Features:**  
  - **🧑‍⚕️ Patient Data:** Age, sex, cholesterol levels, blood pressure, heart rate, etc.  
  - **🎯 Target Variable:** `1` (Heart Disease) / `0` (No Heart Disease).  

---

# **🚀 Project Workflow**  

## **1️⃣ Problem Definition & Data Acquisition**  
✅ Clearly defined the **heart disease prediction problem**.  
✅ Obtained dataset from **Kaggle**.  
✅ Provided **dataset descriptions** and properties.  

## **2️⃣ Data Understanding & Exploration (EDA)**  
✅ Loaded dataset and checked for **missing values**.  
✅ Analyzed **distributions, outliers, and correlations**.  
✅ Visualized key relationships between **features and target variable**.  

## **3️⃣ Data Preprocessing**  
✅ **Encoded categorical variables**.  
✅ **Scaled numerical features** for better model performance.  
✅ **Split data** into **80% training** and **20% testing**.  

## **4️⃣ Model Implementation & Training**  
✅ Selected **Random Forest Classifier** for classification.  
✅ Tuned hyperparameters using **GridSearchCV**.  
✅ Trained the model on **preprocessed data**.  

## **5️⃣ Model Evaluation**  
✅ Evaluated using **Accuracy, Precision, Recall, and F1-score**.  
✅ Visualized **Confusion Matrix** and **Feature Importance**.  
✅ Compared against a **baseline model**.  

## **6️⃣ Model Deployment (Bonus Marks)**  
✅ Deployed model using **FastAPI** to serve real-time predictions.  
✅ API **receives patient data and returns a diagnosis**.  

---

# **🛠️ Technologies Used**  
✅ **Programming Language:** Python 3.x  
✅ **Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`  
✅ **API Framework:** FastAPI  
✅ **Model Deployment:** Uvicorn  
✅ **Data Visualization:** Matplotlib, Seaborn  

---

# **🛠️ Installation & Setup**  

## **📥 1. Clone the Repository**  
```bash
git clone https://github.com/meron1221-cpu/Machine-Learning-Project.git
```


## **📦 2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

## **📌 3. Run Model Training**  
```bash
python main.py
```

## **🚀 4. Start API for Model Deployment**  
```bash
uvicorn main:app --reload
```

## **🔬 5. Test API**  
- Open **Swagger UI** at **[`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)**.  
- Send a **POST request** with **patient data** to get a prediction.  

---

# **📊 Results & Key Findings**  
✅ Achieved ** ~95% accuracy** on test data.  
✅ **Chest pain type, exercise-induced angina, and max heart rate** were top predictive features.  
✅ Deployment provides an **accessible API** for real-world use.  

---
Here's the updated JSON section formatted for a GitHub README:

---

# 📋 Example Predictions  
Here are some example predictions made by the deployed model based on input data:

### Example 1:
**Input JSON**
```json
{ 
  "age": 40,
  "sex": 1,
  "cp": 0,
  "trestbps": 110,
  "chol": 167,
  "fbs": 0,
  "restecg": 0,
  "thalachh": 114,
  "exang": 1,
  "oldpeak": 2.0,
  "slope": 1,
  "ca": 0,
  "thal": 3
}
```
**Response**
```json
{ 
  "prediction": 0,
  "status": "Heart Disease Absent"
}
```

### Example 2:
**Input JSON**
```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalachh": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```
**Response**
```json
{
  "prediction": 1,
  "heart_disease": "Present"
}
``` 

--- 

# **🚀 Future Improvements**  
✅ **🖥️ Interactive User Interface:** Create a **web dashboard** for easy predictions.  
✅ **📊 Enhanced Model Performance:** Experiment with **deep learning models**.  
✅ **☁️ Cloud Deployment:** Host on **AWS/GCP/Heroku** for wider accessibility.  
✅ **📈 Explainability:** Use **SHAP values** for better model interpretability.  

---

# **📌 Submission Details**  
📍 **GitHub Repo:** [🔗 Link to Repository](https://github.com/meron1221-cpu/Machine-Learning-Project.git#)  
📍 **API Deployment Link (if applicable):** [🔗 Link to API](https://machine-learning-project-3-x33d.onrender.com/docs#)  
📍 **Deadline:** February 2, 2017 EC  

---
---

# **👩‍💻 Author**  
📌 **Name:** Meron Nisrane  
📌 **LinkedIn:** [🔗 Connect on LinkedIn](https://www.linkedin.com/in/meron-nisrane-1882b629b)
📌 **Email:** [📩 meronnisrane@gmail.com](mailto:meronnisrane@gmail.com)  

---

