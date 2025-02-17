# Fix UnicodeEncodeError
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Import required libraries
import pandas as pd

# Load the cleaned dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\cleaned_marketing_campaign.csv"
df = pd.read_csv(file_path)

# Compute summary statistics
print("\n📊 Descriptive Statistics:")
print(df.describe())

# Create a new feature: Total Purchases
df['Total_Purchases'] = df['NumDealsPurchases'] + df['NumWebPurchases'] + df['NumCatalogPurchases'] + df['NumStorePurchases']

# Create a Recency metric (convert 'Dt_Customer' to days since the most recent signup)
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
df['Recency'] = (df['Dt_Customer'].max() - df['Dt_Customer']).dt.days

# Compute Recency, Frequency, and Monetary (RFM) metrics
rfm = df.groupby('ID').agg({
    'Recency': 'min',  # Most recent signup
    'Total_Purchases': 'sum',  # Total number of purchases
    'Total_Spent': 'sum'  # Total amount spent
}).reset_index()

# Rename columns for clarity
rfm.columns = ['Customer_ID', 'Recency', 'Frequency', 'Monetary']

# Display the RFM dataset
print("\n🛍️ RFM Table Sample:")
print(rfm.head())

# Save the RFM dataset
rfm.to_csv(r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\rfm_dataset.csv", index=False)

print("\n✅ Feature engineering complete! RFM dataset saved.")
