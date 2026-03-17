# Customer-churn-prediction
Machine learning customer churn prediction app built with Python, scikit-learn, and Streamlit.

#Overview
This project predicts whether a customer is likely to churn based on customer profile, billing details, and service information. It is built as an end-to-end machine learning project with a Streamlit app for live predictions.
The goal of this project is to apply machine learning to a real business problem and present the result in an easy-to-use web app.

#Dataset
The project uses a customer churn dataset containing information such as:
->Age
->Gender
->Tenure
->Monthly Charges
->Total Charges
->Contract Type
->Internet Service
->Tech Support
->Churn label
This dataset is used to train a machine learning model that classifies whether a customer is likely to leave the service.

#Tools and Technologies
1.Python
2.pandas
3.scikit-learn
4.Streamlit
5.joblib
6.Jupyter Notebook

#Results
-Built a machine learning model to predict customer churn
-Created a Streamlit app for real-time predictions
-Used a saved pipeline/model file for deployment
-Displayed churn prediction based on user input

#How to Run
-Clone or download this repository
-Install the required libraries
-Run the Streamlit app

#Commands:
pip install -r requirements.txt
streamlit run app.py

#Example Workflow
-Open the Streamlit app
-Enter customer details such as age, tenure, charges, and service information
-Click the prediction button
-View whether the customer is likely to churn

#Future Improvements
-Improve model performance with more tuning
-Add more visualizations to the app
-Deploy the app online or in cloud platform
-Compare multiple models
-Improve UI design for a better user experience

#Project Files
1.app.py — Streamlit app
2.customer-churn-prediction.ipynb — model building notebook
3.churn_rf_pipeline.pkl — saved trained model or pipeline
4.customer_churn_data.csv — dataset
5.requirements.txt — required libraries

Author
Samia Tabassum
