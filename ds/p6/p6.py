# Regression and Its Types
#  Implement simple linear regression using a dataset.
#  Explore and interpret the regression model coefficients and goodness-of-fit measures.
#  Extend the analysis to multiple linear regression and assess the impact of additional predictors

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"Simple Linear Regression (One input ➝ One output)"
# Sample data: Hours studied vs Marks scored
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [35, 40, 50, 55, 60, 65, 70, 80]
}
df = pd.DataFrame(data)

# Split X (input) and y (output)
X = df[['Hours_Studied']]
y = df['Marks']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict and evaluate
predictions = model.predict(X)

print("Intercept (b₀):", model.intercept_)
print("Coefficient (b₁):", model.coef_[0])
print("R² Score:", r2_score(y, predictions))  # Goodness of fit
print("Mean Squared Error:", mean_squared_error(y, predictions))

" Multiple Linear Regression (More inputs ➝ One output)"
# More complex data
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Sleep_Hours': [6, 7, 6, 5, 7, 6, 8, 7],
    'Attendance': [70, 75, 80, 82, 85, 88, 90, 95],
    'Marks': [35, 40, 50, 55, 60, 65, 70, 80]
}
df = pd.DataFrame(data)

X = df[['Hours_Studied', 'Sleep_Hours', 'Attendance']]
y = df['Marks']

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("\nIntercept (b₀):", model.intercept_)
print("Coefficients (b₁, b₂, b₃):", model.coef_)
print("R² Score:", r2_score(y, predictions))
