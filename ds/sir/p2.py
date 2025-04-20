import pandas as pd
import numpy as np

# Step 1: Creating the sample data
data = {
    'Student ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Sarah Lee'],
    'Age': [20, 22, 21, 23, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [92, 85, 90, 72, 88]
}

# Step 2: Creating a DataFrame
df = pd.DataFrame(data)

# Step 3: Displaying the DataFrame
print(df)

# Step 4: Save DataFrame to an Excel file
df.to_excel('/content/drive/MyDrive/student_data.xlsx', index=False)

# Step 5: Read CSV file into a DataFrame
df_csv = pd.read_csv('/content/drive/MyDrive/Data.csv')
print(df_csv)

# Step 6: Read JSON file into a DataFrame
df_json = pd.read_json('/content/drive/MyDrive/data.json')
print(df_json)

# Step 7: Sample data with some missing (null) values
data_with_nulls = {
    'Student ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', np.nan],
    'Age': [20, 22, np.nan, 23, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [92, 85, 90, np.nan, 88]
}

# Step 8: Creating DataFrame with missing values
df_nulls = pd.DataFrame(data_with_nulls)
print(df_nulls)

# Step 9: Finding null values
print(df_nulls.isna().sum())

# Step 10: Handling Missing Values
df_nulls['Age'].fillna(df_nulls['Age'].mean(), inplace=True)
df_nulls['Marks'].fillna(df_nulls['Marks'].mean(), inplace=True)
print("\nData after filling missing values:\n", df_nulls)

# Step 11: Handling Outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Step 12: Removing outliers in 'Age' and 'Marks' columns
df_cleaned = remove_outliers(df_nulls, 'Age')
df_cleaned = remove_outliers(df_cleaned, 'Marks')

# Step 13: Displaying cleaned data
print("\nFinal Cleaned Data:\n", df_cleaned)

# Step 14: Creating another sample dataset for filtering, sorting, and grouping operations
data2 = {
    "Age": [25, 30, 35, 40, 28, 32, 38, 45],
    "Income": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 90000],
    "Education": ["Bachelor", "Master", "PhD", "Master", "Bachelor", "Master", "PhD", "Master"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Single", "Married", "Single", "Married"]
}

# Step 15: Creating DataFrame for operations
df2 = pd.DataFrame(data2)
print("\nData with 'Age' and 'Income':\n", df2)

# Step 16: Filtering data where Age > 30
filtered_data = df2[df2['Age'] > 30]
print("\nFiltered Data (Age > 30):\n", filtered_data)

# Step 17: Sorting data by Income in descending order
sorted_data = df2.sort_values(by="Income", ascending=False)
print("\nSorted Data by Income (Descending):\n", sorted_data)

# Step 18: Grouping data by Education and calculating mean Income
grouped_data = df2.groupby("Education")['Income'].mean().reset_index()
print("\nMean Income by Education:\n", grouped_data)

# Step 19: Adding a new column for Income in thousands
df2['Income_in_thousands'] = df2['Income'] / 1000
print("\nData with Income in Thousands:\n", df2)

# Step 20: Adding incorrect column (should be Income in thousands)
# Fixing the issue by using the correct data
df2['Income_in_thousands'] = grouped_data['Income'] / 1000
print("\nFixed Data with Income in Thousands (using correct data):\n", df2)
