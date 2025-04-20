import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Creating a sample dataset
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Preferred_Subject': ['Math', 'English', 'Science', 'Math', 'English', 'Science', 'Math', 'English', 'Science', 'Math']
}

df = pd.DataFrame(data)

# Creating a contingency table
contingency_table = pd.crosstab(df['Gender'], df['Preferred_Subject'])

# Display the contingency table
print("Contingency Table:")
print(contingency_table)

# Hypotheses:
# H₀: Gender and preferred subject are independent
# H₁: Gender and preferred subject are NOT independent

# Performing chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\nChi-square Test Result:")
print(f"Chi-square Statistic: {chi2}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)
print(f"P-value: {p}")

# Interpret the result
alpha = 0.05
if p < alpha:
    print("\nConclusion: Reject the null hypothesis. There is a significant association between gender and preferred subject.")
else:
    print("\nConclusion: Fail to reject the null hypothesis. No significant association between gender and preferred subject.")

# ✅ Visualization: Bar chart of preferences by gender
contingency_table.plot(kind='bar', stacked=True)
plt.title("Preferred Subject by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Subject")
plt.tight_layout()
plt.show()
