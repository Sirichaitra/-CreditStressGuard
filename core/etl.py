import pandas as pd
from db_connection import get_connection

def load_data():
    conn = get_connection()
    transactions = pd.read_sql("SELECT * FROM transactions", conn)
    loans = pd.read_sql("SELECT * FROM loans", conn)
    accounts = pd.read_sql("SELECT * FROM accounts", conn)
    conn.close()
    return transactions, loans, accounts
