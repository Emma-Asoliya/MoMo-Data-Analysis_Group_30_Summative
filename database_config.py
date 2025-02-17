from flask import Flask, jsonify, request
import mysql.connector
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="EmmaBriggs1#",
        database="momo_data_analysis"
    )


@app.route("/transactions", methods=["GET"])
def get_transactions():
    category = request.args.get("category", None)
    start_date = request.args.get("start_date", None)
    end_date = request.args.get("end_date", None)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)


    query = "SELECT * FROM transactions WHERE 1=1"
    values = []


    if category:
        query += " AND transaction_type = %s"
        values.append(category)


    if start_date:
        query += " AND transaction_date >= %s"
        values.append(start_date)
    if end_date:
        query += " AND transaction_date <= %s"
        values.append(end_date)

    cursor.execute(query, values)
    transactions = cursor.fetchall()

   
    for transaction in transactions:
        for key, value in transaction.items():
            if isinstance(value, timedelta):
                transaction[key] = value.total_seconds()
            elif hasattr(value, "isoformat"):
                transaction[key] = value.isoformat()

    cursor.close()
    conn.close()

    return jsonify(transactions)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
