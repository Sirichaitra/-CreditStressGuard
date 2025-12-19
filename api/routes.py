from fastapi import APIRouter
from core.db_connection import get_connection
from api.schemas import RiskResponse

router = APIRouter()

@router.get("/risk/{customer_id}", response_model=RiskResponse)
def get_customer_risk(customer_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT customer_id, risk_score, risk_level, recommendation
        FROM risk_alerts
        WHERE customer_id = %s
        ORDER BY generated_on DESC
        LIMIT 1
    """, (customer_id,))

    result = cursor.fetchone()
    conn.close()

    if not result:
        return {
            "customer_id": customer_id,
            "risk_score": 0.0,
            "risk_level": "Unknown",
            "recommendation": "No data available"
        }

    return result