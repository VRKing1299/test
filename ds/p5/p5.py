# ANOVA (Analysis of Variance)
#  Perform one-way ANOVA to compare means across multiple groups.
#  Conduct post-hoc tests to identify significant differences between group means
import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Sample data: 3 different classes with marks
data = {
    'Class': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Marks': [85, 88, 90, 78, 80, 79, 92, 95, 94]
}

df = pd.DataFrame(data)

# Split the marks into groups
group_A = df[df['Class'] == 'A']['Marks']
group_B = df[df['Class'] == 'B']['Marks']
group_C = df[df['Class'] == 'C']['Marks']

# Perform One-Way ANOVA
f_stat, p_value = f_oneway(group_A, group_B, group_C)

print("F-statistic:", f_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("❌ Reject H₀: At least one class has a different average.")

    # Perform Tukey's HSD post-hoc test
    posthoc = pairwise_tukeyhsd(df['Marks'], df['Class'], alpha=0.05)
    print(posthoc)
else:
    print("✅ Fail to reject H₀: No significant difference among the classes.")
