from fastapi import FastAPI
from typing import Union


app = FastAPI(title="My first API app")

# Första endpoint.
@app.get("/")
def root():
    return {"Hej": "wurld"}

# query param. Query parameter. Två endpoints (en som heter items)
@app.get("/items/{item_id}")
def get_item(item_id: int, color: Union [str, None] = None):
    return {"item_id": item_id, "color": color}
