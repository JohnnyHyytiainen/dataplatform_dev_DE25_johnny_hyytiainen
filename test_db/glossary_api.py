from fastapi import FastAPI, HTTPException
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json # För att spara listan som JSONB
from test_db.schema.glossary_schema import GlossaryInput


app = FastAPI()

# connection string
DB_URL = "postgresql://postgres:Admin1@localhost:5432/test_db"
pool = ConnectionPool(DB_URL)

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