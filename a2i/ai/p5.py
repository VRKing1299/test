# Support Vector Machines


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load your dataset from a local file (e.g., CSV)
# Replace 'your_dataset.csv' with the actual path to your dataset file
data = pd.read_csv('Iris.csv')
# Assuming the target variable is in a column named 'target'
X = data.drop('Target', axis=1)
y = data['Target']
# Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)
# Create an SVM classifier
svm_classifier = SVC(kernel='linear') # You can choosedifferent kernels here
# Fit the classifier to the training data
svm_classifier.fit(X_train, y_train)
# Make predictions on the test data
y_pred = svm_classifier.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")