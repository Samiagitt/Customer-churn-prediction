# Customer-churn-prediction-App
📌 Overview

This project is a machine learning-powered web application that predicts whether a customer is likely to churn based on their demographic and service-related information.

The application is built using Streamlit and a trained Random Forest pipeline, providing an interactive interface for real-time predictions.

🧠 Problem Statement

Customer churn is a major challenge for businesses. Identifying customers who are likely to leave helps companies take proactive actions to improve retention.

This project aims to:

Predict churn probability

Provide quick insights through an interactive UI

Demonstrate an end-to-end ML workflow


⚙️ Tech Stack
Python

Scikit-learn (Random Forest)

Pandas

Streamlit

Joblib


🔍 Features

✔ User-friendly web interface

✔ Real-time churn prediction

✔ Probability score output

✔ Handles categorical + numerical inputs

✔ End-to-end ML pipeline integration


📊 Input Features

The model uses the following features:

Age

Gender

Tenure

Monthly Charges

Contract Type

Internet Service

Total Charges

Tech Support


🧪 How It Works

User inputs customer details through the UI

Data is structured into a dataframe

Input is aligned with model features

Pre-trained pipeline processes the data


Model predicts:

Churn / Not Churn

Probability score


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






