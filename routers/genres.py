#importar las clases necearias para poder utilizarlas
from ast import List
from fastapi import APIRouter
from config.database import Session
from models.genres import Genres as GenresModel
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

@genres_router.get('/genres_for_title',tags=['genres'],status_code=200)
def get_genres_for_title(gen_title:str):
    db = Session()
    result = GenresService(db).get_generes_for_title(gen_title)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.get('/genres_for_id',tags=['genres'],status_code=200)
def get_genres_for_id(id:int):
    db = Session()
    result = GenresService(db).get_generes_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


#CREATE crear
@genres_router.post('/genres',tags=['genres'],status_code=200)
#funcion que recibe parametros verificados por Shemas
def post_genres(genre:Genres):
    #conecta a la base de datos
    db = Session()
    #va a servicio y ejecuta la funcion create_genres y envia una respuesta
    GenresService(db).create_genres(genre)
    #Si la respuesta es positiva mostrara un mensaje y status 200 ok que todo salio bien
    return JSONResponse(content={'message':'Register genrer correctly','status_code':'200'})

