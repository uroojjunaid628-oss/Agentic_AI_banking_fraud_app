import pandas as pd
from pathlib import Path

# Dataset path
DATASET_PATH = Path("datasets") / "fraud_investigation_transactions.csv"
 
def analyse_dataset():
    df = pd.read_csv(DATASET_PATH)
    print("BANKING FRAUD DETECTION DATASET ANALYSIS")
    print(f"\nTotal Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


if __name__ == "__main__":
    analyse_dataset()
