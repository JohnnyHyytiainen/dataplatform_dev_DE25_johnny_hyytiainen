# Catchup övning. Ett fetch python script efter datamod labben.

import httpx  # httpx == det biblioteket jag installerade tidigare
import json  # jsonfile


def fetch_user():
    url = "https://jsonplaceholder.typicode.com/users"

    print(f"___1. Förbereder request mot {url} (TCP connection)___")

    # med httpx.client gör en GET
    # Använd with för att starta och sen stänga connection.
    with httpx.Client() as client:
        response = client.get(url)

        print(f"___2. Fick svar!!! Statuskod: {response.status_code}___")

        # allt annat än statuskod 200 = fail direkt. Gör om och gör rätt.
        if response.status_code != 200:
            raise Exception(f"något gick fel. Servern sa {response.status_code}")

        # konverterar rå text till dict (json parsing)
        data = response.json()

        print(f"___3. Hittade: {len(data)} användare ___")

        # Visar min FÖRSTA användare pga index 0 = 1
        first_user = data[0]
        print("\nExempeldata (JSON):")
        print(json.dumps(first_user, indent=2))

        return data


if __name__ == "__main__":
    users = fetch_user()
