# API Parameters Guide - Johnny's Learning Notes

## Problem Du Hade:

```
❌ Försökte hitta parameters i själva API:n
   https://api.open-meteo.com/v1/forecast/get
   
   Result: {"reason": "Not Found","error": true}
```

**Varför det inte fungerade:**
- API:er har INTE endpoints som `/get` för att visa parameters
- Parameters finns i DOCUMENTATION (på website, inte i API:n själv)

---

## Lösningen: Läs API Documentation

### ✅ Rätt Plats: https://open-meteo.com/en/docs

---

## Hur API Parameters Fungerar (Real Example):

### Open-Meteo Weather API:

**Base URL:**
```
https://api.open-meteo.com/v1/forecast
```

**Parameters Du MÅSTE ha:**
- `latitude` - Geographic coordinate (required)
- `longitude` - Geographic coordinate (required)

**Parameters Du KAN ha (optional):**
- `current_weather` - Get current conditions (true/false)
- `hourly` - Weather variables by hour (comma-separated list)
- `daily` - Weather variables by day (comma-separated list)
- `temperature_unit` - celsius or fahrenheit
- `timezone` - Time zone (e.g., "Europe/Stockholm")
- Plus MÅNGA fler (se documentation!)

---

## Everyday Analogy (Restaurant Order):

### API Request = Beställa Mat

**Base URL** = Restaurangens adress
```
https://pizzeria.com/order
```

**Required Parameters** = Måste specificera
```
?customer=Johnny    ← Vem beställer?
&table=5            ← Vilket bord?
```

**Optional Parameters** = Kan specificera
```
&pizza=Margherita   ← Vad vill du ha?
&size=large         ← Stor eller liten?
&extra=cheese       ← Extra ost?
```

**Full Request:**
```
https://pizzeria.com/order?customer=Johnny&table=5&pizza=Margherita&size=large&extra=cheese
```

---

## Real Open-Meteo Example:

### MINIMAL Request (bara required):

```python
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.33,
    "longitude": 18.07
}
```

**Detta funkar!** Men du får VÄLDIGT mycket data (allt forecast API kan ge).

---

### SMART Request (specify vad du vill ha):

```python
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.33,          # Stockholm lat
    "longitude": 18.07,         # Stockholm long
    "current_weather": True     # Bara nuvarande väder (inte 7-dagars forecast)
}
```

**Detta ger dig mindre data = snabbare, enklare att processa!**

---

### ADVANCED Request (många parameters):

```python
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "hourly": "temperature_2m,precipitation,windspeed_10m",  # Timvis data
    "daily": "temperature_2m_max,temperature_2m_min",        # Daglig data
    "timezone": "Europe/Stockholm",                          # Svensk tid
    "forecast_days": 3                                       # Bara 3 dagar
}
```

---

## Hur Hittar Man Vilka Parameters Som Finns?

### 1. Gå till Documentation Website:
```
https://open-meteo.com/en/docs
```

### 2. Scrolla Ner Till "API Documentation" Section

### 3. Se Tabellen (från documentation):

| Parameter | Format | Required | Default | Description |
|-----------|--------|----------|---------|-------------|
| latitude | Float | YES | - | Geographic coordinate |
| longitude | Float | YES | - | Geographic coordinate |
| current_weather | String | NO | - | Get current weather |
| hourly | String array | NO | - | Hourly weather variables |
| daily | String array | NO | - | Daily weather variables |
| temperature_unit | String | NO | celsius | celsius or fahrenheit |
| timezone | String | NO | GMT | Timezone name |

**"Required = YES" = Du MÅSTE ha detta**
**"Required = NO" = Du KAN ha detta (optional)**

---

## Din Original Script Explained:

```python
import httpx

def get_stockholm_weather():
    """Get Stockholms current weather."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,      # REQUIRED parameter
        "longitude": 18.07,     # REQUIRED parameter
        "current_weather": True # OPTIONAL parameter (men vi vill ha den!)
    }

    with httpx.Client() as client:
        response = client.get(url, params=params)
        response.raise_for_status()  # Throw error if status != 200
        return response.json()
    
if __name__ == "__main__":
    weather = get_stockholm_weather()
    print(f"Stockholm right now: {weather['current_weather']['temperature']}°C")
```

### Vad Händer Bakom Kulisserna:

**httpx gör:**
```python
# httpx tar params dict och bygger URL:
base = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 59.33, "longitude": 18.07, "current_weather": True}

# Blir:
final_url = "https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current_weather=true"

# Skickar HTTP GET request
# Får tillbaka JSON response
```

**Du kan testa själv i browser:**
```
https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current_weather=true
```

Öppna den URL:en i din browser → se JSON response!

---

## Varför Du INTE Behöver Alla Parameters:

### API har TYP 50+ possible parameters!

Men du behöver bara:
- **Required:** latitude, longitude
- **Optional:** Vad du faktiskt vill ha

**Example: Olika Use Cases**

### Use Case 1: Bara Nuvarande Temp
```python
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "current_weather": True
}
```

### Use Case 2: 7-Dagars Forecast
```python
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"
}
```

### Use Case 3: Timvis Data För Idag
```python
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "hourly": "temperature_2m,precipitation",
    "forecast_days": 1  # Bara idag
}
```

---

## JSON Response Structure:

### Vad Du Får Tillbaka (current_weather):

```json
{
  "latitude": 59.33,
  "longitude": 18.07,
  "elevation": 28.0,
  "current_weather": {
    "time": "2026-02-01T14:00",
    "temperature": -3.5,
    "windspeed": 12.0,
    "winddirection": 245,
    "weathercode": 3
  }
}
```

**Därför fungerar:**
```python
weather['current_weather']['temperature']
                 ↑                ↑
            Key level 1      Key level 2
```

---

## Postman Usage (Hur Man Testar):

### Step 1: Öppna Postman

### Step 2: New Request
- Method: GET
- URL: `https://api.open-meteo.com/v1/forecast`

### Step 3: Add Query Parameters (Params tab)
| Key | Value |
|-----|-------|
| latitude | 59.33 |
| longitude | 18.07 |
| current_weather | true |

### Step 4: Send Request

### Step 5: Se JSON Response i Body

**Detta är samma som:**
```python
response = httpx.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 59.33, "longitude": 18.07, "current_weather": True}
)
```

---

## httpx.get() vs Manual URL Building:

### ❌ Manual (du behöver inte göra detta):
```python
url = "https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07&current_weather=true"
response = httpx.get(url)
```

### ✅ Med params (cleanare, enklare):
```python
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 59.33, "longitude": 18.07, "current_weather": True}
response = httpx.get(url, params=params)
```

**httpx hanterar URL-encoding, special characters, etc!**

---

## Varför response.json() Fungerar Utan json Import:

```python
import httpx  # httpx HAR redan JSON parser built-in!

response = httpx.get(url, params=params)
data = response.json()  # ← httpx method (ej Python's json.load!)
```

**Detta är samma som:**
```python
import httpx
import json

response = httpx.get(url, params=params)
data = json.loads(response.text)  # Manual JSON parsing
```

**Men httpx.json() är enklare och säkrare!**

---

## raise_for_status() Explained:

```python
response = client.get(url, params=params)
response.raise_for_status()  # ← Vad gör denna?
```

### Vad Den Gör:

**IF** status code är 4xx or 5xx (error):
→ Throw HTTPStatusError exception

**IF** status code är 2xx (success):
→ Do nothing (continue execution)

### Example:

```python
# API finns inte (404)
response = client.get("https://api.open-meteo.com/v1/does-not-exist")
response.raise_for_status()
# ← Throws: httpx.HTTPStatusError: Client error '404 Not Found'
```

```python
# API funkar (200)
response = client.get("https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.07")
response.raise_for_status()
# ← Nothing happens, code continues
```

### Jämfört Med Manual Check:

```python
# Manual (vad du skrev tidigare)
if response.status_code != 200:
    raise Exception(f"Error: {response.status_code}")

# raise_for_status (samma resultat, mindre kod)
response.raise_for_status()
```

---

## Key Takeaways:

### 1. Parameters finns i DOCUMENTATION (inte i API:n)
→ Läs https://open-meteo.com/en/docs

### 2. Du behöver INTE alla parameters
→ Bara required + vad du faktiskt vill ha

### 3. httpx bygger URL:en åt dig
→ Du behöver bara ge `params` dict

### 4. response.json() är built-in i httpx
→ No need för `import json`

### 5. raise_for_status() = auto error checking
→ Cleaner än manual if-check

---

## Practice Exercise:

### Try This Yourself:

```python
import httpx

# EXERCISE 1: Get Stockholm weather för nästa 3 dagar
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "daily": "temperature_2m_max,temperature_2m_min",  # Max/min temp
    "forecast_days": 3,  # Bara 3 dagar
    "timezone": "Europe/Stockholm"  # Svensk tid
}

with httpx.Client() as client:
    response = client.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    print("3-dagars forecast:")
    for i, date in enumerate(data['daily']['time']):
        max_temp = data['daily']['temperature_2m_max'][i]
        min_temp = data['daily']['temperature_2m_min'][i]
        print(f"{date}: {min_temp}°C - {max_temp}°C")
```

**Output Example:**
```
3-dagars forecast:
2026-02-01: -5.2°C - -2.1°C
2026-02-02: -4.8°C - -1.5°C
2026-02-03: -3.2°C - 0.5°C
```

---

## When In Doubt:

1. **Read the docs:** https://open-meteo.com/en/docs
2. **Test in Postman:** See what response looks like
3. **Test in browser:** Paste URL, see JSON
4. **Copy example code:** Most APIs have examples
5. **Ask Claude:** "Hur använder jag X parameter med Y API?"

---

## Next Step (För Weather Logger):

Nu när du förstår parameters → Build weather logger!

You know:
- ✅ How to find parameters (documentation)
- ✅ How to use params dict (httpx)
- ✅ How to parse JSON response
- ✅ How to handle errors (raise_for_status)

**Du är redo att bygga!** 🚀
