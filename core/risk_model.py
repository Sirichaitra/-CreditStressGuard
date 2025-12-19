import numpy as np

def calculate_risk(df):
    df["cash_stress"] = df["total_debits"] / (df["emi_amount"] + 1)

    df["risk_score"] = (
        0.4 * np.tanh(df["cash_stress"]) +
        0.4 * df["emi_to_loan_ratio"] +
        0.2 * (df["debit_count"] / df["debit_count"].max())
    )

    df["risk_level"] = np.where(
        df["risk_score"] > 0.7, "High",
        np.where(df["risk_score"] > 0.4, "Medium", "Low")
    )

    return df
