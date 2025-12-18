import pandas as pd
import joblib

# Step 1: Load model and column info
model = joblib.load("final_rent_model.pkl")
model_columns = joblib.load("model_columns.pkl")
print("✅ Model loaded successfully!")



# Step 2: Create test input (you can modify these values)
sample = pd.DataFrame({
    "BHK": [1],
    "Size": [5500],
    "Floor": ["2 out of 5"],
    "Area Type": ["Super Area"],
    "Area Locality": ["Whitefield"],
    "City": ["Bangalore"],
    "Furnishing Status": ["Unfurnished"],
    "Tenant Preferred": ["Family"],
    "Bathroom": [2],
    "Point of Contact": ["Contact Owner"]
})



# Step 3: One-Hot Encode (same way as training)
sample_encoded = pd.get_dummies(sample)
sample_encoded = sample_encoded.reindex(columns=model_columns, fill_value=0)

# Step 4: Predict rent
predicted_rent = model.predict(sample_encoded)

print("\n🏠 Predicted Rent (₹):", round(predicted_rent[0], 2))
