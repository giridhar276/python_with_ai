"""
Artificial Neural Network Example
Use case: Customer Churn Prediction

Input file:
customer_churn.csv

Goal:
Predict whether a customer may churn or not.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Step 1: Load dataset
df = pd.read_csv("customer_churn.csv")

print("First 5 rows:")
print(df.head())


# Step 2: Separate input and output
X = df.drop("churn", axis=1)
y = df["churn"]


# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 4: Scale the input data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Step 5: Build Artificial Neural Network
model = Sequential()

# Input + hidden layer
model.add(Dense(16, activation="relu", input_shape=(X_train_scaled.shape[1],)))

# Second hidden layer
model.add(Dense(8, activation="relu"))

# Output layer for binary classification
model.add(Dense(1, activation="sigmoid"))


# Step 6: Compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Step 7: Train the model
model.fit(
    X_train_scaled,
    y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)


# Step 8: Predict
y_pred_prob = model.predict(X_test_scaled)
y_pred = (y_pred_prob > 0.5).astype(int)


# Step 9: Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Step 10: Predict for a new customer
new_customer = [[45, 25000, 8, 520, 2, 4]]
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction[0][0] > 0.5:
    print("Prediction: Customer may churn")
else:
    print("Prediction: Customer may not churn")
