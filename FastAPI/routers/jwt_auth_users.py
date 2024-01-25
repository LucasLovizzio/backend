from fastapi import APIRouter, Depends , HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext                # contexto de encriptacion
from datetime import datetime, timedelta


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 
SECRET = "4da3f5c3b8bfdc3c7cff595387f0153d38436540a164ec503bf67fe1b192f0b3"  # openssl rand -hex 32 (correr en terminal para el secret)

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

crypt = CryptContext(schemes=["bcrypt"])

# Users classes
class User(BaseModel):          # User de Red
    username : str
    full_name: str
    email: str
    disabled : bool
    
class UserDB(User):        # User de Base de datos
    password : str 

#base de datos de usuarios
users_db = {
    
    "lucaslovizzio": {
        
        "username" : "lucaslovizzio",
        "full_name" : "Lucas Lovizzio",
        "email": "llovizzio@gmail.com",
        "disabled" : False,
        "password": "$2a$12$uVKzAn45htMNi.tkHdhbt.YMk.ikW4RiYnT7obldZoaBIwqYvzGGO",
    },
    "arielvilche": {
        
        "username" : "arielvilche",
        "full_name" : "Ariel Vilche",
        "email": "arielvilche@gmail.com",
        "disabled" : True,
        "password": "$2a$12$2JuxK70nv2ZzlYMNOazjb.ECPdBtBHO5he3G6nuGEDMrWfj5NDyBO",
    }
}


def search_user_db(username : str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username : str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token : str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED ,
            detail= "Credenciales de autenticacion invalidas",
            headers={"WWW-Authenticate" : "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError : 
        raise exception
    
    return search_user(username)
    
    

async def current_user(user : User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Usuario inactivo")
    return user
    

@router.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST , detail= "El usuario no es correcto")
        
    user = search_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):      # si la contraseña no coincide con la contraseña encriptada: 
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    access_token = {"sub" : user.username,
                    "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    

    return {"access_token": jwt.encode(access_token, SECRET , algorithm=ALGORITHM) ,"token_type": "bearer"}

@router.get("/users/me")
async def me(user : User = Depends(current_user)):
    return user