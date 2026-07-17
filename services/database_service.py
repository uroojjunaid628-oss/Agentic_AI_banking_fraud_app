from database.connection import get_db_connection
from psycopg2.extras import RealDictCursor


def get_transaction_by_id(transaction_id):
    """
    Retrieve a single transaction using its transaction_id.
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
        SELECT *
        FROM transactions
        WHERE transaction_id = %s;
        """

        cursor.execute(query, (transaction_id,))
        return cursor.fetchone()

    except Exception as error:
        print(f"Database Error:\n{error}")
        return None

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_customer_transactions(customer_id):
    """
    Retrieve all transactions belonging to a customer.
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
        SELECT *
        FROM transactions
        WHERE customer_id = %s;
        """

        cursor.execute(query, (customer_id,))

        return cursor.fetchall()

    except Exception as error:
        print(f"Database Error:\n{error}")
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
def get_fraud_transactions():
    """
    Retrieve all fraudulent transactions.
    """

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
        SELECT *
        FROM transactions
        WHERE fraud_label = 'Fraud';
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as error:
        print(f"Database Error:\n{error}")
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

def main():

    customer_transactions = get_customer_transactions(32056)

    print(customer_transactions)


if __name__ == "__main__":
    main()