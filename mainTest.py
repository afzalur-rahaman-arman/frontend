from models import Product
from fastapi import FastAPI

app =FastAPI()


@app.get("/")
def welc():
    return "Welcome to the Afzal's FastAPI application"


materials = [
   Product(id=101, name= "Material 1", description = "V2.0", price = 10000.0, quantity= 99),
   Product(id=102, name= "Material 2", description = "V2.0", price = 10000.0, quantity= 99),
   Product(id=103, name= "Material 3", description = "V2.0", price = 10000.0, quantity= 99),
   Product(id=104, name= "Material 4", description = "V2.0", price = 10000.0, quantity= 99),
   Product(id=105, name= "Material 5", description = "V2.0", price = 10000.0, quantity= 99)
]

@app.get("/materialsss/")
def get_materials():
    return materials


@app.get("/m/{id}")
def materials_show(id: int):
    for mat in materials:
        if mat.id== id:
            return mat
@app.post("/p")
def add_post(mm: Product):
    materials.append(mm)
    return materials
