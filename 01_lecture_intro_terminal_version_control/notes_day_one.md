# Programmering inom dataplatform dev, dag 1 - Notes.

## Incheckning med lärare i kursen. Koll på klassen för att uppskatta vart kunskap finns och vilken nivå på kunskap.

- Fråga till klassen om intresse för Java om tid finns över. Svaret var ja.  
- Fråga till klassen om intresse för att lära sig mer vad som händer med Python under huven. Svaret var ja.

## Focus areas: Pandas, FastAPI, Docker, Kafka, RabbitMQ. Fixing a few dependencies regarding ETL(etl dependency framework for python).  


## Intro slides.

- Intro, "vad gör vi när data strukturen inte är hållbar?"
    - Vad gör vi med den infon/datan som skickas och tas emot?
    - (Stor overview. Helikopter-perspektiv)
    - Material publiceras på learnpoint (inspelningar, PDFs, github repos etc.)
    - Info tillkommer senare när det kommer till planering och grupparbeten.
    - Feedback "ska ske inom rätt forum" (Läraren har sina åsikter kring feedback. Konstruktiv kritik uppskattas. Helst ej under lektion.)


    ### (Att hålla koll på)
    - Rabbit MQ + Kafka. - Använda python mot event streaming. 
    - FastAPI: XML, JSON, API, CSV - använda python mot relationsdatabaser och andra datakällor

## Kursplan:
- (finns på learnpoint)


## Data platform. Vad är det?
- En dataplattform är teknik som samlar in, lagrar och bearbetar data så att den är korrekt, tillgänglig och pålitlig att använda.
- Vad är det? En dataplattform är ett parallellt system som kopierar data ifrån andra system för att man inte ska störa dom och för att kunna arbeta med data fritt.
- Typer av dataplattformar: 
- Enterprise data platform (EDP)
- Big data platform (BDP)
- Cloud data platform (CDP)
- Customer data platform (CDP)
- ibm.com topics dataplatform <-- Mer info

## Data platform består av (lager)
- Data ingestion, pulls data from apps, DBS andra sources.
- Data storage
- Data transformation
- BI and analytics
- Additional layers
- data observability

---


## Data overview.
- Vilken data sparas? 
    - ALLT för att göra det enkelt.  


## Open data.

**Consuming Data**
- Consuming data in programming involves accessing and utilizing information from external sources, often through APIs.  

- **Open data consumption empowers** developers to create innovative solutions, enhance functionality and provide meaningful insights by connecting users wtih a wealth of accessible and structured information.

## Terminologies
- Dataset, a structured collection of related data.
- API/WS, A set of protocols for accessing and interacting with data or services.
- Open Data, Public available data that anyone can access, use and share.  

## Terminal - CLI interface(Cli-gränssnitt)
- How to move, inspect and control your system.
- (standard linux kommandon med git. ls, ls -a, pwd, cd .. , mkdir , googla vidare på standard linux commands. (Skiljer sig. Kunde t.ex ej köra det command lärare gjorde för att öppna. Var tvungen att använda explorer. Viss skillnad på mac och winOS + Git bash))

## Git and git ls, git ls-files, grep och git rm
- Github == cloud
- git ls-files
  - (Visar alla icke gömda filer i projektet/repot som FINNS committade via git)

- git ls-files | grep filnamn  
  - (filtrerar resultat på beroende vad du har skrivit in) 

- git rm filename
  - (tar bort en committad och pushad fil. Du måste ÄVEN committa och pusha för att få bort den ifrån github.)

## Branches inom git. Vad innebär branches?
- Förgreningar av main. För att flera kan jobba på samma projekt, förgrena main och utveckla för att sedan merge med main. Inte jobba direkt på main. **MAIN IS HOLY**

- Branches är till för struktur för att ej jobba i main om main är i production. 