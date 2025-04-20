#  Read data from CSV and JSON files into a data frame.
print("Read data from CSV and JSON files into a data frame.")
import pandas as pd
df_csv=pd.read_csv('C:\\Users\\VEDANT RAJPUT\\pract\\ds\\p1\\student_data.csv')
print (df_csv)
df_json=pd.read_json('C:\\Users\\VEDANT RAJPUT\\pract\\ds\\p1\\student_data.json')
print (df_json)


#  Perform basic data pre-processing tasks such as handling missing values and outliers.
print(' Perform basic data pre-processing tasks such as handling missing values and outliers.')
'removing rows with missing values'
# df_csv_clean=df_csv.dropna()
# print(df_csv_clean)
# # Or fill missing values with a default (e.g., 0)
df_csv_filled = df_csv.fillna(0)
# "sir's method"
df_csv['Age'].fillna(df_csv['Age'].mean(), inplace=True)
print(df_csv)

'removing outliers'
df_csv_no_outliers = df_csv[(df_csv['Age']>=18)&(df_csv['Age']<=100)]
print(df_csv_no_outliers)
    

#  Manipulate and transform data using functions like filtering, sorting, and grouping
print('\n')
print(" Manipulate and transform data using functions like filtering, sorting, and grouping")
filtered=df_csv_no_outliers[(df_csv_no_outliers["Marks"]>=30)]
print(filtered)
sorted = df_csv_no_outliers.sort_values(by='Marks', ascending=True)
print(sorted)
group=df_csv_no_outliers.groupby('Gender').size()
print(group)