# Weather Logger - Learn by Building

## Goal
Hämta Stockholms väder från API, spara i SQLite databas, bygg enkel analys.

## Why This Project?
- Combines HTTP requests (new skill)
- Combines database work (YrkesCo skill)
- Concrete problem (relatable!)
- Portfolio-worthy

## Tech Stack
- Python (you know this)
- httpx (you used this)
- SQLite (you used this in Space Bridge)
- Open-Meteo API (free, no key needed)

## Steps

### 1. Fetch Weather Data
```python
import httpx

def get_stockholm_weather():
    """Hämta Stockholms väder just nu."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,   # Stockholm
        "longitude": 18.07,
        "current_weather": "true"
    }
    
    with httpx.Client() as client:
        response = client.get(url, params=params)
        response.raise_for_status()
        return response.json()

# Test it!
data = get_stockholm_weather()
print(data)
```

### 2. Create Database Schema
```python
import sqlite3

def create_database():
    """Skapa databas och tabell för väderdata."""
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            windspeed REAL NOT NULL,
            weather_code INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

# Test it!
create_database()
print("Database created!")
```

### 3. Save Weather to Database
```python
import sqlite3
from datetime import datetime

def save_weather(weather_data):
    """Spara väderdata till databas."""
    current = weather_data["current_weather"]
    
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO weather_logs (timestamp, temperature, windspeed, weather_code)
        VALUES (?, ?, ?, ?)
    """, (
        current["time"],
        current["temperature"],
        current["windspeed"],
        current["weathercode"]
    ))
    
    conn.commit()
    conn.close()
    print(f"Saved weather at {current['time']}: {current['temperature']}°C")

# Test it!
weather = get_stockholm_weather()
save_weather(weather)
```

### 4. Complete Script (Put It All Together)
```python
import httpx
import sqlite3
from datetime import datetime
import time

def get_stockholm_weather():
    """Hämta Stockholms väder."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,
        "longitude": 18.07,
        "current_weather": "true"
    }
    
    with httpx.Client() as client:
        response = client.get(url, params=params)
        response.raise_for_status()
        return response.json()

def create_database():
    """Skapa databas."""
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            windspeed REAL NOT NULL,
            weather_code INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

def save_weather(weather_data):
    """Spara väder till databas."""
    current = weather_data["current_weather"]
    
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO weather_logs (timestamp, temperature, windspeed, weather_code)
        VALUES (?, ?, ?, ?)
    """, (
        current["time"],
        current["temperature"],
        current["windspeed"],
        current["weathercode"]
    ))
    
    conn.commit()
    conn.close()
    print(f"✅ Saved: {current['temperature']}°C at {current['time']}")

def main():
    """Main function - kör weather logger."""
    print("=== Weather Logger Starting ===")
    
    # Setup database
    create_database()
    print("✅ Database ready")
    
    # Fetch and save weather every 5 minutes (for testing, use shorter interval)
    try:
        while True:
            weather = get_stockholm_weather()
            save_weather(weather)
            print("Sleeping 5 minutes...")
            time.sleep(300)  # 300 seconds = 5 minutes
    except KeyboardInterrupt:
        print("\n=== Weather Logger Stopped ===")

if __name__ == "__main__":
    main()
```

## What You're Learning (Hidden Lessons)

### HTTP Requests
- ✅ GET with query parameters
- ✅ Error handling
- ✅ JSON parsing

### Database Operations
- ✅ CREATE TABLE (schema design)
- ✅ INSERT data (ETL load step)
- ✅ Connection management

### Data Pipeline
- ✅ Extract (API call)
- ✅ Transform (parse JSON)
- ✅ Load (save to DB)

### This is a MINI DATA PLATFORM!
- Data Ingestion Layer: API calls
- Data Storage Layer: SQLite
- Data Processing: Parse & validate
- Orchestration: While loop (basic!)

## Extensions (When Basic Works)

### Level 2: Add Analysis
```python
def analyze_weather():
    """Visa statistik från väderloggar."""
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    # Average temperature
    cursor.execute("SELECT AVG(temperature) FROM weather_logs")
    avg_temp = cursor.fetchone()[0]
    
    # Max windspeed
    cursor.execute("SELECT MAX(windspeed) FROM weather_logs")
    max_wind = cursor.fetchone()[0]
    
    # Count logs
    cursor.execute("SELECT COUNT(*) FROM weather_logs")
    count = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"\n=== Weather Statistics ===")
    print(f"Total logs: {count}")
    print(f"Average temp: {avg_temp:.1f}°C")
    print(f"Max windspeed: {max_wind:.1f} km/h")
```

### Level 3: Add Error Handling
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_weather_safe(weather_data):
    """Spara väder med error handling."""
    try:
        current = weather_data["current_weather"]
        
        # Validate data
        if current["temperature"] < -50 or current["temperature"] > 50:
            logger.warning(f"Suspicious temperature: {current['temperature']}")
        
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO weather_logs (timestamp, temperature, windspeed, weather_code)
            VALUES (?, ?, ?, ?)
        """, (
            current["time"],
            current["temperature"],
            current["windspeed"],
            current["weathercode"]
        ))
        
        conn.commit()
        conn.close()
        logger.info(f"Saved: {current['temperature']}°C")
        
    except KeyError as e:
        logger.error(f"Missing field in weather data: {e}")
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
```

## How This Connects to Course

### You Just Built:
- ✅ Data Ingestion (API calls)
- ✅ Data Storage (SQLite)
- ✅ ETL Pipeline (Extract-Transform-Load)
- ✅ Basic Orchestration (while loop)

### What's Next in Course (Probably):
- Message Queues (instead of while loop)
- Workflow Orchestration (Airflow instead of while)
- Real-time Streaming (Kafka instead of polling)
- Cloud Deployment (AWS/Azure instead of local)

### Your Foundation:
You understand the CORE concepts now:
1. Fetch data from source (HTTP)
2. Process/validate (Python)
3. Store somewhere (Database)
4. Repeat (Orchestration)

Everything else is just SCALING these concepts!

## Next Steps

1. Build this project (1-2h)
2. Let it run for a few hours (collect data)
3. Add analysis queries
4. Try extending it (new features)
5. THEN go back to slides (theory will make sense now!)

## Key Insight

> "You don't learn data platforms by reading about them.
> You learn by BUILDING one (even a tiny one)."

This project IS a data platform. Just very small.
