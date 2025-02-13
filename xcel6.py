# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/karra/Downloads/archive (1)/store_cities.csv"  # Adjust the path as needed
data = pd.read_csv(file_path)

# Simulate a 'year' column for the purpose of this analysis (replace with actual date column if available)
import random
data['year'] = random.choices(range(2015, 2025), k=len(data))  # Replace with actual date/year column if available

# 1. Count of stores added each year
stores_per_year = data['year'].value_counts().sort_index()

# 2. Plot the number of stores added per year
plt.figure(figsize=(12, 6))
sns.lineplot(x=stores_per_year.index, y=stores_per_year.values, marker='o', color='teal')
plt.title('Number of Stores Added Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Stores')
plt.xticks(stores_per_year.index)
plt.grid(True)
plt.show()

# 3. Identify the year with the highest store growth
max_growth_year = stores_per_year.idxmax()
print(f"The year with the highest store growth is {max_growth_year}, with {stores_per_year[max_growth_year]} stores added.")
