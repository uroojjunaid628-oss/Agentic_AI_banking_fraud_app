import psycopg2
from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

def get_db_connection():
    """Create and return a postgreSQL database connection
    """
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
    return connection

def test_connection():
    """
    Test the PostgreSQL database connection.
    """
    try:
        connection = get_db_connection()

        print(" Successfully connected to PostgreSQL database.")

        connection.close()

        print(" Database connection closed.")

    except Exception as error:
        print(f"Database connection failed.\n{error}")

if __name__ == "__main__":
    test_connection()     

