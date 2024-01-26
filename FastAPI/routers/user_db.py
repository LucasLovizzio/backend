from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/userdb",                          # El prefijo de la ruta es /products y se agrega a todas las rutas de este archivo
                   tags= ["userdb"],                      
                   responses ={ 404 : {"message":"No encontrado"}})
                   
# Entidad User

class User(BaseModel):
    id : int
    name: str
    surname: str
    age: int

def buscar_usuario(id : int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

users_list = [User(id = 1, name="Lucas", surname="Lovizzio",age=19),
              User(id = 2, name="Brais", surname="Moure", age=35),
              User(id = 3, name="Ariel", surname="Vilche",age=40)]

# Buscar por Path

""" @router.get("/{id}")
async def user(id: int):
    return buscar_usuario(id)
 """
# Buscar por query

@router.get("/")
async def user(id: int):
    return buscar_usuario(id)

""" # añadir un nuevo usuario

@router.post("/")
async def user(user : User):
    users_list.append(user)    # agregamos el usuario a la lista de usuarios """
    
@router.post("/", status_code = 201)  # status_code = 201 es para que nos devuelva el codigo 201 de que se ha creado correctamente
async def user(user: User):
    if type(buscar_usuario(user.id)) == User:    #comprobamos si el usuario ya esta en la lista de usuarios
        raise HTTPException(status_code=204, detail="El usuario ya existe")       # Si ya esta tiramos un error     # Si ya esta tiramos un error
    else:
        users_list.append(user)                                 # si no esta lo agregamos
        return user
        
        
@router.put("/", status_code= 201) # status_code = 201 es para que nos devuelva el codigo 201 de que se ha creado correctamente
async def user(user: User):
    for index, usuario_guardado in enumerate(users_list):
        if usuario_guardado.id == user.id:
            users_list[index] = user
            return user
        else:
            raise HTTPException(status_code=404, detail="El usuario no existe")
            
    
@router.delete("/{id}", status_code = 204) # status_code = 204 es para que nos devuelva el codigo 204 de que se ha eliminado correctamente
async def user(id: int):
    for index, usuario_guardado in enumerate(users_list):
        if usuario_guardado.id == id:
            del users_list[index]
        else:
            raise HTTPException(status_code=404, detail="El usuario no existe")
   