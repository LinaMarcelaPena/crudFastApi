from ast import List
from fastapi import APIRouter, HTTPException, status
from config.database import Session
from service.movie_director import MovieDirectorService 
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


Movdirector_router = APIRouter()



@Movdirector_router.get('/MovDirector', tags=['Movie Director'])
def get_director() :
    db = Session()
    result = MovieDirectorService(db).get_director()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No hay peliculas registradas")
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
