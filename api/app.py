from fastapi import FastAPI
from api.routes import router
from api.schemas import HealthResponse

app = FastAPI(
    title="Banking Credit Risk Intelligence API",
    description="Early Warning Credit Stress Detection System",
    version="1.0"
)

@app.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "API is running"}

app.include_router(router)