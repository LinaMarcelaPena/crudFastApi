from ast import List
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from config.database import Session
from fastapi.responses import JSONResponse
from schemas.director import Director 
from service.director import DirectorService
from models.director import Director as DirectorModels

director_router = APIRouter()



@director_router.get('/director', tags=['director'], status_code=status.HTTP_200_OK)
def get_director() -> Director:
    db = Session()
    result = DirectorService(db).get_director()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No hay directores registrados")
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@director_router.get('/director_first_name', tags=['director'], status_code=status.HTTP_200_OK)
def get_director_first_name(first_name: str):
    db = Session()
    result = DirectorService(db).get_director_first_name(first_name)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran directores con el nombre "+ str(first_name))
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@director_router.get('/director_for_id', tags=['director'], status_code=status.HTTP_200_OK)
def get_movies_for_id(id: int):
    db = Session()
    result = DirectorService(db).get_movies_for_id(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran directores con el id "+ str(id))
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@director_router.get('/director_for_last_name', tags=['director'], status_code=status.HTTP_200_OK)
def get_movies_for_last_name(last_name: str):
    db = Session()
    result = DirectorService(db).get_movies_for_last_name(last_name)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran directores con el apellido "+ str(last_name))
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
    

@director_router.post('/director', tags=['director'], status_code=200, response_model=dict)
def create_director(director:Director):
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "Se ha registrado el director"})

@director_router.put('/director{id}',tags=['director'])
def update_director(id:int,director:Director):
    db =  Session()
    result: DirectorModels = db.query(DirectorModels).filter(DirectorModels.dir_id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    DirectorService(db).update_director(id,director)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Se ha modificado el director con id:"+ str(id)})


@director_router.delete('/director/{id}', tags=['director'], status_code=200)
def delete_director(id: int):
    db = Session()
    result: DirectorModels = db.query(DirectorModels).filter(DirectorModels.dir_id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    DirectorService(db).delete_director(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado el director con id:"+ str(id)})
    
    