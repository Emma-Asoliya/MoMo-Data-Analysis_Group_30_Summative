-- This file contains SQL scripts for cleaning up the database, such as removing duplicates or resetting tables.

-- Remove duplicate transactions based on user_id, category_id, and transaction_date
DELETE FROM Transaction_type
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Transaction_type
    GROUP BY user_id, category_id, transaction_date
);

-- Reset the Users table (optional)
DELETE FROM Users;

-- Reset the Categories table (optional)
DELETE FROM Categories;

-- Reset the Business table (optional)
DELETE FROM Business;