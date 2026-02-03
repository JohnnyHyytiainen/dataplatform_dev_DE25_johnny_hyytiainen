# Lecture 05 notes. FastAPI & PostgreSQL + PGadmin4
- Förbered data med FastAPI.
  - (installerat PostgreSQL innan lektion då det ej fanns pga docker och containerized postgres tidigare)

# Run App
* `$ fastpi dev <FILENAME>`

## Storing data - philosophy

* What's the purpose of our data?
  * Bulk uploading
  * JSON data storage
  * Unorganized data
  * PostgreSQL database
* What's the datatype of said data?
  * Unorganized 
  * unstructured
  * Json

## Database - PostgreSQL
A newly created database does NOT contain any TABLES by default.
- Step 1
```postgresql
CREATE TABLE IF NOT EXISTS products_raw (
  id BIGSERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  product JSONB NOT NULL
);
```

- Step 2 - Implement function for Insert (fastAPI)
```postgresql



```