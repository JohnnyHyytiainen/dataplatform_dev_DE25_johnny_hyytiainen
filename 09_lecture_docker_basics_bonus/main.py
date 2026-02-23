from fastapi import FastAPI
from starlette import status
from schema.product_lecture_09 import ProductSchema

app = FastAPI(title="Lecture_09")


@app.get("/")
def root():
    return {"Message": "Hello world!"}


# Första endpoint.
@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)


def post_product(products: ProductSchema) -> ProductSchema:

    return products
