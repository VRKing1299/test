import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Sample dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'Study_Hours': [2, 4, 3.5, 5, 6, 1, 3, 4.5],
    'Marks': [50, 75, 70, 85, 90, 40, 60, 80]
}
df = pd.DataFrame(data)

# Step 2: Plot 1 - Study Hours vs Marks
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Study_Hours', y='Marks', hue='Gender', style='Gender', s=100)
plt.title("📚 More Study = Better Marks?")
plt.grid(True)
plt.show()

# Step 3: Plot 2 - Gender-wise average marks
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Gender', y='Marks', ci=None, palette='pastel')
plt.title(" Who Scores Better on Average?")
plt.grid(True)
plt.show()

# Step 4: Plot 3 - Study Hours Distribution
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='Study_Hours', hue='Gender', kde=True, palette='muted')
plt.title(" Study Hour Patterns")
plt.grid(True)
plt.show()
