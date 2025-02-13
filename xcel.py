# Import required libraries
import pandas as pd
import numpy as np

# Load the dataset
file_path = file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv" # Update with the correct path if needed
data = pd.read_csv(file_path)

# Check for missing values
print("Missing Values:\n", data.isnull().sum())

# Check data types
print("\nData Types:\n", data.dtypes)

# Remove duplicate rows (if any)
data_cleaned = data.drop_duplicates()
print(f"\nNumber of duplicates removed: {len(data) - len(data_cleaned)}")

# Check unique values in each column
print("\nUnique values in each column:")
for col in data_cleaned.columns:
    print(f"{col}: {data_cleaned[col].nunique()} unique values")

# Save the cleaned data (optional)
data_cleaned.to_csv("store_cities_cleaned.csv", index=False)
print("\nCleaned data saved as 'store_cities_cleaned.csv'")
