#importar las clases necearias para poder utilizarlas
from typing import List
from fastapi import APIRouter, HTTPException, status
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
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No hay generos registradas")
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@genres_router.get('/genres_for_title',tags=['genres'],status_code=200)
def get_genres_for_title(gen_title:str):
    db = Session()
    result = GenresService(db).get_generes_for_title(gen_title)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran peliculas con el titulo "+ str(gen_title))
    return JSONResponse(content=jsonable_encoder(result),status_code=status.HTTP_200_OK)

@genres_router.get('/genres_for_id',tags=['genres'],status_code=200)
def get_genres_for_id(id:int):
    db = Session()
    result = GenresService(db).get_generes_for_id(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran peliculas con el id "+ str(id))
    return JSONResponse(content=jsonable_encoder(result),status_code=status.HTTP_200_OK)


#CREATE crear
@genres_router.post('/genres',tags=['genres'],status_code=status.HTTP_200_OK,response_model=dict)
#funcion que recibe parametros verificados por Shemas
def post_genres(genre:Genres):
    #conecta a la base de datos
    db = Session()
    #va a servicio y ejecuta la funcion create_genres y envia una respuesta
    GenresService(db).create_genres(genre)
    #Si la respuesta es positiva mostrara un mensaje y status 200 ok que todo salio bien
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "Se ha registrado el genero"})

@genres_router.put('/genres{id}',tags=['genres'])
def put_genre(id:int,genre:Genres):
    db =  Session()
    result: GenresModel = db.query(GenresModel).filter(GenresModel.id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    GenresService(db).put_genre(id,genre)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Se ha modificado el genero con id:"+ str(id)})

@genres_router.delete('/genres/{id}', tags=['genres'], status_code=status.HTTP_200_OK)
def delete_genres(id: int):
    db = Session()
    result: GenresModel = db.query(GenresModel).filter(GenresModel.id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    GenresService(db).delete_genres(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado el genero con id:"+ str(id)})
    
    
