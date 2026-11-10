import pandas as pd

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display basic info
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n")
print(df.isnull().sum())

# Replace blank spaces with NaN
df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

# Fill missing values with median
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Remove duplicates
df = df.drop_duplicates()

# Check cleaned data
print("\nCleaned Dataset Info:\n")
print(df.info())

# Save cleaned dataset
df.to_excel("data/customer_churn_cleaned.xlsx", index=False)

print("\nData cleaning completed successfully!")