import uuid

class PaymentService:
    def process(self, data: dict):
        gateway = "Stripe" if data["amount"] < 1000 else "Razorpay"
        return {
            "transaction_id": str(uuid.uuid4()),
            "status": "SUCCESS",
            "gateway": gateway
        }

payment_service = PaymentService()
