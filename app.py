
import streamlit as st
import pandas as pd
import joblib
import os


model = joblib.load("E:/project1/churn_rf_pipeline.pkl")
def main():
    st.title("Churn prediction app")
    st.divider()
    st.write("Please enter the values and hit the predict button for getting prediction!")
    st.divider()
    
    default_features = [
        "CustomerID", "Age", "Gender", "Tenure", "MonthlyCharges",
        "ContractType", "InternetService", "TotalCharges", "TechSupport"
    ]
    expected_cols = list(getattr(model, "feature_names_in_", default_features))

    with st.form("input_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, step=1, value=30)
            gender = st.selectbox("Gender", ["Male", "Female"])
            tenure = st.number_input("Tenure (months)", min_value=0, step=1, value=12)
            monthly = st.number_input("MonthlyCharges", min_value=0.0, step=1.0, value=70.0)

        with col2:
            contract = st.selectbox("ContractType", ["Month-to-Month", "One-Year", "Two-Year"])
            internet = st.selectbox("InternetService", ["DSL", "Fiber Optic", "Unknown"])
            total = st.number_input("TotalCharges", min_value=0.0, step=10.0, value=900.0)
            tech = st.selectbox("TechSupport", ["Yes", "No"])

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Build input row
        row = {
            "Age": age,
            "Gender": gender,
            "Tenure": tenure,
            "MonthlyCharges": monthly,
            "ContractType": contract,
            "InternetService": None if internet == "Unknown" else internet,
            "TotalCharges": total,
            "TechSupport": tech,
        }
        input_df = pd.DataFrame([row])

        # Align to what the model expects (important!)
        try:
            input_df = input_df[expected_cols]
        except Exception:
            st.warning("Model columns don't match this input exactly. Showing debug info below:")
            st.write("Model expects:", expected_cols)
            st.write("You provided:", input_df.columns.tolist())
            return

        # Predict
        pred = model.predict(input_df)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            try:
                proba = model.predict_proba(input_df)[0][1]
            except Exception:
                proba = None

        st.divider()
        if str(pred).lower() in ["1", "yes", "true", "churn"]:
            st.error(f"Prediction: CHURN ✅")
        else:
            st.success(f"Prediction: NOT CHURN ✅")

        if proba is not None:
            st.write(f"Churn probability: **{proba:.2%}**")


if __name__ == "__main__":
    main()
