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

    - **DATA LINK LAYER 2** 
        - 
    - **PHYSICAL LAYER 1**
        -   

### Protocol?
När man diskuterar 'handskakes' så är det viktigt att förstå hur vi tillämpar uppkopplingar och kommunicerar.
Det finns två väldigt vanliga protokoll, TCP och UDP. 
- **UDP** : User Datagram Protocol
    - UDP är bättre för streaming eller IP-TV / ringa via nätet. Snabbt, effektivt och "spelar" inte allt för stor roll att något paket inte kommer med.

- **TCP** : Transmission **Control** Protocol
    - När du vill ha kontroll och undvika korrupta filer / korrupt data.

    


