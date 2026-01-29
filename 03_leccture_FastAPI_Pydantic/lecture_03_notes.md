# Lecture 03(dag 3) FastAPI + Pydantic

## Table of contents för lecture 03(dag 3):

- Pydantic
- Project setup
- Installation
- FastAPI

--

## Deletion of __name__== "__main__": (FastAPI) (lärare pratar om main.py som kommer med när uv venv installeras)
- Varför tar vi bort den. 
- Servlet container. <- Kolla upp detta mer
    - Hosting of application (locally)
    - FastAPI introduces this new concept
    - Removes "traditional" 'play/start' button (<-- kolla upp mer)
    - Requires FastAPI start command to run app

`uv init`
`uv add fastapi "uvicorn[standard]" pandas pydantic-settings sqlalchemy psycopg2-binary lxml httpx`

## Endpoints
- API and URL related.
- consists of a path: '/example'    path = --> / <--
    - accompanied by an HTTP Method (ex, GET, POST, PUT, DELETE) 

## Decorators
- A decorator 'kännetecknas' av @ symbolen.
- Function over a function

## Commands for FastAPI
- fastapi dev FILENAME.py

## URL (query parameters - query param)
Exempel URL: https://www.google.com/search?q=unicorn
- ? == start of the query
- q == samma som query (just a variable name)
- = is a dynamic value(my search, the client input)

## Pydantic
- Pydantic uses Schema to define Logical data type structure.
- It is Class based
- Used for validation of data
- Facilitates conversions of JSON to python objects



