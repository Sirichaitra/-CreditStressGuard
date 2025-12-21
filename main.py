from core.etl import load_data
from core.feature_engineering import build_features
from core.risk_model import calculate_risk
from core.recommendation_engine import recommend
from db_connection import get_connection
from sqlalchemy import text
import datetime

print("test----0")
transactions, loans, accounts = load_data()

print("test----1")
features = build_features(transactions, loans)
risk_df = calculate_risk(features)

print("test----2")
engine = get_connection()

# ✅ FIX: Use correct column name from DB schema
insert_sql = text("""
    INSERT INTO risk_alerts
    (customer_id, risk_score, risk_level, recommendation, generated_on)
    VALUES (:customer_id, :risk_score, :risk_level, :recommendation, :generated_on)
""")

print("test----3")
print(risk_df)

print("test----4")
with engine.begin() as conn:
    for _, row in risk_df.iterrows():
        print("test----5")
        conn.execute(
            insert_sql,
            {
                "customer_id": int(row["customer_id"]),
                "risk_score": float(row["risk_score"]),
                "risk_level": row["risk_level"],
                "recommendation": recommend(row["risk_level"]),
                "generated_on": datetime.date.today(),  # ✅ match DB column
            }
        )

print("✅ Risk assessment completed successfully")
