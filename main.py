from core.etl import load_data
from core.feature_engineering import build_features
from core.risk_model import calculate_risk
from core.recommendation_engine import recommend
from core.db_connection import get_connection
import datetime

transactions, loans, accounts = load_data()
features = build_features(transactions, loans)
risk_df = calculate_risk(features)

conn = get_connection()
cursor = conn.cursor()

for _, row in risk_df.iterrows():
    cursor.execute(
        "INSERT INTO risk_alerts VALUES (%s,%s,%s,%s,%s)",
        (
            row["customer_id"],
            float(row["risk_score"]),
            row["risk_level"],
            recommend(row["risk_level"]),
            datetime.date.today()
        )
    )

conn.commit()
conn.close()
print("Risk assessment completed successfully")