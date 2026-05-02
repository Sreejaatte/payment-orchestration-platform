from fastapi import FastAPI
from app.api.v1.endpoints.payment import router as payment_router
from app.middleware.error_handler import global_exception_handler

app = FastAPI(
    title="Payment Orchestration Platform",
    version="1.0.0",
    description="Production-grade payment routing and orchestration backend"
)

app.include_router(payment_router, prefix="/api/v1/payments", tags=["Payments"])
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def health():
    return {"status": "healthy", "service": "payment-orchestration-platform"}
