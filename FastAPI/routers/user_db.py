from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client
from bson import ObjectId                       # Importamos ObjectId para poder convertir el id de mongo a string

router = APIRouter(prefix="/userdb",                          # El prefijo de la ruta es /products y se agrega a todas las rutas de este archivo
                   tags= ["userdb"],                      
                   responses ={ status.HTTP_404_NOT_FOUND : {"message":"No encontrado"}})

               
# Entidad User


def buscar_usuario(field :str , key):
    try:
        user = db_client.local.users.find_one({field : key})
        return User(**user_schema(user))
    except:
        return {"error":"El usuario no existe"}

    
def buscar_usuario_por_email(email : str):
    try:
        user = db_client.local.users.find_one({"email" : email})
        return User(**user_schema(user))
    except:
        return {"error":"El usuario ya existe"}


# Buscar por Path

@router.get("/{id}")
async def user(id: str):
    return buscar_usuario("_id", ObjectId(id))

# Buscar por query

@router.get("/")
async def user(id: str):
    return buscar_usuario("_id", ObjectId(id))

    
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)  # status_code = 201 es para que nos devuelva el codigo 201 de que se ha creado correctamente
async def user(user : User):
    
    if type(buscar_usuario("email", user.email)) == User:    #comprobamos si el usuario ya esta en la lista de usuarios
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")       # Si ya esta tiramos un error

    user_dict = dict(user)
    del user_dict["id"]
    
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))    

    return User(**new_user)
        
        
@router.put("/", response_model = User, status_code= status.HTTP_201_CREATED) # status_code = 201 es para que nos devuelva el codigo 201 de que se ha creado correctamente
async def user(user: User):
    
    user_dict = dict(user)
    del user_dict["id"]
    
    try:
        db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        {"error" : "El usuario no existe"}
    
    return buscar_usuario("_id", ObjectId(user.id))

    
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT) # status_code = 204 es para que nos devuelva el codigo 204 de que se ha eliminado correctamente
async def user(id: str):
    
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")       # Si ya esta tiramos un error