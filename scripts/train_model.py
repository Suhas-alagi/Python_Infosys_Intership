import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("data/processed_data.csv")
# Features: latitude, longitude, pollutant_id (encoded), pollutant_min, pollutant_max
df['pollutant_id'] = df['pollutant_id'].astype('category').cat.codes
features = ['latitude', 'longitude', 'pollutant_id', 'pollutant_min', 'pollutant_max']
X = df[features]
y = df['pollutant_avg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Test MSE: {mse:.2f}, MAE: {mae:.2f}")

# Model Performance Bar Plot
plt.figure(figsize=(6,4))
plt.bar(['MSE','MAE'], [mse, mae], color=['blue','orange'])
plt.title('Model Performance')
plt.tight_layout()
plt.savefig('static/model_performance.png')
plt.close()

# Forecast Plot
plt.figure(figsize=(8,4))
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.title('Pollutant Avg Forecast')
plt.xlabel('Sample')
plt.ylabel('Pollutant Avg')
plt.legend()
plt.tight_layout()
plt.savefig('static/forecast_plot.png')
plt.close()

joblib.dump(model, "models/pollutant_avg_model.pkl")
print("✅ Model trained and saved to models/pollutant_avg_model.pkl")


