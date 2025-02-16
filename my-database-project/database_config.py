import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sms_transactions"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None