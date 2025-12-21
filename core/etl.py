import pandas as pd
from db_connection import get_connection

def load_data():
    print("load_data----1")
    conn = get_connection()
    print("load_data----2")
    transactions = pd.read_sql("SELECT * FROM transactions", conn)
    print("load_data----3")
    loans = pd.read_sql("SELECT * FROM loans", conn)
    print("load_data----4")
    accounts = pd.read_sql("SELECT * FROM accounts", conn)
    print("load_data----5")
    #conn.close()
    print(transactions)
    print(loans)    
    print(accounts)
    print("load_data----6")
    return transactions, loans, accounts

