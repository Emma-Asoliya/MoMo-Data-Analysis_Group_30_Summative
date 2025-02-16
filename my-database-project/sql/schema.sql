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

CREATE TABLE Business (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

CREATE TABLE Transaction_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type VARCHAR(100) NOT NULL,
    transaction_date DATETIME NOT NULL,
    description TEXT NOT NULL,
    sender_phone VARCHAR(15) NOT NULL,
    receiver_phone VARCHAR(15) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);