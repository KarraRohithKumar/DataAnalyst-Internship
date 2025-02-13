# Import required libraries
import pandas as pd

# Load the dataset
file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv"  # Adjust the path as needed
data = pd.read_csv(file_path)

# Analysis Summary
avg_store_size_by_city = data.groupby('city_id')['store_size'].mean().reset_index()
city_store_count = data['city_id'].value_counts().reset_index()
city_store_count.columns = ['city_id', 'store_count']
most_common_storetype = data['storetype_id'].mode()[0]

# Generate Recommendations
print("### Recommendations Based on EDA ###\n")

# 1. City Expansion Strategy
largest_avg_city = avg_store_size_by_city.loc[avg_store_size_by_city['store_size'].idxmax()]
print(f"1. Focus on expanding operations in city '{largest_avg_city['city_id']}' as it has the largest average store size ({largest_avg_city['store_size']} units), indicating a higher capacity for retail business.")

smallest_avg_city = avg_store_size_by_city.loc[avg_store_size_by_city['store_size'].idxmin()]
print(f"2. Investigate city '{smallest_avg_city['city_id']}' with the smallest average store size ({smallest_avg_city['store_size']} units) for potential growth opportunities.")

# 2. Store Type Strategy
print(f"3. The most common store type is '{most_common_storetype}'. Consider diversifying the store types to capture different market segments.")

# 3. Store Distribution
print("4. Focus on cities with a low store count to improve market presence and capture untapped potential.")
print("\nTop cities with the lowest number of stores:")
print(city_store_count.tail(5))
