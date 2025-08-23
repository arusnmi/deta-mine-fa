import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
from kneed import KneeLocator

# Read the CSV file
df = pd.read_csv('matched_records_filtered_with_time.csv')  

df = df.fillna(0)  # Handle missing values by filling with 0
# Select features for clustering
features = ['price', 'surge_multiplier', 'distance', 'time_decimal']  # Added distance
X = df[features].copy()

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters using elbow method
inertias = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Automatically determine optimal k using kneed
kn = KneeLocator(list(K), inertias, curve='convex', direction='decreasing')
optimal_k = kn.elbow
print(f"Optimal number of clusters determined by elbow method: {optimal_k}")

# Perform K-means clustering with optimal k
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Create 3D visualization
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot points
scatter = ax.scatter(df['price'], 
                    df['distance'], 
                    df['time_decimal'],
                    c=df['Cluster'], 
                    cmap='viridis')

ax.set_xlabel('Price')
ax.set_ylabel('Distance')
ax.set_zlabel('Time (Decimal Hours)')
plt.colorbar(scatter)
plt.title('K-means Clustering Results')
plt.show()

# Print cluster statistics
print("\nCluster Statistics:")
for cluster in range(optimal_k):  # Changed n_clusters to optimal_k
    cluster_data = df[df['Cluster'] == cluster]
    print(f"\nCluster {cluster}:")
    print(f"Number of points: {len(cluster_data)}")
    print(f"Average price: ${cluster_data['price'].mean():.2f}")
    print(f"Average distance: {cluster_data['distance'].mean():.2f}")
    print(f"Average time (decimal hours): {cluster_data['time_decimal'].mean():.2f}")
