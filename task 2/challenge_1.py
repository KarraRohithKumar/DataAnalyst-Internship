# Import required libraries
import pandas as pd

# Load the dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\marketing_campaign.csv"

df = pd.read_csv(file_path, sep='\t')

# Convert 'Dt_Customer' to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# Handle missing values in 'Income' by filling with the median
df['Income'].fillna(df['Income'].median(), inplace=True)

# Standardizing 'Marital_Status' values
df['Marital_Status'] = df['Marital_Status'].replace({
    'Single': 'Single', 'Married': 'Married', 'Together': 'Married',
    'Divorced': 'Divorced', 'Widow': 'Widowed', 'Alone': 'Single',
    'Absurd': 'Single', 'YOLO': 'Single'
})

# Display dataset info after cleaning
df.info()
print(df.head())  # Check first few rows to verify changes
