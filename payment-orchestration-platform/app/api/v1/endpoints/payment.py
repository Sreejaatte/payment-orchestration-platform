from fastapi import APIRouter
from app.schemas.payment import PaymentRequest, PaymentResponse
from app.services.payment_service import payment_service

router = APIRouter()

@router.post("/process", response_model=PaymentResponse)
def process_payment(payload: PaymentRequest):
    return payment_service.process(payload.model_dump())
