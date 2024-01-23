from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",                          # El prefijo de la ruta es /products y se agrega a todas las rutas de este archivo
                   tags= ["users"],                      
                   responses ={ 404 : {"message":"No encontrado"}})
                   
# Entidad User

class User(BaseModel):
    id : int
    name: str
    surname: str
    age: int

users_list = [User(id = 1, name="Lucas", surname="Lovizzio",age=19),
              User(id = 2, name="Brais", surname="Moure", age=35),
              User(id = 3, name="Ariel", surname="Vilche",age=40)]
@router.get("json")
async def usersjson():
    return [{"name":"Lucas", "surname": "Lovizzio", "age" : 19},
            {"name":"Brais", "surname": "Moure", "age" : 35},
            {"name":"Moure", "surname": "Dev", "age" : 31}]
    
@router.get("/")
async def users():
    return users_list
