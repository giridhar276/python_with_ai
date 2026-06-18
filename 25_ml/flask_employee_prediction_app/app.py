"""
Flask app for predicting employee hours per week.
Run:
    python app.py
Then open:
    http://127.0.0.1:5000
"""

from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load saved model
saved_object = joblib.load("employee_hours_model.pkl")
model = saved_object["model"]
features = saved_object["features"]


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            # Read values from HTML form
            age = float(request.form["age"])
            fnlwgt = float(request.form["fnlwgt"])
            education_num = float(request.form["education_num"])
            capital_gain = float(request.form["capital_gain"])
            capital_loss = float(request.form["capital_loss"])

            # Create input DataFrame in same feature order used during training
            input_data = pd.DataFrame([{
                "age": age,
                "fnlwgt": fnlwgt,
                "education-num": education_num,
                "capital-gain": capital_gain,
                "capital-loss": capital_loss
            }])

            predicted_hours = model.predict(input_data[features])[0]
            prediction = round(predicted_hours, 2)

        except Exception as error:
            prediction = f"Error: {error}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
