
# Apuntes Backend

Backend focalizado en Python, utilizando Fast API.

Aparte de todo esto también hay apuntes de MongoDB y MongoDB Atlas.
## Type Hint

Python 3.6+ tiene soporte para "type hints" opcionales.

Estos type hints son una nueva sintaxis, desde Python 3.6+, que permite declarar el tipo de una variable.

Usando las declaraciones de tipos para tus variables, los editores y otras herramientas pueden proveerte un soporte mejor.

Todo FastAPI está basado en estos type hints, lo que le da muchas ventajas y beneficios.

Pero, así nunca uses FastAPI te beneficiarás de aprender un poco sobre los type hints.

Ejemplo:

```python
  def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

Llamar este programa nos muestra el siguiente output:

```python
John Doe
```

Es un programa muy simple.

Ahora, imagina que lo estás escribiendo desde ceros.

En algún punto habrías comenzado con la definición de la función, tenías los parámetros listos...

Pero, luego tienes que llamar "ese método que convierte la primera letra en una mayúscula".

Era `upper?` O era `uppercase?` `first_uppercase?` `capitalize?`

Luego lo intentas con el viejo amigo de los programadores, el auto-completado del editor.

Escribes el primer parámetro de la función `first_name`, luego un punto `(.)` y luego presionas `Ctrl+Space` para iniciar el auto-completado.

Tristemente, no obtienes nada útil:

![](https://fastapi.tiangolo.com/img/python-types/image01.png)

### Añadir Type hints

Vamos a modificar los primeros parametros de la funcion.
En lugar de:

```python
first_name, last_name
```

cambiaremos a lo siguiente:

```python
first_name: str, last_name: str
```

Añadir los type hints normalmente no cambia lo que sucedería si ellos no estuviesen presentes.

Pero ahora imagina que nuevamente estás creando la función, pero con los type hints.

En el mismo punto intentas iniciar el `auto-completado` con `Ctrl+Space` y ves:

![](https://fastapi.tiangolo.com/img/python-types/image02.png)

Ahora podes buscar la función que desees y utilizarla.

### Type Hints en FastAPI

FastAPI aprovecha estos *type hints* para hacer varias cosas.

Con **FastAPI** declaras los parámetros con *type hints* y obtienes:

* **Soporte en el editor**
* **Type checks**.

...y **FastAPI** usa las mismas declaraciones para:

* **Definir requerimientos**: desde request path parameters, query parameters, headers, bodies, dependencies, etc.
* **Convertir datos:** desde el request al tipo requerido.
* **Validar datos**: viniendo de cada request:
  * Generando errores automáticos devueltos al cliente cuando los datos son inválidos.
* **Documentar la API usando OpenAPI**:
    * que en su caso es usada por las interfaces de usuario de la documentación automática e interactiva.

## Creación de la API

A la hora de crear una API, se utilizan métodos HTTP como: 

* POST
* GET
* PUT
* DELETE

...y otros mas exóticos como:

* OPTIONS
* HEAD
* PATCH
* TRACE

Normalmente usas uno de estos métodos específicos de HTTP para realizar una acción específica.

* POST: para crear datos.
* GET : para leer datos.
* PUT : para actualizar datos.
* DELETE : para borrar datos.

## Primeros Pasos

Archivo `main.py` con la función básica y url raíz `("/")` :
### Raiz

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

otro ejemplo ahora con la url `("/url")`

```python
@app.get("/url")                #URL local : http://127.0.0.1:8000/url/

async def url():

    return {"url" : "https://github.com/LucasLovizzio/apuntes-backend"}
```

### Parametros de Path

Supongamos que tenemos usuarios guardados, pero no en `main.py` :

![[users.png]]

esta vez los guardaremos en `users.py` , por lo tanto lo mas básico seria tener los usuarios con sus **metadatos** guardados en una `List()`  :

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):

    id : int
    name: str
    surname: str
    age: int

users_list = [User(id = 1, name="Lucas", surname="Lovizzio",age=19),
              User(id = 2, name="Brais", surname="Moure", age=35),
              User(id = 3, name="Ariel", surname="Vilche",age=40)]

@app.get("/users")
async def users():
    return users_list
```

`Basemodel` es una librería que nos permite crear una clase sin tener que hacer el constructor que seria de la siguiente forma:

```python
class Persona:
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age
		
	# Podemos agregar funciones adicionales (getters)
```

Si buscamos por el `{id}` de la persona : 

```python
@app.get("/user/{id}")
async def user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
```

Siempre que el usuario sea el que ponga un dato que puede no estar hay que evitar los posibles errores que se puedan ocurrir con `try` y `except`. 

Esta llamada por `{id}` la cual se realiza desde la `url` se los llama parametros por `path`.
El valor del parámetro de path `id` será pasado a tu función como el argumento `id`.

### Parámetros de Query

Cuando declaras otros parámetros de la función que no hacen parte de los parámetros de path estos se interpretan automáticamente como parámetros de "query".

El query es el conjunto de pares de key-value que van después del `?` en la URL, separados por caracteres `&`.

Por ejemplo, en la URL:

```
http://127.0.0.1:8000/user/?id=1
```
resultado:
```json
{"id":1,"name":"Lucas","surname":"Lovizzio","age":19}
```
### Documentación de nuestra API

Documentación con Swagger: http://127.0.0.1:8000/docs
Documentación con Redocly: http://127.0.0.1:8000/redoc

## POST - PUT - DELETE

POST

```python
@app.post("/user/")

async def user(user: User):

    if type(buscar_usuario(user.id)) == User:         #comprobamos si el usuario ya esta en la lista de usuarios

        return {"error":"No se ha encontrado el usuario"}       # Si ya esta tiramos un error

    else:

        users_list.append(user)                             # si no esta lo agregamos

        return user
```

PUT

```python
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
```

DELETE

```python
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
```

## Codigos de estado HTTP

[HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
[Fast API - Response status code](https://fastapi.tiangolo.com/es/tutorial/response-status-code/#response-status-code)
## Routers

Al crear una API, rara vez ponemos todo en un archivo:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

ya sea por legibilidad o porque queremos dividirlo de mejor manera. Para esto utilizaremos los `routers` .

### API Router

Digamos que el archivo dedicado a manejar solo usuarios es el submódulo en `/app/routers/users.py`.

Desea tener las _operaciones de ruta_ relacionadas con sus usuarios separadas del resto del código, para mantenerlo organizado.

Pero sigue siendo parte de la misma aplicación **FastAPI** / API web (es parte del mismo "Paquete Python").

Puede crear las _operaciones de ruta_ para ese módulo usando `APIRouter`.

### Importar API Router

Lo importas y creas una instancia de la misma manera que lo harías con la clase `FastAPI`:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
```

Se usa de la misma manera que usabas la clase `FastAPI` para acceder a `app` 

Una vez configurados los routers, los importamos  en el archivo `main.py` de la siguiente manera: 

```python
from routers import users
```

Si necesitamos agregar otros, simplemente, los importamos de la misma forma:

```python
from routers import products, users, user
```

Para que funcione con nuestra `app` que tenemos en `main.py` usamos la función `include_router(modulo.router)`. En este caso lo haremos de la siguiente manera:

```python
app.include_router(products.router)
app.include_router(users.router)
app.include_router(user.router)
```

## Recursos estáticos

* Importar modulo `StaticFiles`
* "Montar" una instancia de `StaticFiles` en un `path` especifico. 

Suponiendo que tenemos la siguiente ruta: 

![[Pasted image 20240124000544.png]]

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

La primera `"/static"`se refiere a la subruta en la que se "montará" esta "aplicación". Por lo tanto, cualquier `path` que comience `"/static"`será manejado por él.

`directory="static"`: se refiere al nombre del directorio que contiene sus archivos estáticos.

`name="static"` : le da un nombre que **FastAPI**  puede utilizar internamente .

Todos estos parámetros pueden ser diferentes a " `static`", ajústelos con las necesidades y detalles específicos de su propia aplicación.

## Authors
- [@LucasLovizzio](https://github.com/LucasLovizzio)

## Documentation

[Video de Youtube de MoreDev](https://www.youtube.com/watch?v=_y9qQZXE24A&t)

[Fast API](https://fastapi.tiangolo.com)

[HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

