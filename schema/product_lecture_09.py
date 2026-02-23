from pydantic import BaseModel, Field


# Field definierar attributerna som name, price och quantity ska innehålla.
class ProductSchema(BaseModel):
    name: str = Field(
        min_length=2, max_length=69, description="Name must be between 2-69 characters"
    )
    price: float = Field(gt=0, description="Price MUST be greater than 0")

    quantity: int = Field(
        gt=0, lt=50, description="Must choose 1 or more, maximum of 50"
    )
    sku: str = Field(pattern=r"^SKU-\d{4}$", description="Format must be SKU-0000")

    # sku: Använder sig av RegEX. ^ tyder på att vi förväntar oss någonting som börjar på ^SKU-
    # Sedan är det \d som egentligen betyder [0-9]. Alltså att vi förväntar oss ett heltal mellan 0 och 9
    # {4} betyder att det är antalet siffror som börjar på 0-9
    # $ betyder end. 
    