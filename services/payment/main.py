from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Payment(BaseModel):
    id: str | None = None
    order_id: str
    amount: float
    status: str = "PAID"

payments = {}

@app.post("/payments")
def create_payment(payment: Payment):
    payment.id = str(uuid.uuid4())
    payments[payment.id] = payment
    return payment

@app.get("/payments")
def get_payments():
    return list(payments.values())

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: str):
    payments.pop(payment_id, None)
    return {"message": "payment deleted"}


