import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats.mstats import winsorize

# -------------------------------
# Load and Preprocess Data
# -------------------------------
df = pd.read_csv(r"D:\GitHubProject\ElectricityDemandPrediction\ElectricityDemandPredicter\ElectricityDemand\powerdemand_5min_2021_to_2024_with weather.csv")
df['datetime'] = pd.to_datetime(df['datetime'])

# Drop unnecessary column if exists
df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')

# Drop rows with missing values and duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Time-based Features
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.dayofweek

# Cyclical encoding
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
df['day_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
df['day_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

# Winsorize only the target (Power demand)
df['Power demand'] = winsorize(df['Power demand'], limits=[0.01, 0.01])

# Drop unused raw time features
df.drop(columns=['datetime', 'month', 'hour', 'day_of_week'], inplace=True)

# -------------------------------
# Feature Selection
# -------------------------------
features = [
    'temp', 'dwpt', 'wspd', 'wdir', 'pres', 'rhum',
    'year', 'month_cos', 'hour_sin', 'hour_cos'
]
target = 'Power demand'

X = df[features]
y = df[target]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Drop any remaining NaNs
X_train, y_train = X_train.dropna(), y_train[X_train.index]
X_val, y_val = X_val.dropna(), y_val[X_val.index]
X_test, y_test = X_test.dropna(), y_test[X_test.index]

# -------------------------------
# Train Optimized Random Forest
# -------------------------------
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# -------------------------------
# Evaluate Model
# -------------------------------
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("📊 Model Evaluation")
print("-" * 30)
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# -------------------------------
# Save the Model
# -------------------------------
joblib.dump(model, 'random_forest_model.pkl')
print("✅ Model saved successfully!")
