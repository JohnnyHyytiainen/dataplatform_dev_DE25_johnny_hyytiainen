from fastapi import FastAPI, status
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json # convert Pydantic -> JSON
from psycopg import Connection      # open temporary connection.

from schema.products_lecture_05 import ProductSchema


# Vill jag köra skriptet så använd
# python -m src.dpd.lecture_05_fastAPI.py

DATABASE_URL = "postgresql://postgres:Admin1@localhost:5432/lecture_05"
pool = ConnectionPool(DATABASE_URL)
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

    # query-insert
    with pool.connection() as conn:
        insert_product(conn, product.model_dump())
        conn.commit()

    return product



# helper method for DB queries (can be in a seperate file for the class)
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
    "INSERT INTO products_raw (product) VALUES (%s)",
    (Json(product),)
    )
