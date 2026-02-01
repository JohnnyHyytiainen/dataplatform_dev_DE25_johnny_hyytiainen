import httpx
from pydantic import BaseModel
from exersice_schema.ex_03_pokemon_schema import PokemonSchema


# Exercise 3 v2. Gå från hardcoded pokemon till lista jag enkelt kan fylla i med olika pokemon och iterera över
# + mappa till en pydantic modell
# https://pokeapi.co/api/v2/

def get_pokemon(pokemon_name: str):
    """
    Funktion för att hämta och hitta rätt pokemon.
    Använder mig av objekt i exercise_schema med den datan jag vill få ut
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    print(f"\n Response from: {url} \n")
    with httpx.Client(timeout=10.0) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
        pokemon_obj = PokemonSchema(**data) # **data == dictionary unpacking
        return pokemon_obj
    
if __name__ == "__main__":
    try: 
        my_team = ["pikachu", "gengar", "snorlax", "mewtwo", "mew"]
        for i, pokemon_name in enumerate(my_team):
            team = get_pokemon(pokemon_name)
            print(f"{team}")

    except httpx.HTTPStatusError as e:
        print(f"HTTP-fel: {e.response.status_code} för {e.request.url}")
    except Exception as e:
        print(f"övrigt fel: {e}")
