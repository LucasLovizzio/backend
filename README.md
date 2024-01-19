
# Apuntes Backend

Backend focalizado en Python, utilizando Fast API.

Aparte de todo esto tambien hay apuntes de MongoDB y MongoDB Atlas.






## Type Hint

Python 3.6+ tiene soporte para "type hints" opcionales.

Estos type hints son una nueva sintaxis, desde Python 3.6+, que permite declarar el tipo de una variable.

Usando las declaraciones de tipos para tus variables, los editores y otras herramientas pueden proveerte un soporte mejor.

Todo FastAPI está basado en estos type hints, lo que le da muchas ventajas y beneficios.

Pero, así nunca uses FastAPI te beneficiarás de aprender un poco sobre los type hints.

Ejemplo:

```bash
  def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

Llamar este programa nos muestra el siguiente output:

```bash
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

```first_name, last_name```

cambiaremos a lo siguiente:

```first_name: str, last_name: str```

Añadir los type hints normalmente no cambia lo que sucedería si ellos no estuviesen presentes.

Pero ahora imagina que nuevamente estás creando la función, pero con los type hints.

En el mismo punto intentas iniciar el `auto-completado` con `Ctrl+Space` y ves:

![](https://fastapi.tiangolo.com/img/python-types/image02.png)

Ahora podes buscar la funcion que desees y utilizarla.

## Type Hints en FastAPI

FastAPI aprovecha estos type hints para hacer varias cosas.

Con FastAPI declaras los parámetros con type hints y obtienes:

* *Soporte en el editor*
* *Type checks*.

...y FastAPI usa las mismas declaraciones para:

* *Definir requerimientos*: desde request path parameters, query parameters, headers, bodies, dependencies, etc.
* *Convertir datos: desde el request al tipo requerido.*
* *Validar datos*: viniendo de cada request:
  * Generando errores automáticos devueltos al cliente cuando los datos son inválidos.
* *Documentar la API usando OpenAPI*:
    * que en su caso es usada por las interfaces de usuario de la documentación automática e interactiva.
## Authors
- [@LucasLovizzio](https://github.com/LucasLovizzio)



## Documentation

[Video de Youtube de MoreDev](https://www.youtube.com/watch?v=_y9qQZXE24A&t)

[Fast API](https://fastapi.tiangolo.com)


    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

Llamar este programa nos muestra el siguiente output:

```bash
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

```first_name, last_name```

cambiaremos a lo siguiente:

```first_name: str, last_name: str```

Añadir los type hints normalmente no cambia lo que sucedería si ellos no estuviesen presentes.

Pero ahora imagina que nuevamente estás creando la función, pero con los type hints.

En el mismo punto intentas iniciar el `auto-completado` con `Ctrl+Space` y ves:

![](https://fastapi.tiangolo.com/img/python-types/image02.png)

Ahora podes buscar la funcion que desees y utilizarla.

## Authors

- [@LucasLovizzio](https://github.com/LucasLovizzio)



## Documentation

[Video de Youtube de MoreDev](https://www.youtube.com/watch?v=_y9qQZXE24A&t)

[Fast API](https://fastapi.tiangolo.com)



