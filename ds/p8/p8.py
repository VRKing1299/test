# K-Means Clustering
#  Apply the K-Means algorithm to group similar data points into clusters.
#  Determine the optimal number of clusters using elbow method or silhouette analysis.
#  Visualize the clustering results and analyze the cluster characteristics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Sample Data
df = pd.DataFrame({
    'Income': [15, 16, 15.5, 17, 80, 85, 82, 88, 55, 53, 58, 60],
    'Spending': [40, 42, 38, 45, 90, 85, 87, 88, 60, 62, 63, 65]
})

# 2. Standardize the Data
scaled = StandardScaler().fit_transform(df)

# 3. Elbow & Silhouette Method
for k in range(2, 6):
    model = KMeans(n_clusters=k, random_state=0)
    labels = model.fit_predict(scaled)
    print(f"k={k} → Silhouette Score: {silhouette_score(scaled, labels):.2f}")

# 4. Apply K-Means (Best k=3)
model = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = model.fit_predict(scaled)
print(df)

# 5. Plot the Clusters
colors = ['red', 'green', 'blue']
for i in range(3):
    plt.scatter(df[df['Cluster']==i]['Income'], df[df['Cluster']==i]['Spending'], 
                color=colors[i], label=f'Cluster {i}')
plt.title("K-Means Clusters")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.legend()
plt.grid(True)
plt.show()
