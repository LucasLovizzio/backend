from fastapi import FastAPI

app = FastAPI()

@app.get("/")                   #URL local : http://127.0.0.1:8000/
async def root():
    return "Hola FastAPI!"              # Lo que se va a mostrar en la pagina



@app.get("/url")                #URL local : http://127.0.0.1:8000/url/
async def url():
    return {"url" : "https://github.com/LucasLovizzio/apuntes-backend"}   


