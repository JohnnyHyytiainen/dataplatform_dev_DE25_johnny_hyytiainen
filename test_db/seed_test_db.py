# Seed skript för min test glossary databas.

import requests
import json
import time

# URL till mitt API 
API_URL = "http://127.0.0.1:8000/glossary"

# steg 1: läs in min JSON fil jag skapat i root för att seeda.
def seed():
    try:
        with open("seed_test_db.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Hittade ingen seed_test_db.json fil! Se över pathing.")
        return
    
    print(f"hittade {len(data)} termer. Laddar upp till DB via API")

    # Steg 2: iterera och fyll på.
    for item in data:
        try: 
            response = requests.post(API_URL, json=item)

            if response.status_code == 200:
                print(f"Sparade: {item['term']}")
            else:
                print(f"Fel vid {item['term']}: {response.text}")


        except Exception as e:
            print(f"Connection error: {e}")
            print(f"Är servern igång?")
            break

        # en paus för att vara snäll och se loggarna. Liten delay
        time.sleep(0.2)

    print("KLART!")

if __name__ == "__main__":
    seed()
    


        