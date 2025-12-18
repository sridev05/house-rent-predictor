

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# Step 1: Load dataset
data = pd.read_csv("House_Rent_Dataset.csv")
print("✅ Data Loaded Successfully!")

# Step 2: Check for missing values
print("\nMissing values in dataset:")
print(data.isnull().sum())

# Step 3: Drop columns not useful for prediction
data = data.drop(columns=["Posted On"], errors='ignore')

# Step 4: One-Hot Encode categorical columns
data = pd.get_dummies(data, drop_first=True)
print("\n✅ One-Hot Encoding applied!")

# Step 5: Split features and target
X = data.drop("Rent", axis=1)
y = data["Rent"]

# Step 6: Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n✅ Data split done!")
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Step 7: Train the model
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)
print("\n✅ Model trained successfully!")

# Step 8: Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n📊 MODEL PERFORMANCE:")
print(f"R² Score: {r2:.3f}")
print(f"MAE (₹): {mae:.2f}")
print(f"RMSE (₹): {rmse:.2f}")

# Step 9: Save model and columns (for consistent testing)
joblib.dump(model, "final_rent_model.pkl")
joblib.dump(list(X.columns), "model_columns.pkl")

print("\n✅ Model and columns saved successfully!")
