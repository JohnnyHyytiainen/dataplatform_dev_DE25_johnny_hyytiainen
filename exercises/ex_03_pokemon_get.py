import httpx
from pydantic import BaseModel
from exersice_schema.ex_03_pokemon_schema import PokemonSchema

# EJ DRY PRINCIPEN. Hårdkodar mina pokemon jag vill ha. Nästa övning v2 == tom lista som jag itererar över

# Exercise 3. GET namn + "base_experience"
# + mappa till en pydantic modell
# https://pokeapi.co/api/v2/

def get_pokemon(pokemon_name: str):
    """
    Funktion för att hämta och hitta rätt pokemon.
    Använder mig av objekt i exercise_schema med den datan jag vill få ut
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    print(f"Knock knock, anybody home? {url}")
    with httpx.Client(timeout=10.0) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
        pokemon_obj = PokemonSchema(**data) # **data == dictionary unpacking
        return pokemon_obj
    
if __name__ == "__main__":
    try: 
        squirt = get_pokemon("squirtle")
        print(f"Caught: {squirt.name.capitalize()}, med base EXP: {squirt.base_experience}")
        print(f"Pokedéx ID: {squirt.id}, och ordning: {squirt.order}")
        print(f"Vikt: {squirt.weight}hekton, och längd: {squirt.height} decimeter")

        char = get_pokemon("charmander")
        print(f"Caught: {char.name.capitalize()}, med base EXP: {char.base_experience}")
        print(f"Pokedéx ID: {char.id}, och ordning: {char.order}")
        print(f"Vikt: {char.weight}hekton, och längd: {char.height} decimeter")

        bulb = get_pokemon("bulbasaur")
        print(f"Caught: {bulb.name.capitalize()}, med base EXP: {bulb.base_experience}")
        print(f"Pokedéx ID: {bulb.id}, och ordning: {bulb.order}")
        print(f"Vikt: {bulb.weight}hekton, och längd: {bulb.height} decimeter")


    except httpx.HTTPStatusError as e:
        print(f"HTTP-fel: {e.response.status_code} för {e.request.url}")
    except Exception as e:
        print(f"övrigt fel: {e}")
