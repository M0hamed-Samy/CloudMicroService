from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CartItem(BaseModel):
    product_id: str
    quantity: int

cart = {}

@app.post("/cart")
def add_item(item: CartItem):
    cart[item.product_id] = item
    return item

@app.get("/cart")
def get_cart():
    return list(cart.values())

@app.put("/cart/{product_id}")
def update_item(product_id: str, quantity: int):
    if product_id in cart:
        cart[product_id].quantity = quantity
    return cart.get(product_id)

@app.delete("/cart/{product_id}")
def remove_item(product_id: str):
    cart.pop(product_id, None)
    return {"message": "removed"}
