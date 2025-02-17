# Fix UnicodeEncodeError
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
file_path = r"C:\Users\karra\OneDrive\Desktop\Internship\task 2\cleaned_marketing_campaign.csv"
df = pd.read_csv(file_path)

# Print column names to check if required features exist
print("Columns in dataset:", df.columns)

# Recreate 'Total_Purchases' if it's missing
if 'Total_Purchases' not in df.columns:
    df['Total_Purchases'] = (
        df.get('NumDealsPurchases', 0) + df.get('NumWebPurchases', 0) +
        df.get('NumCatalogPurchases', 0) + df.get('NumStorePurchases', 0)
    )

# Define features and target
features = ['Income', 'Recency', 'Total_Purchases', 'MntWines', 'MntMeatPro
