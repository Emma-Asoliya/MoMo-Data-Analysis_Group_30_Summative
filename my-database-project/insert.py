#!/usr/bin/env python3

import mysql.connector
from database_config import get_db_connection

def insert_transaction(
        transaction_type: Any,
        sender: Any, 
        receiver, 
        amount, 
        currency, 
        transaction_date, 
        message
        ):
    conn = get_db_connection()
    if conn is None:
        print("Error connecting to database")
        return
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO transactions (transaction_type, sender, receiver, amount, currency, transaction_date, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (transaction_type, sender, receiver, amount, currency, transaction_date, message)
        cursor.execute(query, values)
        conn.commit()
        print(f"Inserted: {transaction_type} - {amount} RWF")
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
