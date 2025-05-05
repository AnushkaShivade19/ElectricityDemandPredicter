from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from huggingface_hub import hf_hub_download

app = Flask(__name__)

# 🔽 Replace this with your actual Hugging Face repo ID
REPO_ID = "AnushkaShivade/ElectricityDemandPrediction"  # <-- Change this

# 🔽 Download model and scaler from Hugging Face
model_path = hf_hub_download(repo_id=REPO_ID, filename="random_forest_model.pkl")
scaler_path = hf_hub_download(repo_id=REPO_ID, filename="scaler.pkl")

# Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Features used when training
numerical_cols = ['Power demand', 'temp', 'dwpt', 'rhum', 'wdir', 'wspd', 'pres', 'moving_avg_3']
model_features = [
    'temp', 'dwpt', 'rhum', 'wdir', 'wspd', 'pres', 'moving_avg_3',
    'day_of_week', 'hour_of_day', 'month',
    'hour_sin', 'hour_cos', 'day_sin', 'day_cos'
]

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse datetime input and compute time features
        dt = request.form['datetime']
        dt_obj = datetime.fromisoformat(dt)

        hour = dt_obj.hour
        weekday = dt_obj.weekday()
        month = dt_obj.month

        hour_sin = np.sin(2 * np.pi * hour / 24)
        hour_cos = np.cos(2 * np.pi * hour / 24)
        day_sin = np.sin(2 * np.pi * weekday / 7)
        day_cos = np.cos(2 * np.pi * weekday / 7)

        # Get user input
        inputs = {
            "temp": float(request.form['temp']),
            "dwpt": float(request.form['dwpt']),
            "rhum": float(request.form['rhum']),
            "wdir": float(request.form['wdir']),
            "wspd": float(request.form['wspd']),
            "pres": float(request.form['pres']),
            "moving_avg_3": float(request.form['moving_avg_3']),
            "day_of_week": weekday,
            "hour_of_day": hour,
            "month": month,
            "hour_sin": hour_sin,
            "hour_cos": hour_cos,
            "day_sin": day_sin,
            "day_cos": day_cos
        }

        # Full input for scaling
        full_numeric_input = {
            'Power demand': 0.0,
            'temp': inputs['temp'],
            'dwpt': inputs['dwpt'],
            'rhum': inputs['rhum'],
            'wdir': inputs['wdir'],
            'wspd': inputs['wspd'],
            'pres': inputs['pres'],
            'moving_avg_3': inputs['moving_avg_3']
        }

        # Scale numeric features
        scaled_full = scaler.transform(pd.DataFrame([full_numeric_input]))
        scaled_features = list(scaled_full[0][1:])  # exclude 'Power demand'

        # Final input to model
        final_input = scaled_features + [
            inputs['day_of_week'], inputs['hour_of_day'], inputs['month'],
            inputs['hour_sin'], inputs['hour_cos'], inputs['day_sin'], inputs['day_cos']
        ]

        df_input_final = pd.DataFrame([final_input], columns=model_features)
        y_scaled = model.predict(df_input_final)[0]

        # Inverse transform to get actual value
        inverse = np.zeros((1, len(numerical_cols)))
        inverse[0][0] = y_scaled
        y_actual = scaler.inverse_transform(inverse)[0][0]

        return render_template('index.html', prediction=round(y_actual, 2))

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
