from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from huggingface_hub import hf_hub_download

app = Flask(__name__)

# 🔽 Replace this with your actual Hugging Face repo ID
REPO_ID = "AnushkaShivade/ElectricityDemandPrediction"

# 🔽 Download model from Hugging Face
model_path = hf_hub_download(repo_id=REPO_ID, filename="random_forest_model.pkl")

# Load model
model = joblib.load(model_path)

# Features used during training
features = [
    'temp', 'dwpt', 'wspd', 'wdir', 'pres', 'rhum',
    'year', 'month_cos', 'hour_sin', 'hour_cos'
]

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse datetime and compute cyclical time features
        dt = request.form['datetime']
        dt_obj = datetime.fromisoformat(dt)

        hour = dt_obj.hour
        weekday = dt_obj.weekday()
        month = dt_obj.month
        year = dt_obj.year

        hour_sin = np.sin(2 * np.pi * hour / 24)
        hour_cos = np.cos(2 * np.pi * hour / 24)
        month_cos = np.cos(2 * np.pi * month / 12)

        # Collect input features
        final_input = [
            float(request.form['temp']),
            float(request.form['dwpt']),
            float(request.form['wspd']),
            float(request.form['wdir']),
            float(request.form['pres']),
            float(request.form['rhum']),
            year,
            month_cos,
            hour_sin,
            hour_cos
        ]

        # Predict
        df_input = pd.DataFrame([final_input], columns=features)
        prediction = model.predict(df_input)[0]

        return render_template('index.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
