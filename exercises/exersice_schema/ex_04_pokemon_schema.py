from pydantic import BaseModel
from typing import List


# Schema för exercise 04, pokemon GET.
# NESTED JSON
# Börja bygga nerifrån upp.
# API't ger tillbaka massor av data(json) men jag vill enbart ha viss data.

# Skapa en klass med de parametrar jag vill ha.


# Nivå 3 - Botten
# Ska motsvara "type": {"name": "electric"... ...}
class PokemonTypeDetail(BaseModel):
    name: str
    url: str

# Nivå 2 - Mitten
# Ska motsvara objektet i listan
class PokemonTypeEntry(BaseModel):
    slot: int
    type: PokemonTypeDetail # REF ||--|| PokemonTypeDetail objektet från nivå 3.

# Nivå 1 - Toppen
class PokemonSchema(BaseModel):
    name: str
    base_experience: int
    id: int
    height: int
    weight: int 
    order: int
    types: List[PokemonTypeEntry] # REF ||--|| PokemonTypeEntry objektet från nivå 2.