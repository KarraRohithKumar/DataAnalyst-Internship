# Import required libraries
import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\marketing_campaign.csv"
df = pd.read_csv(file_path, sep='\t')

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Drop duplicate rows if any
df = df.drop_duplicates()

# Convert 'Dt_Customer' to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# Fill missing Income values with the median
df['Income'].fillna(df['Income'].median(), inplace=True)

# Create a new column for Total Spending
df['Total_Spent'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

# Define a function to remove outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from 'Income' and 'Total_Spent'
df = remove_outliers(df, 'Income')
df = remove_outliers(df, 'Total_Spent')

# Display dataset info after cleaning
print("\nDataset Info After Cleaning:")
df.info()

# Display summary statistics
print("\nSummary Statistics After Outlier Removal:")
print(df[['Income', 'Total_Spent']].describe())

# Save the cleaned dataset
df.to_csv(r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\cleaned_marketing_campaign.csv", index=False)

print("\n✅ Data cleaning complete! Outliers removed, missing values handled, and dataset saved.")
