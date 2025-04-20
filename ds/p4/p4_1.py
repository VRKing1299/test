import pandas as pd
from scipy.stats import ttest_ind

# Sample Data
data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [70, 65, 75, 60, 80, 68]
}

df = pd.DataFrame(data)

# Split data by gender
male_marks = df[df['Gender'] == 'Male']['Marks']
female_marks = df[df['Gender'] == 'Female']['Marks']

# Hypothesis:
# H₀: There is no significant difference in average marks between males and females.
# H₁: There is a significant difference.

t_stat, p_value = ttest_ind(male_marks, female_marks)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print(" Reject H₀: There IS a significant difference.")
else:
    print(" Fail to reject H₀: There is NO significant difference.")
