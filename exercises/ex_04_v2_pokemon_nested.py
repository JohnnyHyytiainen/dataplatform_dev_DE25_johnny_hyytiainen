import httpx
from pydantic import BaseModel
from exersice_schema.ex_04_pokemon_schema import PokemonSchema

# Exercise 4 v2 GET method, nested Json.
# + få ut rätt värde för pokemon med DUBBEL 'Type' (List comprehension)
# + mappa till en pydantic modell
# https://pokeapi.co/api/v2/


def get_pokemon(pokemon_name: str) -> PokemonSchema:
    """
    Funktion för att hämta och hitta rätt pokemon.
    Använder mig av objekt i exercise_schema med den datan jag vill få ut
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    print(f"\nResponse from: {url}\n")
    with httpx.Client(timeout=10.0) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
        pokemon_obj = PokemonSchema(**data)  # **data == dictionary unpacking
        return pokemon_obj


if __name__ == "__main__":
    try:
        my_team = ["gengar", "mewtwo", "snorlax", "jynx", "lugia"]
        for i, pokemon_name in enumerate(my_team):
            team = get_pokemon(pokemon_name)
            # 1. Loopa igenom 'team.types'
            # 2. För varje 't' (entry), plocka ut 't.type.name'
            # 3. Skapa en ny lista av strängar: ["ghost", "poison"]
            first_type = team.types[0].type.name
            type_names = [t.type.name for t in team.types]
            type_string = " & ".join(type_names)
            print(
                f"Pokémon name: {pokemon_name.capitalize()}.\n{pokemon_name.capitalize()} is a: {type_string} Pokémon."
            )

    except httpx.HTTPStatusError as e:
        print(f"HTTP-fel: {e.response.status_code} för {e.request.url}")
    except Exception as e:
        print(f"övrigt fel: {e}")