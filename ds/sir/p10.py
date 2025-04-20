import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Set Seaborn style for better visual aesthetics
sns.set(style="whitegrid")

# Step 2: Load the Titanic dataset
df = sns.load_dataset("titanic")

# Step 3: Display first few rows of the dataset for a quick overview
print("First few rows of the dataset:")
print(df.head())

# Step 4: Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Step 5: Display summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Step 6: Count of passengers by class
plt.figure(figsize=(8, 5))
sns.countplot(x="class", data=df, palette="Set2")
plt.title("Number of Passengers by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()

# Step 7: Survival rate by class
plt.figure(figsize=(8, 5))
sns.barplot(x="class", y="survived", data=df, palette="coolwarm")
plt.title("Survival Rate by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# Step 8: Survival rate by gender
plt.figure(figsize=(8, 5))
sns.barplot(x="sex", y="survived", data=df, palette="viridis")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.show()

# Step 9: Age distribution of Titanic survivors vs non-survivors
plt.figure(figsize=(10, 5))
sns.histplot(df[df["survived"] == 1]["age"], bins=30, kde=True, color="green", label="Survived")
sns.histplot(df[df["survived"] == 0]["age"], bins=30, kde=True, color="red", label="Not Survived")
plt.legend()
plt.title("Age Distribution of Titanic Survivors vs Non-Survivors")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
