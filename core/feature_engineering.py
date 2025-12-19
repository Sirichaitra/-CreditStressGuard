import pandas as pd
import numpy as np

def build_features(transactions, loans):
    txn_summary = transactions.groupby("account_id").agg(
        total_debits = ("amount", lambda x: x[transactions.txn_type=="debit"].sum()),
        debit_count = ("amount", "count")
    ).reset_index()

    loan_features = loans.copy()
    loan_features["emi_to_loan_ratio"] = (
        loan_features["emi_amount"] / loan_features["loan_amount"]
    )

    features = loan_features.merge(
        txn_summary, left_on="customer_id", right_on="account_id", how="left"
    )

    features.fillna(0, inplace=True)
    return features
