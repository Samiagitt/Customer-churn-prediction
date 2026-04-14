# Customer Churn Prediction App

## Overview

This project is a machine learning application that predicts whether a customer is likely to churn based on demographic and service-related features. It demonstrates an end-to-end ML pipeline from data preprocessing to deployment using Streamlit.

---

## Objectives

- Predict customer churn using classification models  
- Help businesses identify high-risk customers  
- Build a real-time prediction system  

---

## Dataset

- Customer churn dataset  
- Includes customer demographics, services, and billing information  

---

## Data Processing Steps

- Handled missing values  
- Encoded categorical variables  
- Feature selection and transformation  
- Built pipeline for preprocessing + model  

---

## Model Details

- Model: Random Forest Classifier  
- Used pipeline for preprocessing and prediction  
- Output: Churn / Not Churn + probability score  

---

## Features Used

- Age  
- Gender  
- Tenure  
- Monthly Charges  
- Contract Type  
- Internet Service  
- Total Charges  
- Tech Support  

---

## Application Features

- Interactive Streamlit UI  
- Real-time prediction  
- Probability output  
- Handles structured user input  

---

## How It Works

User Input → Data Processing → Model Prediction → Output Display  

---


🖥️ Application Preview

👉 Users can:

Enter customer information

Click Predict

Instantly see results



🔮 Future Improvements

Add model explainability (SHAP / feature importance)

Deploy on cloud (Streamlit Cloud / Render)

Add user authentication

Improve UI/UX



## How to Run

```bash
git clone <repo-link>
cd churn-app
pip install -r requirements.txt
streamlit run app.py






