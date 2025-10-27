# 🏠 House Rent Prediction

A complete Machine Learning web application that predicts the monthly rent (₹) of a house based on details such as BHK, size, location, furnishing status, and more.

Built using **Python**, **Flask**, **Scikit-learn**, and **HTML/CSS**.

---

## 📘 Overview

This project trains a Random Forest Regression model on a real estate dataset to estimate house rent prices.  
The trained model is integrated with a Flask web application that allows users to input property details and receive an instant rent prediction.


---

## ⚙️ Features

- Predicts house rent based on user input
- Web interface built with HTML and CSS
- Flask backend connected to ML model
- Trained using RandomForestRegressor
- Data preprocessing with one-hot encoding
- Model saved and reloaded using Joblib

---

## 🧠 Technologies Used

- Python 3.x  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- Joblib  
- HTML5 / CSS3

---

## 🧩 Input Attributes

The model uses the following attributes as input:

- BHK  
- Size (sqft)  
- Bathroom  
- Floor (e.g. “2 out of 5”)  
- Area Type (Super Area / Carpet Area / Built Area)  
- City (e.g. Bangalore, Mumbai, Chennai, etc.)  
- Area Locality  
- Furnishing Status (Furnished / Semi-Furnished / Unfurnished)  
- Tenant Preferred (Family / Bachelors / Company)  
- Point of Contact (Owner / Agent / Builder)

---

## 🧪 Model Training

The model is trained on the **House_Rent_Dataset.csv** dataset.

Training steps:
1. Load the dataset  
2. Remove unnecessary columns (like *Posted On*)  
3. Apply one-hot encoding for categorical variables  
4. Split into training and testing sets  
5. Train a `RandomForestRegressor`  
6. Evaluate performance using R², MAE, and RMSE  
7. Save the model and column names for Flask inference

The trained model and columns are saved as:
final_rent_model.pkl
model_columns.pkl

yaml
Copy code

---

## 💻 Flask Backend (`app.py`)

The Flask backend:
- Loads the trained model and columns using `joblib`
- Accepts user input from `index.html`
- Converts input into a DataFrame
- One-hot encodes and aligns input with training columns
- Predicts rent using the trained model
- Displays the result on the web page

---
