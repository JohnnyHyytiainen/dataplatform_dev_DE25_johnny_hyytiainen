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
    - uvicorn är vår servlett när det kommer till FastAPI.

## Pipeline, the flow of data (slide 10)
- Konsekvent form av data. Grund data ska aldrig förändras. Du kan ändra genom att lägga till, transformera men bibehåll alltid din single source of truth
  - SSOT(Single Source Of Truth) UTGÅNGSPUNKTEN.


## Filetypes.
- **CSV (Comma Seperated Values)**
  - (Läs mer om 'Delimiter')
  - CSV är bra för filer som är upp till en viss storlek.
  - ASCII vs Binary. Ascii = översättning av binärkod.

- **JSON - JSONL/NDJSON (Slide 18-20)**
  - Vad hade hänt om du försöker läsa in en 100+mg stor JSON fil via API?
    - Det hade tagit väldigt lång tid, bottlenecks(in memory data). Appen blir överbelastad.
    - Vid större filer vill vi separera dom och streama ett objekt i taget

- **Parquet (slide 21-22)**
  - Gold standard för databaser. Väldigt mycket mindre filer och jobbar med kolumner(columnar storage) istället för rad baserad storage(row based storage. Tänk CSV)
  - Fördelar är:
    - Bättre kompression
    - Effektivare analytiska queries(?)

- **Avro (slide 23-25)**
  - Till för streaming events(Kafka använder sig utav detta(?))
  - Avro är binär data(hög prestanda). Förstått av maskiner men ej läsbart av människor jämfört med t.ex JSON(läsbart av människor)

- **ORC(Optimized Row Columner) (slide 26-27)**
  - ORC verkar vara en legacy filtyp.

- **XML (slide 28)**
  - EXtensible MArkup Language
  - Börjar också gå mot legacy hållet, i SOAP(Single access protocol kan man stöta på XML men man börjar som sagt gå ifrån det)
  - Ganska så lik JSON

- **TXT/LOG (slide 29)**
  - Loggfiler, EJ binär data. Innehåller t.ex processer ifrån rörelserna en 3D printer har gjort, eller hur mycket data som har förts över (se slide 29)
  


- **Excel spreadsheet (XLSX) (slide 30)**
  - XLSX är ett binärt strukturerat filformat för spreadsheets. Baserat på XML.
  - Väldigt vanligt som folk på kontor förstår och kan. Lätt att hantera men kan väldigt enkelt rusa ifrån en(onödigt stora filer och issues)


- **GZIP och ZIP filer (slide 31)**
  - Zippade och komprimerade filer.
  - Kan Spark/Pandas läsa zippade filer, läste om splitting och att det är kan läsas parallellt eller måste det läsas sekventiellt? (Kommer under kommande Pandas föreläsning)

- **ETL(Extract, Transform, Load) (Slide 32-37)**
  - Extrahera data från någon källa, t.ex API'er, JSONL filer, JSON filer, från databas till t.ex skriva den i CSV etc etc. När jag TAR information ifrån ett håll så extraherar jag data. (slide 33)

  - Är datan på slide 34 redo att förvaras?
    - Svar: Nej. Den behöver transformeras, trimma whitespaces, normalisera versaler etc.

  - Data transformation is ecerything you do to clean, reshape and standardize the data so it can be **trusted** and **used**.


  - Load, tar transformerad data och loadar(sparar över till CSV, JSON/JSONL, XML, vad som helst format) till fil eller databas dvs ett data repository(där datan lagras)

- **ELT(Extract, Load, Transform) (slide 38-40)**
  - Extraherar och tar data ifrån källor
  - Laddar datan
  - Transformerar datan



