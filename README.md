# CERSEU-FISI-API

Este es el api que se usará en el proyecto CERSEU para el curso Diseño de Software

## Estructura del código

### db/models

En esta carpeta se declaran clases que representan a las tablas de la base de datos

### schemas

Similar a models pero se usa para modelar el uso que se tendrá de los models. Por ejemplo, al momento de ingresar o enviar datos

### api/routes

En esta carpeta se declaran las rutas (endpoints) del api para cada Model (tabla)
https://www.fastapitutorial.com/blog/post-request-fastapi/

### db/repository

En esta carpeta va la lógica que se usa en los api/routes

## Tipos de endpoint

- **GET**: Obtener/leer información de la bd https://www.fastapitutorial.com/blog/fastapi-get-requests/
- **POST**: Insertar información en la bd
  https://www.fastapitutorial.com/blog/post-request-fastapi/
- **DELETE**: Eliminar información de la bd https://www.fastapitutorial.com/blog/delete-request-fastapi/
- **UPDATE/PATCH**: Actualizar información de la bd  
  **Nota**: En el caso de update es un poco más complejo con fastapi. Para entender bien cómo funciona recomiendo leer https://sqlmodel.tiangolo.com/tutorial/fastapi/update/ y https://www.fastapitutorial.com/blog/update-put-request-fastapi/

  ### Páginas recomendadas para leer

- https://fastapi.tiangolo.com/tutorial/first-steps/
- https://fastapi.tiangolo.com/tutorial/sql-databases/
