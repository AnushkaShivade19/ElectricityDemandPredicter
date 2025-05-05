import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import RobustScaler
from scipy.stats.mstats import winsorize


# Load Data
df = pd.read_csv("powerdemand_5min_2021_to_2024_with weather.csv")
df['datetime'] = pd.to_datetime(df['datetime'])

# Handle missing values
df['wdir'] = df['wdir'].fillna(df['wdir'].median())
df['moving_avg_3'] = df['moving_avg_3'].ffill()


# Winsorize target variable
df['Power demand'] = winsorize(df['Power demand'], limits=[0.01, 0.01])

# Remove duplicates
df = df.drop_duplicates()

# Feature Engineering
df['day_of_week'] = df['datetime'].dt.dayofweek
df['hour_of_day'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.month
df['hour_sin'] = np.sin(2 * np.pi * df['hour_of_day'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour_of_day'] / 24)
df['day_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
df['day_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

# Scaling
numerical_cols = ['Power demand', 'temp', 'dwpt', 'rhum', 'wdir', 'wspd', 'pres', 'moving_avg_3']
scaler = RobustScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Feature Selection
features = [
    'temp', 'dwpt', 'rhum', 'wdir', 'wspd', 'pres', 'moving_avg_3',
    'day_of_week', 'hour_of_day', 'month',
    'hour_sin', 'hour_cos', 'day_sin', 'day_cos'
]
target = 'Power demand'

X = df[features]
y = df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict & Evaluate
y_pred = model.predict(X_test)
y_pred_2d = y_pred.reshape(-1, 1)
y_test_2d = y_test.values.reshape(-1, 1)

y_pred_original = scaler.inverse_transform(
    np.concatenate([y_pred_2d, np.zeros((len(y_pred_2d), len(numerical_cols) - 1))], axis=1)
)[:, 0]

y_test_original = scaler.inverse_transform(
    np.concatenate([y_test_2d, np.zeros((len(y_test_2d), len(numerical_cols) - 1))], axis=1)
)[:, 0]

# Metrics
mse = mean_squared_error(y_test_original, y_pred_original)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_original, y_pred_original)

print("Model Evaluation")
print("-" * 30)
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# Save model and scaler for Flask API
joblib.dump(model, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("\nModel and scaler saved successfully!")
