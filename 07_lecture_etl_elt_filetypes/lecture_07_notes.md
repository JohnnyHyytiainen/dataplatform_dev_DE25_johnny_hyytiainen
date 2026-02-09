# Lecture 07 notes
- Todays lecture focuses on ETL&ELT + filetypes

## overview for lectures
- lecture 08, pandas. Most of it has been pushed forward with one day.

## Moduler:
- ETL
- ELT
- Filetypes
  - Workshop with DQ(Data Quality)

- Förberedelser för att få igång ett projekt med massor av data.  
- Genomgång av "BONUS" slide, prat om venv/bin/activate. (slide 8)  
- Prat om uvicorn och vad det gör i FastAPI, `uvicorn` är "servern" kan man säga enkelt.  
  - Vissa kör `fastapi dev <filename>` vs andra kör `uv run uvicorn app.main:app --reload`   
    - Kolla upp VARFÖR det är **uv run uvicorn folder.skript:folder(?)**   
    - **(--reload är nog enbart för att ladda om. Du kan nog köra igång utan --reload)**  

## Pipeline, the flow of data (slide 10)
- Konsekvent form av data. Grund data ska aldrig förändras. Du kan ändra genom att lägga till, transformera men bibehåll alltid din single source of truth
  - SSOT(Single Source Of Truth) UTGÅNGSPUNKTEN.

  
