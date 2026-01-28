from fastapi import FastAPI, HTTPException
from dpd.http_client import fetch_json, FetchError

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def users():
    try:
        return fetch_json("https://jsonplaceholder.typicode.com/users")
    except FetchError as e:
        # gör om ditt interna fel till ett "API-fel" för klienten
        raise HTTPException(status_code=502, detail=str(e))
