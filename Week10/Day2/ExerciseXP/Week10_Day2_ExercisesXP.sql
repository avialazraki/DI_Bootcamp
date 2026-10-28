-- Week 10 Day 2 - Exercises XP: Items and Customers
-- PostgreSQL / pgAdmin 4
--
-- SETUP: The assignment asks for a database named "public".
-- In pgAdmin, right-click Databases > Create > Database > Database: public.
-- Alternatively, run the following command ONCE while connected to a DIFFERENT database,
-- then connect to the new "public" database before running the rest of this file:
--
-- CREATE DATABASE public;
--
-- Note: PostgreSQL also has a default schema named "public"; a database and
-- a schema are different objects. CREATE DATABASE cannot run inside a transaction.

-- Exercise 1: Create the two tables in the connected database.
CREATE TABLE IF NOT EXISTS items (
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Add the three items. ON CONFLICT makes the script safe to run again.
INSERT INTO items (item_id, item_name, price) VALUES
    (1, 'Small Desk', 100),
    (2, 'Large desk', 300),
    (3, 'Fan', 80)
ON CONFLICT (item_id) DO UPDATE
SET item_name = EXCLUDED.item_name,
    price = EXCLUDED.price;

-- Add the five customers.
INSERT INTO customers (customer_id, first_name, last_name) VALUES
    (1, 'Greg', 'Jones'),
    (2, 'Sandra', 'Jones'),
    (3, 'Scott', 'Scott'),
    (4, 'Trevor', 'Green'),
    (5, 'Melanie', 'Johnson')
ON CONFLICT (customer_id) DO UPDATE
SET first_name = EXCLUDED.first_name,
    last_name = EXCLUDED.last_name;

-- Query 1: All items (3 rows).
SELECT * FROM items ORDER BY item_id;

-- Query 2: Items with price strictly above 80 (2 rows).
SELECT * FROM items WHERE price > 80 ORDER BY item_id;

-- Query 3: Items with price <= 300, including 300 (3 rows).
SELECT * FROM items WHERE price <= 300 ORDER BY item_id;

-- Query 4: Customers whose last name is Smith (0 rows).
SELECT * FROM customers WHERE last_name = 'Smith' ORDER BY customer_id;

-- Query 5: Customers whose last name is Jones (2 rows).
SELECT * FROM customers WHERE last_name = 'Jones' ORDER BY customer_id;

-- Query 6: Customers whose first name is not Scott (4 rows).
SELECT * FROM customers WHERE first_name <> 'Scott' ORDER BY customer_id;
