# Hypothesis Testing
#  Formulate null and alternative hypotheses for a given problem.
#  Conduct a hypothesis test using appropriate statistical tests (e.g., t-test, chisquare test).
#  Interpret the results and draw conclusions based on the test outcomes.
import pandas as pd
from scipy.stats import chi2_contingency

# Sample Data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Preferred_Subject': ['Math', 'Math', 'Science', 'Math', 'Science', 'Science']
}

df = pd.DataFrame(data)

# Create contingency table
contingency_table = pd.crosstab(df['Gender'], df['Preferred_Subject'])
print (contingency_table)

# Hypothesis:
# H₀: Gender and subject preference are independent.
# H₁: Gender and subject preference are NOT independent.

chi2, p, dof, expected = chi2_contingency(contingency_table)

print("Chi-square value:", chi2)
print("P-value:", p)
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

if p < 0.05:
    print(" Reject H₀: Gender and subject preference are related.")
else:
    print(" Fail to reject H₀: Gender and preference are independent.")
