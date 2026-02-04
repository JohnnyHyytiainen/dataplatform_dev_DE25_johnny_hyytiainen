from pydantic import BaseModel
from typing import List, Optional
# Schema för min test glossary DB




class GlossaryInput(BaseModel):
    term: str
    definition: str
    category: str
    tags: List[str] = [] # Lista av strings, ["Svårt", "Tenta", "Fokus område"] t.ex