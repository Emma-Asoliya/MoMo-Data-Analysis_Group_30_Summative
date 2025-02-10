import xml.etree.ElementTree as ET
import os
import json
import re

# Directory for the cleaned data to be stored
cleaned_data_dir = os.path.join('Cleaned_Data')
os.makedirs(cleaned_data_dir, exist_ok=True)

# Regex pattern for different transaction features
def fetch_data(body_text, filename):
    data = {}
    date = re.compile(r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})')
    transaction_id_number = re.compile(r'(TxId|Financial Transaction Id|Transaction Id)[:\s]+(\w+)', re.IGNORECASE)
    amount_of_money = re.compile(r'\b(\d+(?:,\d{3})?(?:\.\d{2})?)\s(RWF)\b')
    account_balance = re.compile(r'New\s+balance\s*:\s*([\d,]+)\s*RWF|Your\s+new\s+balance\s*:\s*([\d,]+)\s*RWF', re.IGNORECASE)
    fee_charges = re.compile(r'\bfee\b.?(\d+(?:,\d{3})?(?:\.\d{2})?)', re.IGNORECASE)

    # Regex patterns for different transaction categories
    incoming_money_sender = re.compile(r'received\s+\d+\s+RWF\s+from\s+([\w\s]+?)\s+\(\*+\d+\)', re.IGNORECASE)
    transfer_to_number_receiver = re.compile(r'transferred to\s+([\w\s]+?)\s+\((\d+)\)|to\s+([\w\s]+?)\s+with token', re.IGNORECASE)
    payment_to_code_receiver = re.compile(r'to\s+([\w\s\w\s]+?)\s+(\d+)')
    third_party_transactions_sender = re.compile(r'by\s+([\w\s]+?)\s+on your MOMO account', re.IGNORECASE)
    withdraw_from_agents = re.compile(r'Agent:\s+([\w\s]+)', re.IGNORECASE)
    transaction_category = re.compile(r'\b(received|payment|transfer|withdraw|deposit|purchase|airtime|bundle|cash power)\b', re.IGNORECASE)

    # Extracting date and time
    date_match = date.search(body_text)
    data['Date'] = date_match.group(1) if date_match else 'Unrecognised'
    data['Time'] = date_match.group(2) if date_match else 'Unrecognised'

    # Extracting transaction amount and currency
    amount_match = amount_of_money.search(body_text)
    if amount_match:
        data['amount'] = int(amount_match.group(1).replace(',', ''))
        data['currency'] = amount_match.group(2)
    else:
        data['amount'] = 0
        data['currency'] = 'Unrecognised'

    # fee
    fee_match = fee_charges.search(body_text)
    data['fee'] = int(fee_match.group(1).replace(',', '')) if fee_match else 0

    # transaction category
    transaction_type_match = transaction_category.search(body_text)
    if transaction_type_match:
        data['transaction_type'] = transaction_type_match.group().lower()
    else:
        if 'received' in body_text.lower():
            data['transaction_type'] = 'received'
        elif 'payment' in body_text.lower():
            data['transaction_type'] = 'payment'
        elif 'withdraw' in body_text.lower():
            data['transaction_type'] = 'withdraw'
        elif 'deposit' in body_text.lower():
            data['transaction_type'] = 'deposit'
        elif 'transfer' in body_text.lower():
            data['transaction_type'] = 'transfer'
        elif 'airtime' in body_text.lower():
            data['transaction_type'] = 'airtime purchase'
        elif 'bundle' in body_text.lower():
            data['transaction_type'] = 'bundle purchase'
        elif 'cash power' in body_text.lower():
            data['transaction_type'] = 'cash power purchase'
        else:
            data['transaction_type'] = 'Unrecognised'

    # sender/receiver based off categories
    if filename == 'incoming_money.xml':
        sender_match = incoming_money_sender.search(body_text)
        data['sender'] = sender_match.group(1) if sender_match else 'Unrecognised'

    elif filename == 'transfer_to_number.xml':
        receiver_match = transfer_to_number_receiver.search(body_text)
        if receiver_match:
            data['receiver'] = receiver_match.group(1) or receiver_match.group(3)
            data['phone_number'] = '+' + receiver_match.group(2) if receiver_match.group(2) else 'Unrecognised'
        else:
            data['receiver'] = 'Unrecognised'
            data['phone_number'] = 'Unrecognised'

    elif filename == 'payment_to_code.xml':
        receiver_match = payment_to_code_receiver.search(body_text)
        data['receiver'] = receiver_match.group(1) if receiver_match else 'Unrecognised'
        data['code'] = int(receiver_match.group(2)) if receiver_match else 0

    elif filename == 'third_party.xml':
        third_party_sender_match = third_party_transactions_sender.search(body_text)
        data['third_party_sender'] = third_party_sender_match.group(1) if third_party_sender_match else 'Unrecognised'

    elif filename == 'withdraw_from_agents.xml':
        agent_match = withdraw_from_agents.search(body_text)
        data['agent'] = agent_match.group(1) if agent_match else 'Unrecognised'

    return data

# Function to clean file and extract transactions
def clean_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    wrapped_content = f"<root>{content}</root>"

    try:
        tree = ET.ElementTree(ET.fromstring(wrapped_content))
        root = tree.getroot()
    except ET.ParseError:
        print(f"Error parsing XML in {input_filename}")
        return

    cleaned_data = []

    for element in root:
        if 'body' in element.attrib:
            body_text = element.attrib['body']
            extracted_data = fetch_data(body_text, os.path.basename(input_filename))
            if extracted_data:
                cleaned_data.append(extracted_data)

    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

import os

# Define base directory for categorized files
base_dir = os.path.abspath(r"C:\Users\lilal\Intranet\MoMo-Data-Analysis_Group_30_Summative\Categorised_Data")


# List of categorized files to process
categorized_files = [
    "Airtime_purchases.xml",
    "bank_deposits.xml",
    "cash_power_purchases.xml",
    "incoming_money.xml",
    "internet_and_voice_bundles.xml",
    "payment_to_code.xml",
    "third_party_transactions.xml",
    "transfer_to_number.xml",
    "withdrawals_from_agents.xml"
]

# Ensure Cleaned_Data directory exists
cleaned_data_dir = os.path.join(base_dir, "Cleaned_Data")
os.makedirs(cleaned_data_dir, exist_ok=True)

for filename in categorized_files:
    input_path = os.path.join(base_dir, filename)  # Use absolute path
    output_path = os.path.join(cleaned_data_dir, f'cleaned_{filename.replace(".xml", ".json")}')

    if os.path.exists(input_path):  # Check if the file exists before processing
        clean_file(input_path, output_path)
    else:
        print(f"File {input_path} not found. Skipping...")

print("Data cleaning process done")