# Fix UnicodeEncodeError
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore

# Load the RFM dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\rfm_dataset.csv"
df = pd.read_csv(file_path)

# Scale the data for clustering
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['Recency', 'Frequency', 'Monetary']])

# Find the optimal number of clusters using the Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o', linestyle='-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()

# Choose the optimal number of clusters (based on the elbow point)
optimal_k = 4  # Adjust based on the elbow method result

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Display cluster distribution
print("\n📊 Cluster Distribution:")
print(df['Cluster'].value_counts())

# Save the clustered dataset
df.to_csv(r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\clustered_rfm_dataset.csv", index=False)

print("\n✅ Customer segmentation complete! Clustered dataset saved.")
