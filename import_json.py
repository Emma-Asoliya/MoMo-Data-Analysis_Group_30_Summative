import json
import mysql.connector
import uuid
import os


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="EmmaBriggs1#",
    database="momo_data_analysis"
)
cursor = conn.cursor()


TRANSACTION_TYPE_MAPPING = {
    "airtime": "Airtime Purchases",
    "deposit": "Bank Deposits",
    "cash power": "Cash Power Purchases",
    "received": "Incoming Money",
    "bundle": "Internet and Voice Bundles",
    "payment": "Payments to Code Holders",
    "transfer": "Transfers to Mobile Numbers",
    "withdraw": "Withdrawals from Agents",
    "unrecognised": "Third Party Transactions"
}


DATA_DIR = "Categorised_Data/Cleaned_Data/"


def insert_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for entry in data:
        raw_transaction_type = entry.get("transaction_type", "Unrecognised").lower()
        transaction_type = TRANSACTION_TYPE_MAPPING.get(raw_transaction_type, "Third Party Transactions")


        transaction_date = entry.get("Date", "2000-01-01")
        transaction_time = entry.get("Time", "00:00:00")

        print(f"🔍 Mapping '{raw_transaction_type}' to '{transaction_type}' from {file_path}")
        print(f"📅 Date: {transaction_date}, ⏰ Time: {transaction_time}")

        query = """
        INSERT INTO transactions (transaction_id, transaction_type, transaction_date, transaction_time, amount, currency, fee, code, sender, receiver, phone_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            str(uuid.uuid4()),
            transaction_type,
            transaction_date,
            transaction_time,
            float(entry.get("amount", 0)),
            entry.get("currency", "RWF"),
            float(entry.get("fee", 0)),
            entry.get("code", None),
            entry.get("sender", None),
            entry.get("receiver", None),
            entry.get("phone_number", None)
        )

        cursor.execute(query, values)

    conn.commit()
    print(f"✅ Inserted {len(data)} records from {file_path}")


for filename in os.listdir(DATA_DIR):
    if filename.endswith(".json"):
        file_path = os.path.join(DATA_DIR, filename)
        insert_data_from_json(file_path)


cursor.close()
conn.close()
