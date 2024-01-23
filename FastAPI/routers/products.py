from fastapi import APIRouter


router = APIRouter(prefix="/products",                          # El prefijo de la ruta es /products y se agrega a todas las rutas de este archivo
                   tags= "products",                      
                   responses ={ 404 : {"message":"No encontrado"}})

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")                   
async def root():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/{id}")                   
async def root(id : int):
    return products_list[id]