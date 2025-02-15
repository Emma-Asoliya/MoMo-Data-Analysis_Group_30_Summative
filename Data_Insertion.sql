INSERT INTO Users (name, phone_number) VALUES
('Frances Saint', '250876543219'),
('Paris Alison', '250123456789'),
('Emma Briggs', '2509987694321'),
('Sam Tyrone', '2500987694321'),


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
(1, 1, 80000.00, 'Incoming Money', '2021-01-01 12:00:00', 'Money received from Paris Alison', '250123456789', '250842187654'),
(2, 2, 500000.00, 'Payments to Code Holders', '2021-01-01 12:00:00', 'Payment made to Business', '250123456789', '250842187654'),
(3, 3, 2900.00, 'Transfers to Mobile Numbers', '2021-01-01 12:00:00', 'Money sent to Sam Tyrone', '250999666578', '250123456789'),
(4, 3, 100.00, 'Bank Deposists', '2021-01-01 12:00:00', 'Money deposited into the user''s account', '250842187654', '250999666578'),
(1, 5, 5.00, 'Airtime Bill Payments', '2021-01-01 12:00:00', 'Purchasing Airtime using Mobile money', '250123456789', '250999666578'),
(2, 6, 1000.00, 'Cash Power Bill Payments', '2021-01-01 12:00:00', 'Paying for electricity using Mobile money', '250999666578', '250842187654'),
(3, 2, 150.00, 'Transactions Inititaed by Third Paries', '2021-01-01 12:00:00', 'Transactions initiated by third parties', '250842187654', '250999666578'),
(4, 7, 2800.00, 'Withdrawals from Agents', '2021-01-01 12:00:00', 'Money withdrawn from a mobile money agent', '250842187654', '250999666578'),


INSERT INTO Business (name, category_id) VALUES
('MTN Rwanda', 10),
('Airtel Rwanda', 10),
('Bank of Kigali', 9),
('I&M Bank', 9),
('Rwanda Energy Group', 8),