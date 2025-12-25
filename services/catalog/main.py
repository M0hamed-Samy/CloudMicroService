from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Product(BaseModel):
    id: str | None = None
    name: str
    price: float
    stock: int

products = {}

@app.post("/products")
def create_product(product: Product):
    product.id = str(uuid.uuid4())
    products[product.id] = product
    return product

@app.get("/products")
def get_products():
    return list(products.values())

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    products.pop(product_id, None)
    return {"message": "deleted"}
