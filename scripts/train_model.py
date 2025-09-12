import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import numpy as np



# 1. Load processed data correctly
df = pd.read_csv("data/processed_data.csv", parse_dates=['datetime'])
df.set_index('datetime', inplace=True)

# Clean column names
df.columns = df.columns.str.strip()

print("✅ Columns in DataFrame:", df.columns.tolist())
print(df.head())

# We'll forecast pollutant_avg
series = df['pollutant_avg'].ffill()


