# Import required libraries
import pandas as pd

# Load the dataset
file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv"  # Adjust the path as needed
data = pd.read_csv(file_path)

# 1. City with the largest and smallest average store size
avg_store_size_by_city = data.groupby('city_id')['store_size'].mean().reset_index()
largest_avg_city = avg_store_size_by_city.loc[avg_store_size_by_city['store_size'].idxmax()]
smallest_avg_city = avg_store_size_by_city.loc[avg_store_size_by_city['store_size'].idxmin()]

print("City with the largest average store size:")
print(largest_avg_city)

print("\nCity with the smallest average store size:")
print(smallest_avg_city)

# 2. Most common store type
most_common_storetype = data['storetype_id'].mode()[0]
print(f"\nMost common store type: {most_common_storetype}")

# 3. Ranking cities by the number of stores
city_store_count = data['city_id'].value_counts().reset_index()
city_store_count.columns = ['city_id', 'store_count']
print("\nCities ranked by the number of stores:")
print(city_store_count)
