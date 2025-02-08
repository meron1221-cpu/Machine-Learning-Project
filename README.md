# **📌 Personalized Machine Learning Project: Heart Disease Prediction**  

## **📝 Course:** Fundamentals of Machine Learning  
## **📌 Assignment Title:** Personalized Machine Learning Project  

---

## **🎯 Objective**  
This project explores a real-world machine learning problem, guiding through the entire ML lifecycle—from **data acquisition and preprocessing to model training, evaluation, and deployment**. The goal is to build a **classification model** that predicts heart disease based on patient health indicators.  

---

## **📊 Dataset Information**  
- **📌 Source:** [kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset/data)  
- **📜 License:** Open-source dataset for research purposes.  
- **📁 Format:** CSV  
- **🔑 Features:**  
  - **Numerical & Categorical Features:** Age, cholesterol, blood pressure, exercise-induced angina, etc.  
  - **🎯 Target Variable:** `1` (Heart Disease) / `0` (No Heart Disease).  

---

# **🚀 Project Workflow**  

## **1️⃣ Problem Definition & Data Acquisition**  
✅ Clearly defined the **heart disease prediction problem**.  
✅ Obtained dataset from **UCI Heart Disease Repository**.  
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

# **🛠️ Installation & Setup**  

## **📥 1. Clone the Repository**  
```bash
[git clone https://github.com/meron1221-cpu/Machine-Learning-Project.git

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
- Open **Swagger UI** at **`http://127.0.0.1:8000/docs`**.  
- Send **POST request** with **patient data** to get a prediction.  

---

# **📊 Results & Key Findings**  
✅ Achieved **85-90% accuracy** on test data.  
✅ **Chest pain type, exercise-induced angina, and max heart rate** were top predictive features.  
✅ Deployment provides an **accessible API** for real-world use.  

---

# **🚀 Future Improvements**  
🔹 Collect **more data** for better generalization.  
🔹 Experiment with **deep learning models**.  
🔹 Deploy on **cloud (AWS/GCP/Heroku)**.  
🔹 Improve explainability with **SHAP values**.  

---

# **📌 Submission Details**  
📍 **GitHub Repo:** [🔗 Link to Repository](https://github.com/meron1221-cpu/Machine-Learning-Project.git#)  
📍 **Deadline:** February 2, 2017 EC  
