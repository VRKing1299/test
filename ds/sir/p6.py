import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Generate synthetic dataset
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Independent variable
y = 2.5 * X + np.random.randn(100, 1) * 2  # Linear relation with noise

# Convert to DataFrame for easy handling
df = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})

# Display the DataFrame for verification
print("Dataset:\n", df.head())

# Step 2: Visualize the Data Before Model Training
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['X'], y=df['y'], color='blue')
plt.xlabel("X (Independent Variable)")
plt.ylabel("y (Dependent Variable)")
plt.title("Scatter Plot of Dataset Before Model Training")
plt.grid(True)
plt.show()

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Simple Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predictions from the model
y_pred = model.predict(X_test)

# Step 6: Model Coefficients and Performance Metrics
print(f"Intercept: {model.intercept_[0]:.4f}, Coefficient: {model.coef_[0][0]:.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")

# Step 7: Plot Regression Line
plt.scatter(X_test, y_test, color='blue', label="Actual")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Predicted")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Step 8: Multiple Linear Regression (Adding another predictor)
X_multi = np.hstack((X, np.random.rand(100, 1) * 5))  # Adding another independent variable

# Step 9: Split the multi-variable data
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multi, y, test_size=0.2, random_state=42)

# Step 10: Train Multiple Linear Regression Model
model_multi = LinearRegression()
model_multi.fit(X_train_multi, y_train_multi)

# Step 11: Predictions for Multiple Regression
y_pred_multi = model_multi.predict(X_test_multi)

# Step 12: Print Model Coefficients and R-squared for Multiple Regression
print(f"\nMultiple Regression Coefficients: {model_multi.coef_}")
print(f"Multiple Regression R-squared: {r2_score(y_test_multi, y_pred_multi):.4f}")
