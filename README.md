# ⚡ Electricity Demand Forecasting – Delhi (5-Minute Intervals)

This project builds a machine learning model to predict **electricity demand** in Delhi using high-resolution **5-minute interval data**. The model is trained on temporal and environmental features to forecast demand accurately, making it valuable for smart grid optimization and energy planning.

---

## 📊 Dataset

**Source**: [Delhi 5-Minute Electricity Demand for Forecasting](https://www.kaggle.com/datasets/yug201/delhi-5-minute-electricity-demand-for-forecasting)

- **Records**: Over 1 million entries
- **Time span**: 2016–2024
- **Columns**: 
  - `datetime`
  - `Power demand (kW)`
  - `Temperature (°C)`
  - `Humidity (%)`
  - And other environmental conditions

---

## 🧠 Model Overview

We use a **Random Forest Regressor** to predict electricity demand based on:

- **Datetime Features** (hour, day, month, weekday, etc.)
- **Temperature & Humidity**
- **Lagged Demand Features** (optional)
- **Rolling Averages** (optional)

### ⚙️ Preprocessing Includes:

- `pd.to_datetime()` to parse timestamps
- Feature extraction (hour, day, etc.)
- Handling outliers using `winsorize`
- Scaling inputs using `RobustScaler`
- Train/Validation/Test split
- Model saving using `joblib`

---

