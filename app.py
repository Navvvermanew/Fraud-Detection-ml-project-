import streamlit as st
import pandas as pd
import joblib

pipeline=joblib.load('fraud_detection_pipeline.pkl')

st.title("Fraud Detection Web App")

txn_type=st.selectbox("Transaction Type",["TRANSFER","CASH_OUT"])
amount=st.number_input("Amount",min_value=0.0)
oldbalanceOrg=st.number_input("Old Balance Origin",min_value=0.0)
newbalanceOrig=st.number_input("New Balance Origin",min_value=0.0)
oldbalanceDest=st.number_input("Old Balance Destination",min_value=0.0)
newbalanceDest=st.number_input("New Balance Destination",min_value=0.0)

input_df=pd.DataFrame({
    'type':[txn_type],
    'amount':[amount],
    'oldbalanceOrg':[oldbalanceOrg],
    'newbalanceOrig':[newbalanceOrig],
    'oldbalanceDest':[oldbalanceDest],
    'newbalanceDest':[newbalanceDest]
})

if st.button("Check Fraud"):
    pred=pipeline.predict(input_df)[0]
    prob=pipeline.predict_proba(input_df)[0][1]
    if pred==1:
        st.error(f"Fraud Detected (Probability: {prob:.2f})")
    else:
        st.success(f"Legitimate Transaction (Probability: {prob:.2f})")
