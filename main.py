

from fastapi import FastAPI, HTTPException
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, welcome to the program!"

products = [
    Product(id=1, name="Product 1", description="Description 1", price=10.99, quantity=5),
    Product(id=2, name="Product 2", description="Description 2", price=20.99, quantity=10),
    Product(id=3, name="Product 3", description="Description 3", price=30.99, quantity=15)
]

@app.get("/products/")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product
