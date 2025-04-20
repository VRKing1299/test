# 📌 Section 1: Creating a Sample DataFrame
import pandas as pd
import numpy as np

# Sample data
data = {
    'Student ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Sarah Lee'],
    'Age': [20, 22, 21, 23, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [92, 85, 90, 72, 88]
}

# Creating a DataFrame
df = pd.DataFrame(data)
# Displaying the DataFrame
print("📄 Sample DataFrame:")
print(df)

# 📌 Section 2: Reading from CSV
# Note: Make sure the path is valid on your system
df_csv = pd.read_csv('C:\\Users\\khi\\Documents\\Data Science\\Dta.csv')
print("\n📄 Data from CSV:")
print(df_csv)

# 📌 Section 3: Reading from JSON
# Note: Make sure the path is valid on your system
df_json = pd.read_json('C:\\Users\\khi\\Documents\\Data Science\\data.json')
print("\n📄 Data from JSON:")
print(df_json)

# 📌 Section 4: Handling Missing Values
# Sample data with missing values
data_missing = {
    'Student ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', np.nan],
    'Age': [20, 22, np.nan, 23, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [92, 85, 90, np.nan, 88]
}

# Creating a new DataFrame with missing values
df_missing = pd.DataFrame(data_missing)

# Finding null values
print("\n🔍 Missing Values:")
print(df_missing.isna().sum())

# Filling missing numerical values with mean
df_missing['Age'].fillna(df_missing['Age'].mean(), inplace=True)
df_missing['Marks'].fillna(df_missing['Marks'].mean(), inplace=True)

# Displaying after handling missing values
print("\n🧹 After Handling Missing Values:")
print(df_missing)

# 📌 Section 5: Handling Outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Removing outliers in 'Age' and 'Marks'
df_cleaned = remove_outliers(df_missing, 'Age')
df_cleaned = remove_outliers(df_cleaned, 'Marks')

print("\n🧼 Final Cleaned Data (Outliers Removed):")
print(df_cleaned)

# 📌 Section 6: Filtering, Sorting, Grouping, and Transforming Data
# Sample dataset
data2 = pd.DataFrame({
    "Age": [25, 30, 35, 40, 28, 32, 38, 45],
    "Income": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 90000],
    "Education": ["Bachelor", "Master", "PhD", "Master", "Bachelor", "Master", "PhD", "Master"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Single", "Married", "Single", "Married"]
})
print("\n📄 Original Data for Transformation:")
print(data2)

# Filtering data (Age > 30)
filtered_data = data2[data2['Age'] > 30]
print("\n🔍 Filtered Data (Age > 30):")
print(filtered_data)

# Sorting data by Income in descending order
sorted_data = data2.sort_values(by="Income", ascending=False)
print("\n📊 Sorted Data by Income (Descending):")
print(sorted_data)

# Grouping by Education and calculating mean Income
grouped_data = data2.groupby("Education")['Income'].mean().reset_index()
print("\n📈 Mean Income by Education:")
print(grouped_data)

# Transform: Creating new column for income in thousands
data2['Income_in_thousands'] = data2['Income'] / 1000
print("\n💰 Data with Income in Thousands:")
print(data2)
