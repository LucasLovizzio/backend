from fastapi import FastAPI, HTTPException
from routers import products, users, user

app = FastAPI()

# Routers

app.include_router(products.router)
app.include_router(users.router)
app.include_router(user.router)

@app.get("/")                   #URL local : http://127.0.0.1:8000/
async def root():
    return "Hola FastAPI!"              # Lo que se va a mostrar en la pagina



@app.get("/url")                #URL local : http://127.0.0.1:8000/url/
async def url():
    return {"url" : "https://github.com/LucasLovizzio/apuntes-backend"}   


