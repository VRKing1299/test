import pandas as pd

# ✅ 1. Read data from CSV and JSON files into a data frame
print("🔹 Read data from CSV and JSON files into a data frame.")
df_csv = pd.read_csv('C:\\Users\\VEDANT RAJPUT\\pract\\ds\\p1\\student_data.csv')
print(df_csv)

df_json = pd.read_json('C:\\Users\\VEDANT RAJPUT\\pract\\ds\\p1\\student_data.json')
print(df_json)

# ✅ 2. Perform basic data pre-processing: missing values and outliers
print('\n🔹 Perform basic data pre-processing tasks')

# Fill missing values in "Age" with the column's mean
df_csv['Age'].fillna(df_csv['Age'].mean(), inplace=True)

# Alternatively: fill all missing values with 0
df_csv_filled = df_csv.fillna(0)

# Remove outliers in Age (e.g., Age < 18 or > 100)
df_csv_no_outliers = df_csv[(df_csv['Age'] >= 18) & (df_csv['Age'] <= 100)]
print("\nCleaned data (No outliers):")
print(df_csv_no_outliers)

# ✅ 3. Manipulate and transform: filtering, sorting, grouping
print("\n🔹 Data manipulation and transformation:")

# Filter: Students with Marks >= 30
filtered = df_csv_no_outliers[df_csv_no_outliers["Marks"] >= 30]
print("\nFiltered students (Marks >= 30):")
print(filtered)

# Sort: Students by Marks in ascending order
sorted_df = df_csv_no_outliers.sort_values(by='Marks', ascending=True)
print("\nSorted students by Marks:")
print(sorted_df)

# Group: Count how many students per gender
group = df_csv_no_outliers.groupby('Gender').size()
print("\nGroup by Gender:")
print(group)
