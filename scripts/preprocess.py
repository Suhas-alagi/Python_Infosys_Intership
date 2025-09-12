import pandas as pd
def load_and_clean_data(file_path):
    # Load CSV, skip bad lines
    df = pd.read_csv(file_path, on_bad_lines='skip')

    # Convert last_update to datetime
    df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
    df = df.dropna(subset=['last_update'])
    df.rename(columns={'last_update': 'datetime'}, inplace=True)

    # Sort and set index
    df = df.sort_values('datetime')
    df = df.set_index('datetime')

    # Separate numeric and text columns
    numeric_df = df[['pollutant_min', 'pollutant_max', 'pollutant_avg']].resample('D').mean()

    # For text columns, take the most frequent value for that day (mode)
    text_cols = ['country', 'state', 'city', 'station']
    text_df = df[text_cols].resample('D').agg(lambda x: x.mode()[0] if not x.mode().empty else None)

    # Combine back
    final_df = text_df.join(numeric_df)

    # Fill missing numeric values
    final_df[['pollutant_min','pollutant_max','pollutant_avg']] = final_df[['pollutant_min','pollutant_max','pollutant_avg']].interpolate()
    return final_df
if __name__ == "__main__":
    df = load_and_clean_data("data/world_air_quality.csv")
    print(df.head())
    df.to_csv("data/processed_data.csv")
    print("✅ Data preprocessing complete. File saved as data/processed_data.csv")
