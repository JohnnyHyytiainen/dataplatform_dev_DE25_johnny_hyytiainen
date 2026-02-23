# mini-cheatsheet


```text 
Curl på Windows (viktigt!)

I Git Bash är curl oftast riktig curl.

I PowerShell kan curl vara alias för Invoke-WebRequest. Kör då curl.exe för att vara säker.
``` 
```text
curl URL -> gör GET

curl -i URL -> visar status + headers

curl -o data/raw/x.json URL -> sparar svaret till fil

curl -L URL -> följer redirects
```
```text
HTTP Verb   Motsvarighet i SQL          Vad det gör
GET             SELECT	                Hämta data. (Säkert att köra 100 ggr).
POST	        INSERT	                Skapa ny data. (Kör du den 2 ggr får du dubbletter).
PUT	            UPDATE	                Ersätt data helt.
DELETE	        DELETE	                Ta bort data.
```