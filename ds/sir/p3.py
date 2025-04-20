import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# Step 1: Create a sample dataset
data = pd.DataFrame({
    "Age": [25, 30, 35, 40, 28, 32, 38, 45],
    "Income": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 90000],
    "Education": ["Bachelor", "Master", "PhD", "Master", "Bachelor", "Master", "PhD", "Master"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Single", "Married", "Single", "Married"]
})

# Display the original data
print("Original Data:\n", data)

# Step 2: Check data types
print("\nData Types:\n", data.dtypes)

# Step 3: Apply Standardization (Z-Score Scaling) to 'Age' and 'Income'
scaler = StandardScaler()
data[['Age_scaled', 'Income_scaled']] = scaler.fit_transform(data[['Age', 'Income']])

# Display data after standardization
print("\nData after Standardization:\n", data[['Age', 'Income', 'Age_scaled', 'Income_scaled']])

# Step 4: Apply Normalization (Min-Max Scaling) to 'Age' and 'Income'
normalizer = MinMaxScaler()
data[['Age_normalized', 'Income_normalized']] = normalizer.fit_transform(data[['Age', 'Income']])

# Display data after normalization
print("\nData after Normalization:\n", data[['Age', 'Income', 'Age_normalized', 'Income_normalized']])

# Step 5: Encode categorical variables ('Education' and 'Marital_Status') using Label Encoding
le = LabelEncoder()
data['Education_code'] = le.fit_transform(data['Education'])
data['Marital_Status_code'] = le.fit_transform(data['Marital_Status'])

# Display data after encoding categorical variables
print("\nData with Encoded Categorical Variables:\n", data)

# Step 6: Perform Feature Dummification (One-Hot Encoding) for categorical variables
data_dummified = pd.get_dummies(data, columns=["Education", "Marital_Status"], drop_first=True)

# Display data after dummification
print("\nData after Dummification:\n", data_dummified)

# Check data types again after transformations
print("\nData Types After Transformations:\n", data.dtypes)
