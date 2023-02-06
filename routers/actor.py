from fastapi import APIRouter, HTTPException, Path, Query, Depends, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor
from config.database import Session
from service.actor import ActorService
from models.actor import Actor as ActorModels

# como se va a llamar desde main
actor_router = APIRouter()


@actor_router.get('/actors', tags=['actors'], response_model=Actor, status_code=status.HTTP_200_OK)
def get_actor() -> Actor:
    db = Session()
    result = ActorService(db).get_actors()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay actores registrados")
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@actor_router.get('/actors_for_first_name', tags=['actors'], status_code=status.HTTP_200_OK)
def get_actors_first_name(first: str):
    db = Session()
    result = ActorService(db).get_actors_first_name(first)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No registran actores con el nombre " + str(first))
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@actor_router.get('/actors_for_id', tags=['actors'], status_code=200)
def get_actors_for_id(id: int):
    db = Session()
    result = ActorService(db).get_actors_for_id(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No registran actores con el id " + str(id))
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@actor_router.get('/actors_for_last_name', tags=['actors'], status_code=200)
def get_actors_for_last_name(last: str):
    db = Session()
    result = ActorService(db).get_actors_for_last_name(last)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No registran actores con el apellido " + str(last))
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@actor_router.post('/actors', tags=['actors'], status_code=200, response_model=dict)
def create_actor(actor: Actor):
    db = Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha registrado el actor"})


@actor_router.put('/actors{id}', tags=['actors'])
def update_actor(id: int, actor: Actor):
    db = Session()
    result: ActorModels = db.query(ActorModels).filter(ActorModels.id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El id " + str(id)+" no existe")
    ActorService(db).update_actor(id, actor)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha modificado el actor con id:" + str(id)})


@actor_router.delete('/actors/{id}', tags=['actors'], status_code=200)
def delete_actor(id: int):
    db = Session()
    result: ActorModels = db.query(ActorModels).filter(ActorModels.id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El id " + str(id)+" no existe")
    ActorService(db).delete_actor(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado el actor con id:" + str(id)})
