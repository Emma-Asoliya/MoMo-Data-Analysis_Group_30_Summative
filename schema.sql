CREATE DATABASE IF NOT EXISTS momo_data_analysis;
USE momo_data_analysis;


CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    transaction_type ENUM(
        'Airtime Purchases',
        'Bank Deposits',
        'Cash Power Purchases',
        'Incoming Money',
        'Internet and Voice Bundles',
        'Payments to Code Holders',
        'Transfers to Mobile Numbers',
        'Withdrawals from Agents',
        'Third Party Transactions'
    ) NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_time TIME NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'RWF',
    fee DECIMAL(10,2) NOT NULL DEFAULT 0,
    code VARCHAR(50) NULL,
    sender VARCHAR(255) NULL,
    receiver VARCHAR(255) NULL,
    phone_number VARCHAR(20) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM transactions LIMIT 100;
SELECT transaction_type, COUNT(*) FROM transactions GROUP BY transaction_type;


DESC transactions;
SHOW TABLES;
