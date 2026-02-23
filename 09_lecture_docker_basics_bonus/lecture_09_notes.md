# Lecture 09 notes
- Docker basics
- Lab recap. 
    - What do we do with missing values?
- BONUS MODULE: Hosting
    - Supabase (1gb)
    - Google bigstorage (10-20gb storage(?))

## Moduler för dagen:
- Pandas och missing values
- Pydantic Field Validation
- Docker
- Dockerizing
- Hosting with Supabase (bonus)
- Environment Variables recap

## Personal notes:
```text
Genomgång av labben, prata om problematiken vid arbete av data.
(Kolla upp github action/github actions på egen tid).
Torsdag 26/02 släpps grupperna för grupp-projektet.
```
**Recap och brief summering av labben (Se dagens slides(lecture_09 sides)):**
```text
Recap: vad innehöll labben? På ytan såg labben väldigt enkel ut, men det fanns medvetet ett par gråzoner och 'curve balls' för att göra labben mer komplex.

Att flagga något så är syftet enbart att uppmärksamma på att någonting är otydligt i datan. Till skillnad från att 'rejecta' någonting som innebär att datan sorteras bort och ej används, den är icke valid.

Felaktig data och risker kring det:
Det handlar om konsekvenstänkande. Datakvalitét kan bli en affärsrisk. Vi får ALDRIG gissa affärsKRITISK information i ett datalager. Antaganden hör hemma i kravspecifikation (I labbens fall så fanns det ingen, därav blev det diffust.)

När vi pratar om ramar kring just denna lab, vad är då ramarna? - Jo, det är där datamodellering kommer in i det hela. Innan du ens tittar på siffror så bör det finnas en modell först. (Det är det steget som själva kravspecs kommer ut ifrån(?))
(Ett 'data-kontrakt')

- Se över KPI(Key performance indicator)
- Se över QA gates mer(asserts i python t.ex)

Summering. Finansiell rapportering / KIPer
    - Oftast endast valid data

Explorativ analys/Kvalitétssäkring
    - Valid + flagga (med transparens)
```

**Next module. Pydantic modelling:**
```text
- Nytt projekt, installera lite dependencies.
    - uv add python-dotenv <-- Har det redan
    - uv add fastapi <-- Har det redan
    - uv add psycopg[binary, pool] <-- Har det redan

- Se schema/product_lecture_09.py
- Se 09_lecture_docker_basics_bonus/main.py
```
```text
Docker image basics, hur en Dockerfile ska utformas:

# FROM      - Image(Snapshot, vår startpunkt)
# WORKDIR   - Working directory ("/app") - A new folder within docker, called app
# COPY      - Extract a duplicate copy of our app (app snapshot)
# EXPOSE    - Includes a port that OS uses
# CMD       - Commands to be run on start up.

docker build -t min-api .
docker run -p 8000:8000 min-api
```