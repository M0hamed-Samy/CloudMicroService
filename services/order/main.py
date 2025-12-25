from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Order(BaseModel):
    id: str | None = None
    items: list
    status: str = "CREATED"

orders = {}

@app.post("/orders")
def create_order(order: Order):
    order.id = str(uuid.uuid4())
    orders[order.id] = order
    return order

@app.get("/orders")
def get_orders():
    return list(orders.values())

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return orders.get(order_id)

@app.put("/orders/{order_id}/status")
def update_status(order_id: str, status: str):
    if order_id in orders:
        orders[order_id].status = status
    return orders.get(order_id)

@app.delete("/orders/{order_id}")
def delete_order(order_id: str):
    orders.pop(order_id, None)
    return {"message": "order deleted"}
