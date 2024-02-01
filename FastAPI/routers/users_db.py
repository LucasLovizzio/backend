from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import users_schema
from db.client import db_client

router = APIRouter(prefix="/usersdb",                          # El prefijo de la ruta es /products y se agrega a todas las rutas de este archivo
                   tags= ["usersdb"],                      
                   responses ={ 404 : {"message":"No encontrado"}})
                   
@router.get("/", response_model=list[User], status_code= status.HTTP_200_OK)
async def users():
    return users_schema(db_client.users.find())
