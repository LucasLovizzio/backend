from fastapi import FastAPI
from routers import products, users, user
from fastapi.staticfiles import StaticFiles    # modulo para añadir recursos estaticos
app = FastAPI()

# Routers

app.include_router(products.router)
app.include_router(users.router)
app.include_router(user.router)

# Recursos estaticos

app.mount("/static", StaticFiles(directory="static"),name="static") # añadimos la carpeta static como recurso estatico, el StaticFiles es el modulo que nos permite hacerlo, el directory es la carpeta que queremos añadir y el name es el nombre que le damos a la carpeta

@app.get("/")                   #URL local : http://127.0.0.1:8000/
async def root():
    return "Hola FastAPI!"              # Lo que se va a mostrar en la pagina


@app.get("/url")                #URL local : http://127.0.0.1:8000/url/
async def url():
    return {"url" : "https://github.com/LucasLovizzio/apuntes-backend"}   


