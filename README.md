# Fraud Detection Using Machine Learning

An end-to-end machine learning project for detecting potentially fraudulent financial transactions using Python, Scikit-learn, and Streamlit.

## Objective

Developed a machine learning system for detecting fraudulent financial transactions with imbalanced data.

## Project Overview

Fraud detection is a highly imbalanced classification problem where fraudulent transactions represent a small proportion of total transactions. This project develops a machine learning pipeline to classify transactions as fraudulent or legitimate while handling class imbalance and providing probability-based predictions.

## Key Features

- Data preprocessing for categorical and numerical transaction features
- Class-weighted Logistic Regression for fraud classification
- Leakage-resistant Scikit-learn Pipeline and ColumnTransformer
- Fraud prediction with probability scores
- Interactive Streamlit web application
- Saved trained model pipeline using Joblib

## Machine Learning Workflow

1. Data preprocessing
2. Feature transformation
3. Handling class imbalance
4. Model training using Logistic Regression
5. Model evaluation using classification metrics
6. Saving the trained pipeline
7. Real-time prediction through Streamlit

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Project Structure

```text
fraud-detection-ml/
│
├── app.py
├── fraud_detection_pipeline.pkl
├── requirements.txt
└── README.md
