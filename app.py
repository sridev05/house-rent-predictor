from flask import Flask, request, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "final_rent_model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "model_columns.pkl")

# Load with joblib 


model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)

print("✅ Model and columns loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        bhk = int(request.form['bhk'])
        size = float(request.form['size'])
        bathroom = int(request.form['bathroom'])
        floor = request.form['floor']
        area_type = request.form['area_type']
        city = request.form['city']
        area_locality = request.form['area_locality']
        furnishing_status = request.form['furnishing_status']
        tenant_preferred = request.form['tenant_preferred']
        point_of_contact = request.form['point_of_contact']

        # Create input DataFrame
        input_dict = {
            'BHK': [bhk],
            'Size': [size],
            'Bathroom': [bathroom],
            'Floor': [floor],
            'Area Type': [area_type],
            'City': [city],
            'Area Locality': [area_locality],
            'Furnishing Status': [furnishing_status],
            'Tenant Preferred': [tenant_preferred],
            'Point of Contact': [point_of_contact]
        }

        input_df = pd.DataFrame(input_dict)

        # One-hot encode & align with model columns
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

        # Make prediction
        prediction = model.predict(input_encoded)[0]
        output = round(prediction, 2)

        return render_template('index.html', prediction_text=f"🏠 Predicted Rent (₹): {output}")

    except Exception as e:
        print("❌ Error:", e)
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
