import mysql.connector
from database_config import get_db_connection

def insert_transaction(transacntion_type, sender, receiver, amount, currency, transaction_date, message):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO transactions (transaction_type, sender, receiver, amount, currency, transaction_date, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (transacntion_type, sender, receiver, amount, currency, transaction_date, message)
            cursor.execute(query, values)
            conn.commit()
            print(f"Inserted: {transacntion_type} - {amount} RWF")
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()