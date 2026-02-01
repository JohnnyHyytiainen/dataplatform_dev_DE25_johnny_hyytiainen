import httpx
from pydantic import BaseModel
from exersice_schema.ex_04_pokemon_schema import PokemonSchema

# Exercise 4. GET method, nested Json.
# + mappa till en pydantic modell
# https://pokeapi.co/api/v2/


def get_pokemon(pokemon_name: str):
    """
    Funktion för att hämta och hitta rätt pokemon.
    Använder mig av objekt i exercise_schema med den datan jag vill få ut
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    print(f"\nResponse from: {url}\n")
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
        pokemon_obj = PokemonSchema(**data)  # **data == dictionary unpacking
        return pokemon_obj


if __name__ == "__main__":
    try:
        my_team = ["pikachu", "gengar", "mewtwo"]
        for i, pokemon_name in enumerate(my_team):
            team = get_pokemon(pokemon_name)
            first_type = team.types[0].type.name
            print(
                f"Pokémon name: {pokemon_name.capitalize()}.\n{pokemon_name.capitalize()} is a: {first_type.capitalize()} Pokémon."
            )

    except Exception as e:
        print(f"Någonting gick fel, felkod: {e}")
