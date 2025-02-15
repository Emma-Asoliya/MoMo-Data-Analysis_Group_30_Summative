INSERT INTO Users (name, phone_number) VALUES
('Frances Saint', '1234567890'),
('Paris Alison', '0987654321'),
('Emma Briggs', '1234567890'),
('Sam Tyrone', '0987694321');

INSERT INTO Categories (name, description) VALUES
('Incoming Money', ' Money received from another user'),
('Payments to Code Holders', 'Payments made to registered businesses or merchants'),
('Transfers to Mobile Numbers','Money sent to another user'),
('Bank Deposists', 'Money deposited into the user''s account'),
('Airtime Bill Payments', 'Purchasing Airtime using Mobile money'),
('Cash Power Bill Payments', 'Paying for electricity using Mobile money'),
('Transactions Inititaed by Third Paries', 'Transactions initiated by third parties'),
('Withdrawals from Agents', 'Money withdrawn from a mobile money agent'),
('Bank Transfers', 'Money sent to a bank account'),
('Internet and Voice Bundle Purchases', 'Buying internet and voice bundles using mobile money'),

INSERT INTO Transaction_type (user_id, category_id, amount, transaction_type, transaction_date, description, sender_phone, receiver_phone) VALUES
(1, 1, 80000.00, 'Incoming Money', '2021-01-01 12:00:00', 'Money received from Paris Alison', '0987654321', '1234567890'),
(2, 2, 500000.00, 'Payments to Code Holders', '2021-01-01 12:00:00', 'Payment made to Business', '1234567890', '0987654321'),
(3, 3, 2900.00, 'Transfers to Mobile Numbers', '2021-01-01 12:00:00', 'Money sent to Sam Tyrone', '1234567890', '0987694321'),
(4, 4, 10.00, 'Bank Deposists', '2021-01-01 12:00:00', 'Money deposited into the user''s account', '1234567890', '1234567890'),
(1, 5, 5.00, 'Airtime Bill Payments', '2021-01-01 12:00:00', 'Purchasing Airtime using Mobile money', '1234567890', '1234567890'),
(2, 6, 10.00, 'Cash Power Bill Payments', '2021-01-01 12:00:00', 'Paying for electricity using Mobile money', '1234567890', '1234567890'),
(3, 7, 15.00, 'Transactions Inititaed by Third Paries', '2021-01-01 12:00:00', 'Transactions initiated by third parties', '1234567890', '1234567890'),
(4, 8, 20.00, 'Withdrawals from Agents', '2021-01-01 12:00:00', 'Money withdrawn from a mobile money agent', '1234567890', '1234567890'),
