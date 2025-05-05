# 🌍 Power Demand Prediction for Disaster Management ⚡

## 🌟 Overview  
The **Power Demand Prediction** project forecasts electricity demand in disaster-prone regions (floods, earthquakes, storms) using **machine learning**. It enables:

- 📊 Smart energy planning  
- ⚡ Grid load management  
- 🚑 Priority power allocation during emergencies  

> This system becomes essential for **real-time disaster response**, ensuring swift recovery and continuity of critical services.

---

## 🧠 Key Features

### 📈 Accurate Forecasting
- ⏰ Time of day (hour, day, month)  
- 🌡️ Weather data (temperature, humidity, pressure)  
- 📅 Holiday/event impact  
- 🌀 Seasonal patterns  

### 🚨 Disaster Recovery Aid  
- Predicts power needs **during/after disasters**  
- Prioritizes hospitals, shelters & emergency services  

### 💡 Efficient Load Balancing  
- Anticipates high-demand areas  
- Reduces strain on the power grid  

### 🔌 Smart Grid & IoT Ready  
- Real-time monitoring via IoT sensors  
- Supports **dynamic energy routing**

### 🔮 Scenario Simulation  
- Plans for worst-case grid failures  
- Identifies weak spots using historical data  

### 📊 Management Dashboards  
- Visual insights & predictions  
- 🔔 Grid issue alerts

---

## 📊 Dataset  

🗂️ **Delhi 5-Minute Electricity Demand (2016–2024)**  
🕐 **Interval**: Every 5 minutes  
📄 **Records**: 1,000,000+  

**Features:**
- `datetime`  
- `Power demand (kW)`  
- `Temperature (°C)`  
- `Humidity (%)`  
- 🌦️ Environmental conditions  

---

## 🧠 Model Architecture

🧪 **Model Used**: `Random Forest Regressor`  
🎛️ **Features**:
- Time-based (hour, day, month)  
- Weather: Temperature, Humidity  
- Lagged demand (optional)  
- Rolling averages (optional)  

### ⚙️ Preprocessing Steps:
- `pd.to_datetime()` for timestamps  
- ⛏️ Feature extraction  
- 📉 Outlier removal: `winsorize`  
- ⚖️ Scaling: `RobustScaler`  
- 🔃 Train/Test Split  
- 💾 Saved with `joblib`  

---

## 🤖 Hugging Face Integration

🧠 We use **Hugging Face Transformers** for:
- Real-time crisis news interpretation  
- Weather alert embeddings  
- Enhanced context for disaster response  

```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="huggingface-model-id", filename="model_file")
```

---

## 🚀 How It Works

```text
📥 Data Collection: Usage history, weather, time
🧹 Preprocessing: Clean + feature extraction
🎯 Training: Random Forest on demand data
📈 Evaluation: MSE, R² score
🌐 Deployment: Flask app as REST API
```

---

## 💻 Installation

```bash
# ⬇️ Clone the repository
git clone https://github.com/yourusername/power-demand-prediction.git
cd power-demand-prediction

# 🛠️ (Optional) Create a virtual environment
python -m venv venv

# ▶️ Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 📦 Install dependencies
pip install -r requirements.txt

# 🚀 Run the app
python app.py

# 🌐 Visit in browser
http://127.0.0.1:5000/
```

---

## 🎯 Usage

```text
🔢 Input:
  - Timestamp (Month, Day, Hour)
  - Weather: Temperature, Humidity, Pressure
  - Region data

📊 Output:
  - Predicted Power Demand (kW)
  - Resource Allocation Suggestion
```

---

## 🚀 Future Enhancements

- 🌐 Live weather + disaster feeds  
- 🗺️ GIS-based regional predictions  
- 🧠 Switch to LSTM or XGBoost models  
- 📊 Interactive dashboards for real-time tracking  
- 🔍 Anomaly detection for sudden demand spikes  

---

## 🏁 Conclusion

This project empowers **disaster response** teams by offering:

- 🧭 Smarter resource allocation  
- ⚡ Grid resilience planning  
- 🏥 Ensured power supply to critical services  

Let’s build a **future-ready**, energy-aware disaster response system 🔋🌪️