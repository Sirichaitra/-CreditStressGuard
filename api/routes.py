from fastapi import APIRouter
from db_connection import get_connection
from api.schemas import RiskResponse
from sqlalchemy import text

router = APIRouter()

@router.get("/risk/{customer_id}", response_model=RiskResponse)
def get_customer_risk(customer_id: int):
    engine = get_connection()  # SQLAlchemy Engine
    query = text("""
        SELECT customer_id, risk_score, risk_level, recommendation
        FROM risk_alerts
        WHERE customer_id = :customer_id
        ORDER BY generated_on DESC
        LIMIT 1
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"customer_id": customer_id}).mappings().first()

    if not result:
        return RiskResponse(
            customer_id=customer_id,
            risk_score=0.0,
            risk_level="Unknown",
            recommendation="No data available"
        )

    return RiskResponse(**result)
