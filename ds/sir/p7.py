import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

# Step 1: Generate a simple binary classification dataset
np.random.seed(42)
X = np.random.rand(100, 2) * 10  # Two independent features
y = (X[:, 0] + X[:, 1] > 10).astype(int)  # Binary target (0 or 1)

# Step 2: Convert data into a DataFrame for easy handling
df = pd.DataFrame({'Feature1': X[:, 0], 'Feature2': X[:, 1], 'Target': y})

# Display the first few rows of the DataFrame
print("Dataset:\n", df.head())

# Step 3: Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Logistic Regression Model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

# Step 5: Train Decision Tree Model
tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

# Step 6: Evaluate Logistic Regression Performance
print("\nLogistic Regression Performance:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_log):.4f}")
print(classification_report(y_test, y_pred_log))

# Step 7: Evaluate Decision Tree Performance
print("\nDecision Tree Performance:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_tree):.4f}")
print(classification_report(y_test, y_pred_tree))

# Step 8: Plot Confusion Matrices for Both Models
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Confusion Matrix for Logistic Regression
ConfusionMatrixDisplay.from_estimator(log_model, X_test, y_test, ax=ax[0])
ax[0].set_title("Logistic Regression")

# Confusion Matrix for Decision Tree
ConfusionMatrixDisplay.from_estimator(tree_model, X_test, y_test, ax=ax[1])
ax[1].set_title("Decision Tree")

plt.show()
