from pydantic import BaseModel
from typing import Optional

class RiskResponse(BaseModel):
    customer_id: int
    risk_score: float
    risk_level: str
    recommendation: str

class HealthResponse(BaseModel):
    status: str
