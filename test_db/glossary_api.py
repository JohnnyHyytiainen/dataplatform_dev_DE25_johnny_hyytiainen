import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json # För att spara listan som JSONB
from psycopg.rows import dict_row # för att kunna få "dictionaries" och inte tuples.
from test_db.schema.glossary_schema import GlossaryInput

# 1. Ladda in variabler från .env filen till Pythons minne
load_dotenv()
# 2. Hämta värdet ifrån den
db_url = os.getenv("DATABASE_URL")
app = FastAPI()

if not db_url:
    raise ValueError("Ingen DATABASE_URL hittades. Se över om du har en .env fil!")

# connection string
pool = ConnectionPool(db_url)
print("Uppkopplad via .env(Environment Variables!)")

@app.post("/glossary")
def add_term(term_data: GlossaryInput):
    """
    Docstring for add_term
    (Tar emot en term och sparar i Postgres)
    :param term_data: Description
    :type term_data: GlossaryInput
    """
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                #sql frågan
                cur.execute("""
                    INSERT INTO glossary (term, definition, category, tags)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (
                    term_data.term,
                    term_data.definition,
                    term_data.category,
                    Json(term_data.tags)
                ))

                new_id = cur.fetchone()[0]
                conn.commit()

        return {"message": "Term saved", "id": new_id, "term": term_data.term}
    
    except Exception as e:
        # fångar exceptions, term finns redan pga UK constraint t.ex
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/glossary")
def get_all_terms():
    """hämtar alla termer ifrån DB"""
    try:
        with pool.connection() as conn:
            # row_factory=dict_row Säger till psycopg att ge mig mina svar som dicts och inte tuples!
            with conn.cursor(row_factory=dict_row) as cur:

                cur.execute("SELECT * FROM glossary ORDER BY id DESC")
                results = cur.fetchall() # här hämtar den alla rader

                conn.commit()
                return results
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))