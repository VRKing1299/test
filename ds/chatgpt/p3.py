import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 🧹 First, select only numerical columns for scaling
df_csv_no_outliers = pd.read_csv('C:\\Users\\VEDANT RAJPUT\\pract\\ds\\p1\\student_data.csv')
numerical_features = df_csv_no_outliers[['Age', 'Marks']]

# ✅ 1. Standardization (mean = 0, std = 1)
scaler_standard = StandardScaler()
standardized = scaler_standard.fit_transform(numerical_features)
df_standardized = pd.DataFrame(standardized, columns=['Age_Standardized', 'Marks_Standardized'])

print("🔹 Standardized Data:")
print(df_standardized)

# ✅ 2. Normalization (values between 0 and 1)
scaler_minmax = MinMaxScaler()
normalized = scaler_minmax.fit_transform(numerical_features)
df_normalized = pd.DataFrame(normalized, columns=['Age_Normalized', 'Marks_Normalized'])

print("\n🔹 Normalized Data:")
print(df_normalized)

# ✅ 3. Dummification (convert Gender and Grade to numbers)
df_dummies = pd.get_dummies(df_csv_no_outliers, columns=['Gender', 'Grade'], drop_first=True)

print("\n🔹 Dummified DataFrame (with numerical representations of categories):")
print(df_dummies)
