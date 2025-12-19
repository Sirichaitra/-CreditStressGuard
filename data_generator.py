import pandas as pd
import numpy as np
from db_connection import get_connection

np.random.seed(42)
conn = get_connection()
cursor = conn.cursor()

# Customers
for i in range(1, 201):
    cursor.execute(
        "INSERT INTO customers VALUES (%s,%s,%s,%s)",
        (i, f"Cust_{i}", np.random.randint(25,60), "Retail")
    )

# Accounts
for i in range(1, 201):
    cursor.execute(
        "INSERT INTO accounts VALUES (%s,%s,%s)",
        (i, i, np.random.randint(5000,500000))
    )

# Loans
for i in range(1, 151):
    cursor.execute(
        "INSERT INTO loans VALUES (%s,%s,%s,%s,CURDATE())",
        (i, i, np.random.randint(100000,2000000), np.random.randint(3000,25000))
    )

# Transactions
txn_id = 1
for acc in range(1, 201):
    for _ in range(60):
        cursor.execute(
            "INSERT INTO transactions VALUES (%s,%s,CURDATE() - INTERVAL %s DAY,%s,%s)",
            (
                txn_id,
                acc,
                np.random.randint(1,60),
                np.random.choice(["credit","debit"]),
                np.random.randint(500,20000)
            )
        )
        txn_id += 1

conn.commit()
conn.close()
