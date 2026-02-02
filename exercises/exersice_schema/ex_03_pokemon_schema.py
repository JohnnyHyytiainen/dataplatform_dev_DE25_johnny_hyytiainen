from pydantic import BaseModel

# Schema för exercise 03, pokemon GET.
# 1) Bestäm vad du vill spara ifrån API't.
# API't ger tillbaka massor av data(json) men jag vill enbart ha viss data.

# Skapa en klass med de parametrar jag vill ha.

class PokemonSchema(BaseModel):
    name: str
    base_experience: int
    id: int
    height: int
    weight: int
