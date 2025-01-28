# Week_6-KAIM

KAIM AI training week_6 challenge

# 1. Introduction

Credit scoring is essential for assessing the creditworthiness of potential borrowers. This project involves using data from an eCommerce platform to build a model that accurately classifies users into high-risk (bad) and low-risk (good) categories.

# 2. Understanding Credit Risk

According to the Basel III framework, credit risk is defined as the potential that a borrower will fail to meet obligations as per agreed terms. Effective credit risk management maximizes a bank's risk-adjusted return by maintaining credit risk exposure within acceptable parameters.

# 3. Data Exploration and Preparation

Dataset Overview
The dataset consists of various fields relevant to transaction history and customer profiles:
TransactionId: Unique transaction identifier
CustomerId: Unique identifier for the customer
Amount: Value of the transaction
TransactionStartTime: Time of the transaction
FraudResult: Indicates if the transaction is fraudulent (1 - Yes, 0 - No)
Summary Statistics
Analyzing central tendency, dispersion, and distribution will help identify patterns and outliers.
Missing Values and Outlier Detection
Identify any missing values and outliers that may affect model performance, employing techniques like box plots for visualization.

# 4. Feature Engineering

Aggregate Features
Total Transaction Amount: Sum of all transaction amounts for each customer.
Average Transaction Amount: Average transaction amount per customer.
Transaction Count: Total number of transactions per customer.
Extract Features
Transaction Hour: Hour the transaction occurred.
Transaction Day: Day of the month when the transaction occurred.
Encode Categorical Variables
Use One-Hot Encoding and Label Encoding to convert categorical variables into numerical format.
Handle Missing Values
Utilize imputation for missing values, filling with mean, median, or mode as suitable.
Normalize/Standardize Numerical Features
Employ normalization and standardization techniques to bring all numerical features onto a similar scale.

# 5. Model Development

5.1 Model Selection
Selected models for credit scoring include:
Logistic Regression
Random Forest
Gradient Boosting Machines (GBM)
5.2 Hyperparameter Tuning
Conduct hyperparameter tuning using Grid Search and Random Search techniques to enhance model performance.
5.3 Model Evaluation
Assess model performance using:
Accuracy: Ratio of correct predictions to total predictions.
Precision: Correct positive predictions relative to total positive predictions.
Recall: Correct positive predictions relative to actual positives.
F1 Score: Weighted average of precision and recall.
ROC-AUC: Area Under the ROC Curve.

# 6. API Development for Model Deployment

Framework Selection
FastAPI is chosen for its speed and ease of integration with machine learning models.
Load the Model
Load the trained model using pickle to facilitate predictions.
Define API Endpoints
Create an endpoint /predict/ that accepts input data and returns predictions.
Handle Requests and Return Predictions
Implement logic to preprocess input data, make predictions, and format responses for the API call.
Deployment
Deploy the API on a cloud platform such as AWS or Heroku to ensure accessibility.

# 7. Conclusion

The project aims to develop a comprehensive credit scoring model that not only assesses the risk associated with potential borrowers but also enhances the efficiency of the lending process. By leveraging alternative data and advanced machine learning techniques, Bati Bank can improve financial inclusion for its customers. 8. References
Basel III Capital Accord
Towards Data Science: How to Develop a Credit Risk Model and Scorecard
Corporate Finance Institute: Credit Risk
Risk Officer: Credit Risk Overview

This report serves as a high-level overview of the steps taken to develop the credit risk model, detailing the processes involved in data exploration, feature engineering, model selection, and deployment.
