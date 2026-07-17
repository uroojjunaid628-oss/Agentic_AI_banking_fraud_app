import pandas as pd
from database.connection import get_db_connection

DATASET_PATH = "datasets/banking_fraud_detection_clean.csv"

def import_dataset():
    """
    Import the cleaned dataset into the PostgreSQL transactions table.
    """
    df = pd.read_csv(DATASET_PATH)
    print("Total Rows:", len(df))
    print("Duplicate Transaction IDs:", df["transaction_id"].duplicated().sum())

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()


        insert_query = """
        INSERT INTO transactions (
            transaction_id,
            customer_id,
            transaction_amount_million,
            transaction_time,
            transaction_date,
            transaction_type,
            merchant_id,
            merchant_category,
            transaction_location,
            customer_home_location,
            distance_from_home,
            device_id,
            ip_address,
            card_type,
            account_balance_million,
            daily_transaction_count,
            weekly_transaction_count,
            avg_transaction_amount_million,
            max_transaction_last_24h_million,
            is_international_transaction,
            is_new_merchant,
            failed_transaction_count,
            unusual_time_transaction,
            previous_fraud_count,
            fraud_label
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        );
        """

        for index, row in enumerate(df.itertuples(index=False), start=1):
            try:
               cursor.execute(insert_query, tuple(row))
            except Exception as error:
               print(f"Error on row {index}: {error}")
               raise
        
        connection.commit()   
        print(f"Successfully imported {len(df)} records.") 

    except Exception as error:
        print(f"Import failed:\n{error}")


        if connection:
            connection.rollback()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    import_dataset()
