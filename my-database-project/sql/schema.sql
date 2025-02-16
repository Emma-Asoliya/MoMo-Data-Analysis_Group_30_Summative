CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE Categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE Businesses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

CREATE TABLE Transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type VARCHAR(100) NOT NULL,
    transaction_date DATETIME NOT NULL,
    description TEXT NULL,
    sender_phone VARCHAR(15) NOT NULL,
    receiver_phone VARCHAR(15) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);


CREATE VIEW daily_summary AS
SELECT
    DATE(transaction_date) AS date,
    type_name,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM Transaction_type tt
GROUP BY DATE(transaction_date), tt.transaction_type;


CREATE VIEW monthly_summary AS
SELECT
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    type_name,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM transaction_type tt
GROUP BY MONTH(transaction_date), type_name;

CREATE VIEW user_transcation_summary AS
SELECT
    sender_phone,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount,
    MIN(transaction_date) AS first_transaction_date,
    MAX(transaction_date) AS last_transaction_date
    COUNT(DISTINCT type_id) AS unique_transaction_types
FROM Transaction_type
GROUP BY sender_phone
HAVING COUNT(*) > 1;
ORDER BY total_amount DESC;
