from database.connection import get_db_connection


def create_transactions_table():
    """
    Create the transactions table if it does not already exist.
    """

    create_table_query = """
    CREATE TABLE IF NOT EXISTS transactions (

        id SERIAL PRIMARY KEY,

        transaction_id BIGINT,
        customer_id BIGINT,
        transaction_amount_million DECIMAL,
        transaction_time TIME,
        transaction_date DATE,
        transaction_type VARCHAR(50),
        merchant_id BIGINT,
        merchant_category VARCHAR(100),
        transaction_location VARCHAR(100),
        customer_home_location VARCHAR(100),
        distance_from_home DECIMAL,
        device_id BIGINT,
        ip_address VARCHAR(50),
        card_type VARCHAR(50),
        account_balance_million DECIMAL,
        daily_transaction_count INTEGER,
        weekly_transaction_count INTEGER,
        avg_transaction_amount_million DECIMAL,
        max_transaction_last_24h_million DECIMAL,
        is_international_transaction VARCHAR(10),
        is_new_merchant VARCHAR(10),
        failed_transaction_count INTEGER,
        unusual_time_transaction VARCHAR(10),
        previous_fraud_count INTEGER,
        fraud_label VARCHAR(20)

    );
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(create_table_query)
        connection.commit()

        print("Transactions table created successfully.")

    except Exception as error:
        print(f"Error creating table:\n{error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    create_transactions_table()