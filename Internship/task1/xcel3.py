# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv"  # Adjust the path as needed
data = pd.read_csv(file_path)

# Set plot style
sns.set(style="whitegrid")

# 1. Distribution of 'store_size'
plt.figure(figsize=(10, 6))
sns.histplot(data['store_size'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Store Size')
plt.xlabel('Store Size')
plt.ylabel('Frequency')
plt.show()

# 2. Count of stores by 'storetype_id'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='storetype_id', palette='muted')
plt.title('Count of Stores by Store Type')
plt.xlabel('Store Type')
plt.ylabel('Count')
plt.show()

# 3. Average store size by 'city_id'
avg_store_size = data.groupby('city_id')['store_size'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_store_size, x='city_id', y='store_size', palette='coolwarm')
plt.title('Average Store Size by City')
plt.xlabel('City ID')
plt.ylabel('Average Store Size')
plt.xticks(rotation=45)
plt.show()
