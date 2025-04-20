import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Sample data (three groups)
group1 = [23, 20, 25, 22, 21]
group2 = [27, 30, 29, 31, 28]
group3 = [35, 37, 36, 34, 38]

# Step 1: Combine data into a pandas DataFrame
data = group1 + group2 + group3
groups = ['A'] * len(group1) + ['B'] * len(group2) + ['C'] * len(group3)

df = pd.DataFrame({'score': data, 'group': groups})

# Display the DataFrame for verification
print("Dataset:\n", df)

# Step 2: Perform one-way ANOVA
model = ols('score ~ C(group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the results of ANOVA
print("\nANOVA Results:\n", anova_table)

# Step 3: Perform Tukey's HSD test for post-hoc analysis
tukey_result = pairwise_tukeyhsd(df['score'], df['group'], alpha=0.05)

# Print Tukey's HSD test results
print("\nTukey's HSD Test Results:\n", tukey_result)
