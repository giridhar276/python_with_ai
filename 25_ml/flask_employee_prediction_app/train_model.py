"""
Train and save a simple Linear Regression model for employee hours-per-week prediction.
Run this first:
    python train_model.py
"""

import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("employee.csv")

# Clean column names and text values
df.columns = df.columns.str.strip()
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Replace unknown values and remove missing rows
df = df.replace("?", pd.NA).dropna()

# Some datasets use education-num, some use educational-num
if "education-num" not in df.columns and "educational-num" in df.columns:
    df = df.rename(columns={"educational-num": "education-num"})

# Target: what we want to predict
target = "hours-per-week"

# Input columns used by the model
features = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss"]

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("Model training completed")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

# Save both model and feature names
joblib.dump({"model": model, "features": features}, "employee_hours_model.pkl")
print("Saved model as employee_hours_model.pkl")
