from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_cast import MovieCast
from models.moviecast import MovieCast as MovieCastModel
from service.movie_cast import MovieCastService


movie_cast_router = APIRouter()


@movie_cast_router.get('/movie/{id_movie}/cast/', tags=['cast'],response_model=list[MovieCast],status_code=200)
def get_movie_cast(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieCastService(db).get_movie_cast(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_cast_router.post('/cast', tags=['cast'],response_model=dict,status_code=201)
def create_cast(cast:MovieCast)->dict:
    db = Session()
    MovieCastService(db).create_movie_cast(cast)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})
