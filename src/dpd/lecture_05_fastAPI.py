from fastapi import FastAPI, status
import requests
from schema.products_lecture_05 import ProductSchema


# Vill jag köra skriptet så använd
# python -m src.dpd.lecture_05_fastAPI.py

app = FastAPI(title="lektion_05_postgresql_fastapi")


@app.get("/")
def root() -> dict:
    return {"Hej": "wurld"}


@app.post(
        "/products", 
        status_code=status.HTTP_201_CREATED, 
        response_model=ProductSchema
        )
def post_products(product: ProductSchema) -> ProductSchema:
    return product
