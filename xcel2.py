# Import required libraries
import pandas as pd

# Load the dataset
file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv"  # Adjust the path as needed
data = pd.read_csv(file_path)

# Descriptive Statistics for 'store_size'
print("Descriptive Statistics for 'store_size':\n")
print(f"Mean: {data['store_size'].mean()}")
print(f"Median: {data['store_size'].median()}")
print(f"Mode: {data['store_size'].mode()[0]}")
print(f"Standard Deviation: {data['store_size'].std()}")

# Count unique values for categorical columns
print("\nUnique Value Counts:")
for col in ['store_id', 'storetype_id', 'city_id']:
    print(f"{col}: {data[col].nunique()} unique values")

# Summary Statistics for the entire dataset
print("\nSummary Statistics:\n", data.describe())
