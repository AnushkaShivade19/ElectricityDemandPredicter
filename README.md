# 🌍 Power Demand Prediction for Disaster Management ⚡

## 🌟 Overview
The **Power Demand Prediction** project focuses on accurately forecasting electricity demand in disaster-prone regions such as areas affected by floods, earthquakes, or storms. 

By leveraging machine learning, we predict power consumption patterns, helping disaster management agencies and energy providers:
- Optimize resource allocation
- Minimize grid strain
- Ensure swift recovery

This tool becomes essential in disaster preparedness by integrating real-time data and advanced models, enabling timely power restoration and efficient grid management during emergencies.

---

## 🧠 Key Features and Applications

### 📈 Accurate Power Demand Prediction
Predicts power consumption using multiple features such as:
- Time of Day (hour, day, month)
- Weather Conditions (temperature, humidity, pressure)
- Seasonal Variations (peak demand seasons like summer or winter)
- Special Events & Holidays (festivities, public holidays)

### 🚨 Disaster Response & Recovery
- Forecasts energy needs during and after disasters
- Optimizes power grid allocation for efficient recovery efforts
- Prioritizes power restoration for critical areas (hospitals, shelters, emergency services)

### 💡 Resource Allocation & Load Balancing
- Efficiently allocates resources by predicting high-demand areas
- Balances power loads to prevent grid overuse and minimize strain

### 🔌 Integration with IoT & Smart Grids
- Real-time monitoring of energy consumption via IoT sensors
- Enables dynamic power distribution to high-need areas

### 🔮 Scenario Planning & Simulation
- Simulates disaster scenarios to aid in planning
- Identifies potential infrastructure vulnerabilities using historical data

### 📊 Disaster Management Dashboards
- Real-time power demand predictions and visualizations
- Location-specific insights with alerts for potential grid issues

---

## 📊 Dataset
**Delhi 5-Minute Electricity Demand for Forecasting**

- **Period:** 2016–2024  
- **Frequency:** 5-minute intervals  
- **Records:** Over 1 million entries  
- **Features:**
  - `datetime`
  - `Power demand (kW)`
  - `Temperature (°C)`
  - `Humidity (%)`
  - Other environmental factors

---

## 🧠 Model Overview

**Model:** `Random Forest Regressor`

### Features used:
- Datetime (hour, day, month)
- Temperature & Humidity
- Lagged demand (optional)
- Rolling averages (optional)

### ⚙️ Preprocessing Steps:
- `pd.to_datetime()` for timestamp parsing
- Feature extraction (hour, day, month)
- Winsorization for outlier handling
- RobustScaler for scaling
- Train/Validation/Test splits
- Model saved using `joblib`

---

## 🤖 Hugging Face Integration
Hugging Face pre-trained transformers are used for enhanced feature extraction and to interpret real-time crisis data such as:
- Disaster news
- Weather alerts

### Example:
```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="huggingface-model-id", filename="model_file")
🚀 How It Works
Data Collection: Power usage, weather, timestamps

Preprocessing: Clean, extract time & weather features

Model Training: Random Forest Regressor

Evaluation: Metrics like MSE, R²

Deployment: Flask API for real-time use
```
💻 Installation
Step-by-Step Setup
```
# Clone the repository
git clone https://github.com/yourusername/power-demand-prediction.git
cd power-demand-prediction

# (Optional) Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
Visit: http://127.0.0.1:5000/
```
🎯 Usage
Input:
Timestamp (Month, Day, Hour)

Weather (Temperature, Humidity, Pressure)

Region

Output:
Predicted Power Demand

#🚀 Future Enhancements
🌐 Real-time data integration

🗺️ GIS and geospatial data for region-specific insights

🧠 Advanced models like XGBoost, LSTM

📊 Interactive dashboards for disaster simulations

🏁 Conclusion
This project empowers disaster response by forecasting electricity needs in disaster-affected regions.
It improves:

🧭 Resource allocation

⚡ Power grid resilience

🔄 Continuity of critical services (e.g., hospitals, shelters)