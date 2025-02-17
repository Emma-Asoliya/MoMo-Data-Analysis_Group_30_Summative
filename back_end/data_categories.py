import xml.etree.ElementTree as ET
import os

# Create the directory for the categorized data files if it doesn't exist
os.makedirs('Categorised_Data', exist_ok=True)

# Parse the XML file
tree = ET.parse(r'C:\Users\lilal\Intranet\summative_momo\back_end\modified_sms_v2.xml')
root = tree.getroot()

# Dictionaries for categorizing data or maybe lists would be better
categories = {
    'incoming_money': [],
    'payment_to_code': [],
    'transfer_to_number': [],
    'withdrawals_from_agents': [],
    'bank_deposits': [],
    'third_party_transactions': [],
    'Airtime_purchases': [],
    'Internet_and_voice_bundles': [],
    'cash_power_purchases': [],
    'miscellaneous_messages': []
}

# Helper function to add categorized data to the appropriate list
def categorize_message(body_text, message_xml):
    # For Incoming Money
    if 'received' in body_text:
        categories['incoming_money'].append(message_xml)

    # For Trnasfers to Phone Numbers
    elif 'transfer' in body_text and 'fee was:' in body_text:
        categories['transfer_to_number'].append(message_xml)

    # 3️⃣  Transactions have the Keyword as payment but dont include failed payments 
    elif 'payment' in body_text and 'failed' not in body_text:
        if 'mtn cash power' in body_text:
            categories['cash_power_purchases'].append(message_xml)  r
        elif 'airtime' in body_text:
            categories['Airtime_purchases'].append(message_xml)
        elif 'bundles and packs' in body_text:
            categories['Internet_and_voice_bundles'].append(message_xml)
        elif 'fee was 0 rwf.' in body_text:
            categories['payment_to_code'].append(message_xml)

    # Bank deposits
    elif 'bank deposit' in body_text:
        categories['bank_deposits'].append(message_xml)

    # Withdrawals from agents
    elif 'withdraw' in body_text:
        categories['withdrawals_from_agents'].append(message_xml)

    # Third-party transactions
    elif '*164*s*y\'ello,a transaction of' in body_text:
        if 'bundle' in body_text:
            categories['Internet_and_voice_bundles'].append(message_xml)
        categories['third_party_transactions'].append(message_xml)

    # For Miscellaneous messages anything that fails to pass the conditions
    else:
        categories['miscellaneous_messages'].append(message_xml)

# For Loop to act as a search bar for each category to categorize them
for element in root:
    if 'body' in element.attrib:
        body_text = element.attrib['body'].lower()
        message_xml = ET.tostring(element, encoding='unicode')
        categorize_message(body_text, message_xml)

# Fuction to categorize the data from conditions to files
def organise_into_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item)

# Loop for the organising function for each category when code is run
for category, data in categories.items():
    organise_into_file(f'Categorised_Data/{category}.xml', data)

