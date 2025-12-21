import numpy as np
from sqlalchemy import text
from db_connection import get_connection

# -------------------------------------------------
# Setup
# -------------------------------------------------
np.random.seed(42)
engine = get_connection()

# -------------------------------------------------
# Generate Customers
# -------------------------------------------------
customers = [
    {
        "customer_id": i,
        "name": f"Cust_{i}",
        "age": np.random.randint(25, 60),
        "segment": "Retail",
    }
    for i in range(1, 201)
]

# -------------------------------------------------
# Generate Accounts
# -------------------------------------------------
accounts = [
    {
        "account_id": i,
        "customer_id": i,
        "balance": round(np.random.uniform(5_000, 500_000), 2),
    }
    for i in range(1, 201)
]

# -------------------------------------------------
# Generate Loans (emi_amount + start_date)
# -------------------------------------------------
loans = [
    {
        "loan_id": i,
        "customer_id": i,
        "loan_amount": round(np.random.uniform(100_000, 2_000_000), 2),
        "emi_amount": round(np.random.uniform(3_000, 25_000), 2),
        "start_date": np.datetime64("2022-01-01") + np.random.randint(0, 900),
    }
    for i in range(1, 151)
]

# -------------------------------------------------
# Generate Transactions
# -------------------------------------------------
transactions = []
txn_id = 1

for account_id in range(1, 201):
    for _ in range(60):
        transactions.append(
            {
                "txn_id": txn_id,
                "account_id": account_id,
                "txn_date": np.datetime64("2024-01-01") - np.random.randint(1, 60),
                "txn_type": np.random.choice(["credit", "debit"]),
                "amount": round(np.random.uniform(500, 20_000), 2),
            }
        )
        txn_id += 1

# -------------------------------------------------
# Insert Data (AUTO COMMIT)
# -------------------------------------------------
with engine.begin() as conn:

    conn.execute(
        text("""
            INSERT INTO customers (customer_id, name, age, segment)
            VALUES (:customer_id, :name, :age, :segment)
        """),
        customers
    )

    conn.execute(
        text("""
            INSERT INTO accounts (account_id, customer_id, balance)
            VALUES (:account_id, :customer_id, :balance)
        """),
        accounts
    )

    conn.execute(
        text("""
            INSERT INTO loans
            (loan_id, customer_id, loan_amount, emi_amount, start_date)
            VALUES (:loan_id, :customer_id, :loan_amount, :emi_amount, :start_date)
        """),
        loans
    )

    conn.execute(
        text("""
            INSERT INTO transactions
            (txn_id, account_id, txn_date, txn_type, amount)
            VALUES (:txn_id, :account_id, :txn_date, :txn_type, :amount)
        """),
        transactions
    )

print("✅ Data generation completed successfully for bank_risk database")
