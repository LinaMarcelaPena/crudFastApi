from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor
from config.database import Session
from service.actor import ActorService

#como se va a llamar desde main
actor_router = APIRouter()

@actor_router.get('/actors',tags=['actors'], response_model=Actor, status_code= 200)
def get_actor() ->Actor:   
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@actor_router.post('/actors', tags=['actors'], status_code=201 , response_model=dict)
def create_actor(actor:Actor) ->dict:
    db= Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={'message':'actor save in data base'})

