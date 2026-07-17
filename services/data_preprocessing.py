import pandas as pd
from pathlib import Path

# File Paths
DATASET_PATH = Path("datasets") / "fraud_investigation_transactions.csv"
OUTPUT_PATH = Path("datasets") / "banking_fraud_detection_clean.csv"


# Column Mapping
COLUMN_MAPPING = {
    "Transaction_ID": "transaction_id",
    "Customer_ID": "customer_id",
    "Transaction_Amount (in Million)": "transaction_amount_million",
    "Transaction_Time": "transaction_time",
    "Transaction_Date": "transaction_date",
    "Transaction_Type": "transaction_type",
    "Merchant_ID": "merchant_id",
    "Merchant_Category": "merchant_category",
    "Transaction_Location": "transaction_location",
    "Customer_Home_Location": "customer_home_location",
    "Distance_From_Home": "distance_from_home",
    "Device_ID": "device_id",
    "IP_Address": "ip_address",
    "Card_Type": "card_type",
    "Account_Balance (in Million)": "account_balance_million",
    "Daily_Transaction_Count": "daily_transaction_count",
    "Weekly_Transaction_Count": "weekly_transaction_count",
    "Avg_Transaction_Amount (in Million)": "avg_transaction_amount_million",
    "Max_Transaction_Last_24h (in Million)": "max_transaction_last_24h_million",
    "Is_International_Transaction": "is_international_transaction",
    "Is_New_Merchant": "is_new_merchant",
    "Failed_Transaction_Count": "failed_transaction_count",
    "Unusual_Time_Transaction": "unusual_time_transaction",
    "Previous_Fraud_Count": "previous_fraud_count",
    "Fraud_Label": "fraud_label"
}



# Load Dataset
def load_dataset():
    """
    Load the raw banking fraud dataset.
    """
    return pd.read_csv(DATASET_PATH)



# Rename Columns
def rename_columns(df):
    """
    Rename dataset columns using a standard naming convention.
    """
    return df.rename(columns=COLUMN_MAPPING)



# Remove Missing Values
def remove_missing_values(df):
    """
    Remove rows containing missing values.
    """
    rows_before = len(df)

    df = df.dropna()

    rows_after = len(df)

    print(f"\nRemoved {rows_before - rows_after} rows containing missing values.")

    return df



# Convert Data Types
def convert_data_types(df):
    """
    Convert columns to appropriate data types.
    """

    # Convert IDs back to integers
    integer_columns = [
        "transaction_id",
        "customer_id",
        "merchant_id",
        "device_id",
        "daily_transaction_count",
        "weekly_transaction_count",
        "failed_transaction_count",
        "previous_fraud_count",
    ]

    for column in integer_columns:
        df[column] = df[column].astype(int)

    # Convert date column
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    return df



# Save Clean Dataset
def save_clean_dataset(df):
    """
    Save the cleaned dataset.
    """
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nCleaned dataset saved to:\n{OUTPUT_PATH}")

# Main Pipeline
def main():

   
    print("BANKING FRAUD DATA PREPROCESSING")
  

    df = load_dataset()

    print(f"\nOriginal Shape: {df.shape}")

    df = rename_columns(df)

    df = remove_missing_values(df)

    df = convert_data_types(df)

    save_clean_dataset(df)

    print(f"\nFinal Shape: {df.shape}")

    print("\nData preprocessing completed successfully.")


if __name__ == "__main__":
    main()

