# Logistic Regression and Decision Tree
#  Build a logistic regression model to predict a binary outcome.
#  Evaluate the model's performance using classification metrics (e.g., accuracy, precision, recall).
#  Construct a decision tree model and interpret the decision rules for classification.

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Marks': [40, 50, 60, 30, 90, 85, 20, 75],
    'Attendance': [60, 70, 80, 50, 95, 90, 40, 85],
    'Pass': [0, 1, 1, 0, 1, 1, 0, 1]  # Target variable (binary)
}

df = pd.DataFrame(data)

# Step 1: Split input (X) and output (y)
X = df[['Marks', 'Attendance']]
y = df['Pass']

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Build model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Predict and Evaluate
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Build decision tree model
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Predict
y_pred_tree = tree_model.predict(X_test)

# Evaluate
print("Accuracy (Decision Tree):", accuracy_score(y_test, y_pred_tree))

# Visualize the tree
plt.figure(figsize=(10,6))
tree.plot_tree(tree_model, feature_names=['Marks', 'Attendance'], class_names=['Fail', 'Pass'], filled=True)
plt.title("Decision Tree")
plt.show()
