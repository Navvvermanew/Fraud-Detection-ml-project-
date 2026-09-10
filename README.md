Fraud Detection Using Machine Learning
This project demonstrates an end-to-end fraud detection pipeline built using Python and scikit-learn.

Project Overview
Built a fraud detection model using Logistic Regression
Handled class imbalance using class-weighted learning
Used pipelines and column transformers to prevent data leakage
Evaluated performance using confusion matrix and recall-focused metrics
Deployed the trained pipeline using a Streamlit web application
Files in this Repository
fraud_model.ipynb – Data analysis, feature engineering, model training
fraud_detection_pipeline.pkl – Saved preprocessing + model pipeline
app.py – Streamlit web app for real-time fraud prediction
requirements.txt – Required Python libraries
How to Run the App
pip install -r requirements.txt
streamlit run app.py
