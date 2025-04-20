#  Apply feature-scaling techniques like standardization and normalization to numerical features.


#  Perform feature dummification to convert categorical variables into numerical representations.

import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler

# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample dataset
data = {
    "Age": [25, 30, 35, 40, 28, 32, 38, 45],
    "Income": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 90000],
    "Education": ["Bachelor", "Master", "PhD", "Master", "Bachelor", "Master", "PhD", "Master"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Single", "Married", "Single", "Married"]
}

df = pd.DataFrame(data)

# Standardization (Z-score scaling)
scaler_std = StandardScaler()
df[['Age', 'Income']] = scaler_std.fit_transform(df[['Age', 'Income']])
print('\n')
print(df)

# Normalization (Min-Max scaling)
scaler_norm = MinMaxScaler()
df[['Age', 'Income']] = scaler_norm.fit_transform(df[['Age', 'Income']])
print('\n')
print(df)

# Dummification (Convert categorical 'Gender' column)
df = pd.get_dummies(df, columns=['Education', 'Marital_Status'], drop_first=True)
print('\n')
print(df)
