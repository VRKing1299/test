from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
# Load the football dataset from CSV
dataset = pd.read_csv('argfrc_dataset.csv')
# Separate features (X) and labels (y)
X = dataset[['Argentina', 'France']].values
y = dataset['Result'].values
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
# Create a Naïve Bayes classifier (Gaussian Naïve Bayes for continuousfeatures)
clf = GaussianNB()
# Train the classifier on the training data
clf.fit(X_train, y_train)
# Make predictions on the test data
y_pred = clf.predict(X_test)
# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)