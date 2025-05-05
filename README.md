🌍 Power Demand Prediction for Disaster Management ⚡
🌟 Overview
The Power Demand Prediction project focuses on accurately forecasting electricity demand in disaster-prone regions such as areas affected by floods, earthquakes, or storms. By leveraging machine learning, we predict power consumption patterns, helping disaster management agencies and energy providers optimize resource allocation, minimize grid strain, and ensure swift recovery.

By integrating real-time data and advanced models, this tool becomes essential in disaster preparedness, ensuring timely power restoration and efficient grid management during emergencies.

🧠 Key Features and Applications
📈 Accurate Power Demand Prediction
Predicts power consumption using multiple features such as:

Time of Day (hour, day, month)

Weather Conditions (temperature, humidity, pressure)

Seasonal Variations (peak demand seasons like summer or winter)

Special Events & Holidays (festivities, public holidays)

🚨 Disaster Response & Recovery
Helps forecast energy needs during and after disasters.

Optimizes power grid allocation for efficient recovery efforts.

Prioritizes power restoration for critical areas such as hospitals, shelters, and emergency services.

💡 Resource Allocation & Load Balancing
Efficiently allocates resources by predicting high-demand areas.

Balances power loads to prevent grid overuse and minimize strain during crises.

🔌 Integration with IoT & Smart Grids
Integrates with smart grids and IoT sensors for real-time monitoring of energy consumption.

Enables dynamic power distribution, prioritizing high-need areas in times of disaster.

🔮 Scenario Planning & Simulation
Simulates different disaster scenarios to help agencies plan for worst-case events.

Provides insights into potential infrastructure vulnerabilities based on historical data.

📊 Disaster Management Dashboards
Visualizes real-time power demand predictions.

Offers location-specific insights, highlighting areas with the highest demand.

Sends alerts and notifications for potential grid issues.

📊 Dataset
Delhi 5-Minute Electricity Demand for Forecasting
We use a high-resolution dataset for forecasting electricity demand in Delhi. The data spans 2016–2024 and is recorded at 5-minute intervals. It's perfect for smart grid optimization and energy management.

Source: Delhi 5-Minute Electricity Demand for Forecasting

Records: Over 1 million entries

Features:

datetime

Power demand (kW)

Temperature (°C)

Humidity (%)

Other environmental factors

🧠 Model Overview
The Power Demand Prediction Model uses a Random Forest Regressor to predict electricity demand based on:

Datetime Features (e.g., day, month, hour)

Temperature & Humidity

Lagged Demand Features (optional)

Rolling Averages (optional)

⚙️ Preprocessing Steps:
pd.to_datetime() to parse timestamps

Feature extraction (e.g., extracting hour, day)

Outlier handling using winsorize

Scaling using RobustScaler

Train/Validation/Test splits

Saving the model with joblib

🤖 Hugging Face Integration
For enhanced feature extraction and to handle more complex data patterns, Hugging Face's pre-trained transformer models are integrated into the system. This brings added flexibility for more accurate predictions and real-time processing of unforeseen inputs like crisis news or weather forecasts.

Example Usage with Hugging Face:
python
Copy
Edit
from huggingface_hub import hf_hub_download

# Download the model from Hugging Face
model_path = hf_hub_download(repo_id="huggingface-model-id", filename="model_file")
🚀 How It Works
Data Collection: Collect historical data on power usage, weather, and timestamps.

Data Preprocessing: Clean and extract relevant features (e.g., weather, time of day).

Model Training: Use Random Forest Regressor to predict future power demand.

Prediction & Evaluation: Evaluate model performance with metrics like Mean Squared Error (MSE) and R-squared.

Deployment: Deploy as a Flask API for real-time predictions.

💻 Installation
Step-by-Step Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/power-demand-prediction.git
Navigate to the project folder:

bash
Copy
Edit
cd power-demand-prediction
Create a virtual environment (optional):

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

For Windows:

bash
Copy
Edit
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask application:

bash
Copy
Edit
python app.py
The application will be accessible at http://127.0.0.1:5000/.

🎯 Usage
Input: Provide features such as:

Timestamp (Month, Day, Hour)

Weather Data (Temperature, Humidity, Pressure)

Location (Region)

Output: Get:

Predicted Power Demand

Resource Allocation Suggestions

🚀 Future Enhancements
Real-Time Data Integration: Integrate live weather and grid data for continuous updates.

Geospatial Data: Improve predictions with GIS and infrastructure data.

Advanced Models: Test with models like XGBoost, LSTM for more precision.

Interactive Dashboards: Build real-time analytics and disaster simulations.

🏁 Conclusion
This project aids in disaster management by predicting electricity demand in disaster-prone areas. It enables better resource allocation, faster power restoration, and ensures that critical services (e.g., hospitals, shelters) remain powered during emergencies.

By combining machine learning, Hugging Face integration, and smart grid technology, it empowers agencies and energy providers to plan, respond, and recover more effectively during disasters.







