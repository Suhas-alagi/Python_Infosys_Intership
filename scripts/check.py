import pandas as pd

df = pd.read_csv("data/world_air_quality.csv", on_bad_lines='skip')
print("✅ CSV Columns Found:", df.columns.tolist())
print("\nFirst 5 Rows:")
print(df.head())
