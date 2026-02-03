from typing import Union
from fastapi import FastAPI, status
from schema.user import UserSchema, UserSchemaOutput
from schema.fox import FoxSchema
import requests

# Vill jag köra skriptet så använd 
# python -m src.dpd.lecture_03_main

userlist: list[UserSchema] = [
    UserSchema(username="Benny", password="123", is_enabled=True),
    UserSchema(username="Lenny", password="321", is_enabled=False),
    UserSchema(username="Jenny", password="1234", is_enabled=True)
]

app = FastAPI(title="My first API app")


# query param. Query parameter. Tre endpoints (en som heter /items, en som heter /users)
# Första endpoint.
@app.get("/")
def root():
    return {"Hej": "wurld"}

# Andra endpoint.
@app.get("/items/{item_id}")
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}

# Tredje endpoint.
@app.get("/users", response_model=list[UserSchemaOutput])
def get_users() -> list[UserSchemaOutput]:
    return userlist

# Fjärde endpoint
@app.post(
    "/users",
    response_model=UserSchemaOutput,
    status_code=status.HTTP_201_CREATED
)
def post_user(user: UserSchema) -> UserSchema:
    userlist.append(user)
    return user


@app.get("/fox", response_model=FoxSchema)
def get_fox() -> FoxSchema:
    response = requests.get("https://randomfox.ca/floof/")
    result_json = response.json()
    fox = FoxSchema(**result_json) # Konverterar json till python object

    return fox
