from pydantic import BaseModel


# Schema måste matcha API's struktur
class FoxSchema(BaseModel):
    image: str
    link: str