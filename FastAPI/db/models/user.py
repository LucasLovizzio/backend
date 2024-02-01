from pydantic import BaseModel

class User(BaseModel):
    id : str = None           # el ID que pone MongoDB por default es un str
    username: str
    email: str
    