# Principal Component Analysis (PCA)
#  Perform PCA on a dataset to reduce dimensionality.
#  Evaluate the explained variance and select the appropriate number of principal components.
#  Visualize the data in the reduced-dimensional space.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Sample Data
df = pd.DataFrame({
    'Marks': [45, 55, 65, 75, 85, 95, 40, 60, 70, 90],
    'Attendance': [60, 65, 70, 80, 85, 95, 55, 75, 78, 93],
    'Study_Hours': [2, 3, 3.5, 4, 5, 6, 1.5, 3.8, 4.5, 5.5]
})

# 2. Standardize
scaled = StandardScaler().fit_transform(df)

# 3. Apply PCA (2 components)
pca = PCA(n_components=2)
reduced = pca.fit_transform(scaled)

# 4. Explained Variance
print("Explained Variance:", pca.explained_variance_ratio_)

# 5. Plot
plt.scatter(reduced[:, 0], reduced[:, 1], color='orchid', s=100)
plt.title("PCA Result (2D View)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()

