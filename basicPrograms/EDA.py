# ==========================================
# 📌 Pandas Tutorial using Employee Dataset
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
# 1. LOAD AND INSPECT DATA
# -------------------------
df = pd.read_csv("data.csv")
print("🔹 Dataset Info:")
print(df.info())          # Summary of dataset
print("\n🔹 First 5 Rows:")
print(df.head())          # First 5 rows
print("\n🔹 Summary Stats:")
print(df.describe())      # Stats for numeric columns
print("\n🔹 Columns:", df.columns.tolist())
print("🔹 Shape:", df.shape)   # (rows, cols)

# 2. DATA CLEANING
# -----------------
print("\n🔹 Missing Values Count:")
print(df.isnull().sum())
# Example: Fill missing bonuses with average bonus
df['bonus'].fillna(df['bonus'].mean(), inplace=True)
# Example: Drop rows where city is missing
df.dropna(subset=['city'], inplace=True)
# Rename a column
df.rename(columns={'performance': 'employee_performance'}, inplace=True)
# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# 3. DATA SELECTION & FILTERING
# ------------------------------
print("\n🔹 Selecting 'name' and 'salary':")
print(df[['name', 'salary']].head())
# Filter: employees older than 35
older = df[df['age'] > 35]
print("\n🔹 Employees older than 35:\n", older)
# Filter: IT department + salary > 60,000
it_high_salary = df[(df['department'] == 'IT') & (df['salary'] > 60000)]
print("\n🔹 High salary IT employees:\n", it_high_salary)
# Sort by salary (descending)
sorted_df = df.sort_values(by='salary', ascending=False)
print("\n🔹 Sorted by Salary:\n", sorted_df[['name', 'salary']].head())

# 4. DATA AGGREGATION & GROUPING
# -------------------------------
# Average salary by department
avg_salary_dept = df.groupby('department')['salary'].mean()
print("\n🔹 Average Salary by Department:\n", avg_salary_dept)
# Multiple aggregations
agg_df = df.groupby('department').agg({'salary': 'mean', 'bonus': 'sum'})
print("\n🔹 Aggregated Salary & Bonus by Department:\n", agg_df)

# 5. ADDING & MODIFYING COLUMNS
# -------------------------------
# Total compensation = salary + bonus
df['total_compensation'] = df['salary'] + df['bonus']
# Salary level classification
df['salary_level'] = df['salary'].apply(lambda x: 'High' if x > 55000 else 'Low')
print("\n🔹 Added Columns:\n", df[['name', 'salary', 'bonus', 'total_compensation', 'salary_level']].head())

# 6. DATA VISUALIZATION (Pandas + Matplotlib)
# -------------------------------------------
# Bar chart: Average salary per department
avg_salary_dept.plot(kind='bar', title="Avg Salary by Department")
plt.ylabel("Salary")
plt.show()
# Histogram: Age distribution
df['age'].plot(kind='hist', bins=5, title="Age Distribution")
plt.xlabel("Age")
plt.show()
# Scatter plot: Salary vs Bonus
df.plot(x='salary', y='bonus', kind='scatter', title="Salary vs Bonus")
plt.show()

# 7. MERGING & JOINING
# ---------------------
# Create another small dataframe (department head info)
dept_heads = pd.DataFrame({
    'department': ['Sales', 'HR', 'IT', 'Finance'],
    'head': ['Karan', 'Priya', 'Amit', 'Sonia']
})
# Merge with employees
merged_df = pd.merge(df, dept_heads, on='department', how='inner')
print("\n🔹 Merged with Dept Heads:\n", merged_df[['name', 'department', 'head']].head())

# 8. RESHAPING DATA
# ------------------
# Pivot: department as index, performance count
pivot_table = df.pivot_table(values='salary', index='department', columns='employee_performance', aggfunc='count', fill_value=0)
print("\n🔹 Pivot Table (Dept vs Performance Count):\n", pivot_table)

# 9. EXPORTING DATA
# ------------------
df.to_csv("cleaned_employees.csv", index=False)
df.to_excel("cleaned_employees.xlsx", index=False)
print("\n✅ Data exported to cleaned_employees.csv and cleaned_employees.xlsx")

# 10. ADVANCED TECHNIQUES
# ------------------------
# Correlation between age, salary, bonus
correlation_matrix = df[['age', 'salary', 'bonus']].corr()
print("\n🔹 Correlation Matrix:\n", correlation_matrix)
# Detect & remove outliers in salary using IQR
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
df_no_outliers = df[~((df['salary'] < (Q1 - 1.5 * IQR)) | (df['salary'] > (Q3 + 1.5 * IQR)))]
print("\n🔹 Dataset without salary outliers:\n", df_no_outliers[['name', 'salary']])
 
 