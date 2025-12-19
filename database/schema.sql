CREATE DATABASE bank_risk;
USE bank_risk;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    segment VARCHAR(20)
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    balance DECIMAL(15,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    loan_amount DECIMAL(15,2),
    emi_amount DECIMAL(10,2),
    start_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    txn_id INT PRIMARY KEY,
    account_id INT,
    txn_date DATE,
    txn_type VARCHAR(10),
    amount DECIMAL(12,2)
);

CREATE TABLE risk_alerts (
    customer_id INT,
    risk_score FLOAT,
    risk_level VARCHAR(20),
    recommendation VARCHAR(100),
    generated_on DATE
);