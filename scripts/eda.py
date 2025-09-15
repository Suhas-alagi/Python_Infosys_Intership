import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed_data.csv")

# Time Series Plot
plt.figure(figsize=(8,4))
plt.plot(df['datetime'], df['pollutant_avg'], marker='o')
plt.title('Pollutant Avg Time Series')
plt.xlabel('Date')
plt.ylabel('Pollutant Avg')
plt.tight_layout()
plt.savefig('static/pollutant_avg_plot.png')
plt.close()

# Distribution Plot
plt.figure(figsize=(6,4))
sns.histplot(df['pollutant_avg'].dropna(), bins=20, kde=True)
plt.title('Pollutant Avg Distribution')
plt.xlabel('Pollutant Avg')
plt.tight_layout()
plt.savefig('static/distribution_plot.png')
plt.close()

# Correlation Plot
plt.figure(figsize=(6,4))
corr = df[['pollutant_min','pollutant_max','pollutant_avg']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Pollutant Feature Correlations')
plt.tight_layout()
plt.savefig('static/correlation_plot.png')
plt.close()

# Statistical Summary
summary = df[['pollutant_min','pollutant_max','pollutant_avg']].describe().round(2)
summary.to_csv('static/summary.csv')
print("✅ EDA plots and summary generated.")