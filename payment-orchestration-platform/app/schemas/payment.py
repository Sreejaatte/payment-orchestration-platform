from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    customer_id: str
    amount: float = Field(..., gt=0)
    currency: str
    payment_method: str

class PaymentResponse(BaseModel):
    transaction_id: str
    status: str
    gateway: str
