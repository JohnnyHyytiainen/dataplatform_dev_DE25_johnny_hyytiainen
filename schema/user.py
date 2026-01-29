from pydantic import BaseModel

class UserSchema():
    username: str
    password: str

    