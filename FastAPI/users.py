from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

#  iniciar el server: uvicorn usersjson:app --reload

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
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Lucas", "surname": "Lovizzio", "age" : 19},
            {"name":"Brais", "surname": "Moure", "age" : 35},
            {"name":"Moure", "surname": "Dev", "age" : 31}]
    
@app.get("/users")
async def users():
    return users_list

# Buscar por Path

@app.get("/user/{id}")
async def user(id: int):
    return buscar_usuario(id)

# Buscar por query

@app.get("/user/")
async def user(id: int):
    return buscar_usuario(id)

""" # añadir un nuevo usuario

@app.post("/user/")
async def user(user : User):
    users_list.append(user)    # agregamos el usuario a la lista de usuarios """
    
@app.post("/user/", status_code = 201)
async def user(user: User):
    if type(buscar_usuario(user.id)) == User:    #comprobamos si el usuario ya esta en la lista de usuarios
        raise HTTPException(status_code=204, detail="El usuario ya existe")       # Si ya esta tiramos un error     # Si ya esta tiramos un error
    else:
        users_list.append(user)                                 # si no esta lo agregamos
        return user
        
        
@app.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, usuario_guardado in enumerate(users_list):
        if usuario_guardado.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error" : "No se ha encontrado el usuario"}
    else:
        return user
    
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    
    for index, usuario_guardado in enumerate(users_list):
        if usuario_guardado.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error" : "No se ha encontrado el usuario"}
    else:
        return {"message" : "Usuario eliminado correctamente"}