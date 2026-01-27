# Lecture 2 - Web communication & protocols. Tisdag 27/01-2026
- Hur kommunicerar vi över nätet?

## Moduler för dagen:
- OSI (Bonus)
- TCP/UDP
- HTTP / HTTPS
- local hosts & ports
- Status codes
- Requests & responses
- http methods
- content types
- inspecting elements
------------

- Hur fungerar APIer? (Ta reda på)
  - Från att ha något lokalt på datorn till att nå ut till resten av världen.

- Använda python mot relationsdatabaser och andra datakällor (Pandas är tydligen närmare det och bättre på det(?))  
    - **Note to self: Var försiktig med att säga att pandas är bättre. Det beror på syftet är!**

```text
Databasen (SQL) är alltid snabbare på att filtrera och aggregera data än Pandas, eftersom den gör det nära disken utan att flytta data över nätverket.

Pandas är fantastiskt för komplexa transformationer i minnet som är svåra att skriva i SQL.

Best Practice: Låt SQL göra grovjobbet (filtrera bort 90% av raderna). Läs in de återstående 10% i Pandas för finliret. Att läsa in hela databasen i Pandas för att sen filtrera är ett nybörjarmisstag som sänker prestandan ("Memory Hog").
```

-----------

## OSI (Open System Interconnection BONUS)
- Lager som "förklarar" hur en organisation har fördelat dess tech. 
  - Lager 1-7
    - **Software layer 7-5)**
        - 7: Application (DNS/HTTP, P2P, EMAIL/POP, SMTP, TELENET, FTP). 
        - 6: Presentation recognizing data (HTML, DOC, JPEG, MP3, AVI, Sockets). 
        - 5: Session (Session establishment in TCP, SIP, RTP, ROC-named pipes).
    - **Heart of OSI. Layer 4**
        - 4: Transport (TCP, UDP, SCTP, SSL, TLS) <--- Fokus för dagen(?)
    - **Network layer 3**
        - 3: (IP ARP IPsec, ICMP, IGMP, OSPF)


## Protocol
När man diskuterar 'handskakes' så är det viktigt att förstå hur vi tillämpar uppkopplingar och kommunicerar.
Det finns två väldigt vanliga protokoll, TCP och UDP. 
- **UDP** : User Datagram Protocol
    - UDP är bättre för streaming eller IP-TV / ringa via nätet. Snabbt, effektivt och "spelar" inte allt för stor roll att något paket inte kommer med.

- **TCP** : Transmission **Control** Protocol
    - När du vill ha kontroll och undvika korrupta filer / korrupt data.


## TCP vs UDP (Layer 4) – Varför bryr vi oss?
```text
I Data Engineering är detta skillnaden mellan "Vi får inte tappa en enda rad data" (TCP) och "Vi måste skicka miljoner datapunkter per sekund, strunt samma om vi tappar några" (UDP).

Databases & APIs (Postgres, REST): Alltid TCP. Vi vill ha bekräftelse (ACK) på att data sparats.

Streaming (Ibland): Vissa strömmar kan använda UDP, men moderna köer som Kafka kör oftast över TCP för att garantera leverans.
```    

## Ports and URL.
- Läs:
    - https://www.geeksforgeeks.org/javascript/what-is-url-uniform-resource-locator/ 
    - **(Se bilden på URL strukturen. Med Scheme, Domain name, Port, Path to the file, Query, Parameters och Fragments)**


## Status codes. What are they?
```text
HTTP Status Codes = Din bästa vän för "Fail Fast"

När jag bygger min/en pipeline eller min API senare, tänk på statuskoder som min pipelines trafikljus:
------------------------------------------

100/1xx : Kolla upp statuskoderna för 100


------------------------------------------

200 OK: Allt bra. <- FOKUS
201 Created: <- Kolla upp mer <- FOKUS
204 No Content: <- Kolla upp mer (APIer) <- FOKUS

------------------------------------------
Use when redirecting the client to a different resource or providing multiple choises for the requested resource.

300/3xx : Kolla upp om statuskoderna för 300
300 Multiple choices: <- Kolla upp
301 moved permanently: <- Kolla upp DENNA ÄR FOKUS
304 Not modified: <- Kolla upp

------------------------------------------
Use for client-related errors, such as malformed requests, authentication issues or insuficcient permissions.

4xx (t.ex 400 Bad Request): Felet ligger hos klienten (eller din inkommande data) (Här kommer Pydantic in!!) Om datan är fel -> kasta 422 Unprocessable Entity direkt.

400 Bad request: <- FOKUS
401 Unauthorized:
403 Forbidden:
404 Not found: <- FOKUS

------------------------------------------
5xx (t.ex. 500 Internal Server Error): Felet ligger hos dig. Din kod kraschade.

500 Internal server error: <- FOKUS
502 bad gateway:
503 Service unavailable: 
```

## Web communication (data)

- API logistics, poll results, Data collection. 
    - Vem gör vad?
    - Vad händer bakom kulisserna?

- Server, Request, Client

- Det jag bör hålla koll på:
    - Method, Headers och Protocol version. 

