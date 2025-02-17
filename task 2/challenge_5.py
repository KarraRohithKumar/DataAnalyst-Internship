# Fix UnicodeEncodeError
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clustered RFM dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\clustered_rfm_dataset.csv"
df = pd.read_csv(file_path)

# Set the Seaborn style
sns.set(style="whitegrid")

# Scatter Plot for Clusters (Recency vs Frequency)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Recency', y='Frequency', hue='Cluster', palette='viridis', s=50)
plt.title('Customer Clusters (Recency vs Frequency)')
plt.xlabel('Recency (Days Since Last Purchase)')
plt.ylabel('Frequency (Total Purchases)')
plt.legend(title="Cluster")
plt.show()

# Pairplot to visualize clusters
sns.pairplot(df, hue="Cluster", palette="husl", diag_kind="kde")
plt.show()

# Heatmap of Feature Importance by Cluster
plt.figure(figsize=(8, 5))
sns.heatmap(df.groupby('Cluster').mean(), cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Feature Importance by Cluster")
plt.show()

print("\n✅ Customer segmentation visualization complete!")
