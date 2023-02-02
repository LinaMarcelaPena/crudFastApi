#importar las clases necearias para poder utilizarlas
from ast import List
from fastapi import APIRouter
from config.database import Session
from models.genres import Genre as GenresModel
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from schemas.genres import Genres
#llamo al servicio
from service.genres import GenresService

# como se va a llamar en mi clase principal main donde inicia la app
genres_router = APIRouter()


# READ leer registros
@genres_router.get('/genres', tags=['genres'],status_code=200)
#funcion
def get_genres():
    #conexion a la base de datos 
    db= Session()
    #Conectar a la base de datos y traer el resultado de la funcion creada en el servicio  
    result = GenresService(db).get_genres()
    # respuesta de la base de datos en formato JSON
    #al ser correcta la peticion GET para recuperar los datos en este caso la lista de generos 
    # nos dara un codigo de status 200 que nos indica que la respuesta es positiva, OK, correcta
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



