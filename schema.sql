CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100 NOT NULL),
    phone_number VARCHAR(12) UNIQUE NOT NULL,
);


CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Transaction_type (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    category_id INT REFERNCES categories(category_id) ON DELETE SET NULL
    amount DECIMAL(10,2) NOT NULL,
    transaction_type VARCHAR(50),
    transaction_date TIMESTAMP NOT NULL,
    description TEXT,
    sender_phone VARCHAR(12),
    receiver_phone VARCHAR(12)
);

CREATE TABLE Business (
    merchant_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    category_id INT REFERENCES categories(category_id) ON DELETE SET NULL
);