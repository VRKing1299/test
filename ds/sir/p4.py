import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import warnings

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate two samples for demonstration
sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)

# Step 2: Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2)

# Set the significance level
alpha = 0.05

# Step 3: Print the results of the t-test
print("Results of Two-Sample T-Test:")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"Degrees of Freedom: {len(sample1) + len(sample2) - 2}")

# Step 4: Plot the distributions of the two samples
plt.figure(figsize=(10, 6))
plt.hist(sample1, alpha=0.5, label='Sample 1', color='blue', bins=10)
plt.hist(sample2, alpha=0.5, label='Sample 2', color='orange', bins=10)
plt.axvline(np.mean(sample1), color='blue', linestyle='dashed', linewidth=2, label='Mean Sample 1')
plt.axvline(np.mean(sample2), color='orange', linestyle='dashed', linewidth=2, label='Mean Sample 2')
plt.title('Distributions of Sample 1 and Sample 2')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Highlight the critical region if null hypothesis is rejected
if p_value < alpha:
    critical_region = np.linspace(min(sample1.min(), sample2.min()), max(sample1.max(), sample2.max()), 1000)
    plt.fill_between(critical_region, 0, 5, color='red', alpha=0.3, label='Critical Region')

plt.text(11, 5, f"T-statistic: {t_stat:.2f}", ha='center', va='center', color='black', backgroundcolor='white')

# Show the plot
plt.legend()
plt.show()

# Step 5: Load dataset and suppress warnings
warnings.filterwarnings('ignore')
df = sb.load_dataset('mpg')

# Step 6: Display dataset summary
print("\nDataset Summary:")
print(df)
print(df['horsepower'].describe())
print(df['model_year'].describe())

# Step 7: Bin numerical columns into categories
bins_horsepower = [0, 75, 150, 240]
labels_horsepower = ['Low', 'Medium', 'High']
df['horsepower_new'] = pd.cut(df['horsepower'], bins=bins_horsepower, labels=labels_horsepower)

bins_year = [69, 72, 74, 84]
labels_year = ['T1', 'T2', 'T3']
df['modelyear_new'] = pd.cut(df['model_year'], bins=bins_year, labels=labels_year)

# Step 8: Create and display the contingency table
df_chi = pd.crosstab(df['horsepower_new'], df['modelyear_new'])
print("\nContingency Table:")
print(df_chi)

# Step 9: Perform the chi-square test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(df_chi)

# Step 10: Print results of the chi-square test
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Step 11: Conclusion based on p-value
if p_value < alpha:
    print("\nResult: Reject the null hypothesis. There is a significant association between horsepower category and model year category.")
else:
    print("\nResult: Fail to reject the null hypothesis. No significant association between horsepower category and model year category.")
