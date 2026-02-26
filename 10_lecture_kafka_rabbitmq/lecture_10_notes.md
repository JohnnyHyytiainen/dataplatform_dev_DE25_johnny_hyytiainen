# Lecture 10 notes
- Docker compose
- Apache Kafka ' Crafting a functional pipeline for realtime data streaming'

## Moduler för dagen:
- Docker compose
- Kafka (terminologies)
- Kafka consumers (bonus)
    - (Ex, ha 4-5st appar som skapas och körs i bakgrunden)

## Commands för docker:
- Nuke it all:
    - `docker compose down -v`
- Build:
    - `docker compose up --build`


## Personal notes:
```text
Inom enterprise är det väldigt vanligt med SR principer(single responsibility). Konceptet innebär att dela upp ansvar, var sak har sitt ansvarsområde, därav flera moduler för att hålla igång hela "systemet".
Tänk: SoC principen, både SoC och SR tillhör samma kategori(I min uppfattning)

Docker-compose: Multi containers. 
FastAPI app(Dockerfile), PostgreSQL(Dockerfile), Back-end(Dockerfile) -> Docker-compose.yml "kopplar ihop" alla bilder och containerizes alla images och under ett och samma nätverk(privat(?)) och får alla att leka väl med varandra.
```
## Vad jag ska lyssna efter och fokusera på kring kafka:

- Immutable Log: I en databas kan du ändra en rad (UPDATE). I Kafka kan du aldrig ändra något. Ett meddelande som har skrivits sitter där det sitter. Man lägger bara till nya längst bak.

- Decoupling (Isolering): Detta är nyckeln. Producern (den som skickar data) skiter fullständigt i om Consumern lever eller är död. Producern bara dumpar data på rulltrappan och går därifrån.

- Consumer Groups: Om du har 100 000 meddelanden i sekunden, kan du sätta 5 stycken "appar" (Consumers) som jobbar tillsammans och delar på bördan. Det är så man skalar system till Netflix-nivå.

## Kafka Terminology:
- Term      -   Vad det faktiskt är (enkelt förklarat)
- Broker    -   Själva servern (motorn) som kör Kafka.
- Topic     -   "En ""mapp"" eller kategori där meddelanden lagras."
- Producer  -   "Appen som ""skriver"" data till ett topic."
- Consumer  -   "Appen som ""läser"" data från ett topic."
- Offset    -   Ett unikt ID (som ett sidnummer) för varje meddelande så att consumern vet var den slutade läsa.



Egna terms att dubbelkolla kring kafka:


- Record. Ett enskilt meddelande. <--- Luddigt
    - Exempel: JSON {"order_id": 123, "ammount": 100}
    - Records streamas(skickas) även kallat EVENTS
    - Allt som ska spåras(sparas) skickas vidare till Topics. Record är relaterat till Topics.

- Så ett Record(event(?)) skickas till ett Topic((?))
    - Flera ordrar går in i ett ämne.

---

- Partition. En topic innehåller flera partitions (ENBART APPEND. APPEND ONLY och EJ ÄNDRAS!)
    - En topic innehåller flera delar(Partitions)
        - En partition innehåller ett antal Partitions
            - En partition kan ses som en

Exempel:

Topic: orders

    Partition 0
        offset 0 -> {order 123}
        offset 1 -> {order 125}
    
    Partition 1
        offset 0 -> {order 201}
        offset 1 -> {order 202}

---
Kafka Broker. <-- Luddigt 
- En server som sparar data ifrån topics (som innehåller orders som i sin tur innehåller partitions som innehåller offsets)

---

Kafka Controller. <-- OTROLIGT luddigt
- Controller styr metadatan och INTE datan. Den bestämmer:
- vem som ska vara leader för partition 0
- Vad händer om broker 1 dör
- Hur ska partitions fördelas?
- När skapas topics?
    - Hanterar kluster logic och inte records
---

Vad för verktyg behövs och som behövs kollas upp:
- Python dependencies som hanterar asynkron och synkron.
    - Async <-- Kolla upp mer
    - Sync  <-- Kolla upp mer

- Kafka Python <--
    - `uv add kafka-python`
    - (kommer hamna i pyproject.toml som alltid)

- In i .env filen för att lägga till:  
    - KAFKA_BOOTSTRAP_SERVERS=kafka:9092
    - PRODUCTS_TOPIC=products.created 


---
Todo:
Utforma docker-compose.yml fil
Skapa docker container
Koppla postgres db för att ta emot data/innehålla data

Gör egen mini app, skapa api med två, tre enkla endpoints. GET, GET(?), POST

- Posta lite data via postman till API(?)

- Få in det i DB (containerized via docker(?))

- In i Apache Kafka GUI(För visuell feedback. Det är nog enklast väg för förståelse)

- Lägg till Kafka på det och gå igenom basics i enkel form för att förstå teorin bakom allting. Basics och förståelse för basics == prio.

---
När det kommer till kodandet behövs en miljö variabel i ditt script (kafka setup)
- Kafka producer (sync)

```python

KAFKA_BOOTSTRAOP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
PRODUCTS_TOPIC = os.getenv("PRODUCTS_TOPIC", "products.created")

# Kafka producer (sync) Import from kafka import KafkaProducer och lägg bland dina imports FÖRST
# import json
# Ska vara en decorator någonstans med @async... ???

# Kafka producer (sync) introduces creation of Records (messages + requests)
# boilerplate setup. MÅSTE GÖRAS för att kunna kommunicera med Kafka
app.state.kafka_producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    key_serializer=lambda k: k.encode("utf-8") if k else None,

)

yield

# shutdown
try:
    app.state.kafka_producer.close()

except Exception: # lägg till mer graciös error-handling
    pass

app.state.pool.close()

```
(se main.py i lecture 10 repot)
Där jag gör min POST (row innehåller mitt objekt)
Skapa även event objektet
```python
 event = {
    "type": "product.created",
    "product_id": row["id"],
    "pname": row["name"],
    "price": str(row["price"]),
    "quantity": row["quantity"],
    "created_at": row["created_at"].isoformat(),
}

# innan du returnerar row, row ovanför event ska innehåla row = cur.fetchone() conn.commit()

# Skicka objektet TILL Kafka:
app.state.kafka_producer.send(
    PRODUCTS_TOPIC,         # Address
    key=str(row["id"]),     # Nyckel
    value=event             # Eventet 
)
```
int -> har det att göra med serialisering(serializing). Hur du packar ihop data för att skicka över nätverk.
 
Kafka använder key i key=str(row["id"]) för att bestämma vilken partition som meddelandet ska hamna i.
 
Så är hur information skickas över nätverk och för att kafka inte ska gnälla och skrika på dig.

Det har att göra med serializing och json endocing att göra(?)