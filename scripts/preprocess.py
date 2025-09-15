import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, na_values=['NA'])
    df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
    df = df.dropna(subset=['last_update'])
    df.rename(columns={'last_update': 'datetime'}, inplace=True)
    df = df.sort_values('datetime')
    df = df.set_index('datetime')

    # Convert pollutant columns to numeric
    for col in ['pollutant_min', 'pollutant_max', 'pollutant_avg']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Only aggregate numeric columns
    numeric_cols = ['latitude', 'longitude', 'pollutant_min', 'pollutant_max', 'pollutant_avg']
    numeric_df = df.groupby(['pollutant_id']).resample('D')[numeric_cols].mean().reset_index()

    # For text columns, take the mode per day and pollutant
    text_cols = ['country', 'state', 'city', 'station']
    text_df = df.groupby(['pollutant_id']).resample('D')[text_cols].agg(lambda x: x.mode()[0] if not x.mode().empty else None).reset_index()

    # Merge back
    final_df = pd.merge(text_df, numeric_df, on=['pollutant_id', 'datetime'])
    # Fill missing numeric values
    for col in ['pollutant_min', 'pollutant_max', 'pollutant_avg']:
        final_df[col] = final_df[col].interpolate().ffill().bfill()
    return final_df

if __name__ == "__main__":
    df = load_and_clean_data("data/world_air_quality.csv")
    print(df.head())
    df.to_csv("data/processed_data.csv", index=False)
    print("✅ Data preprocessing complete. File saved as data/processed_data.csv")
