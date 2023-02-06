import statistics
from telnetlib import STATUS
from fastapi import APIRouter, HTTPException, Path, Query, Depends,  status
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.movie import Movie as MovieModel
from service.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


# @app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> Movie:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies_for_title', tags=['movies'], status_code=200)
def get_movies_for_title(title: str):
    db = Session()
    result = MovieService(db).get_movies_for_title(title)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies_for_id', tags=['movies'], status_code=200)
def get_movies_for_id(id: int):
    db = Session()
    result = MovieService(db).get_movies_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies_for_country', tags=['movies'], status_code=200)
def get_movies_for_country(country: str):
    db = Session()
    result = MovieService(db).get_movies_for_country(country)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post('/movies', tags=['movies'], status_code=200, response_model=dict)
def create_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la pelicula", "status_code": 200})


@movie_router.put('/movies{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    db =  Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id)
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id:"+ str(id)})


@movie_router.delete('/movies/{id}', tags=['movies'], status_code=200)
def delete_movie(id: int):
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item not found")
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película con id:"+ str(id)})


    
