from typing import List
from fastapi import APIRouter, HTTPException, status


from config.database import Session
from service.reviewer import Reviewer as ReviewerService
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.reviewer import Reviewer
from models.reviewer import Reviewer as ReviewerModels


reviewer_router = APIRouter()



# READ leer registros
@reviewer_router.get('/revewer', tags=['Reviewer'],status_code=200)
#funcion
def get_reviewer():
    #conexion a la base de datos 
    db= Session()
    #Conectar a la base de datos y traer el resultado de la funcion creada en el servicio  
    result = ReviewerService(db).get_reviewer()
    # respuesta de la base de datos en formato JSON
    #al ser correcta la peticion GET para recuperar los datos en este caso la lista de generos 
    # nos dara un codigo de status 200 que nos indica que la respuesta es positiva, OK, correcta
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No hay generos registradas")
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)



@reviewer_router.get('/reviewer_name', tags=['Reviewer'], status_code=200)
def get_reviewer_for_name(name: str):
    db = Session()
    result = ReviewerService(db).get_reviewer_for_name(name)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran revisores con el nombre "+ str(name))
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@reviewer_router.get('/reviewer_id', tags=['Reviewer'], status_code=200)
def get_reviewer_for_id(id: int):
    db = Session()
    result = ReviewerService(db).get_reviewer_for_id(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No registran revisores con el id "+ str(id))
    return JSONResponse(content=jsonable_encoder(result), status_code=200)




@reviewer_router.post('/reviewer', tags=['Reviewer'], status_code=200)
def create_reviewer(reviewer: Reviewer):
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "Se ha registrado el revisor"})
    

@reviewer_router.put('/reviewer{id}',tags=['Reviewer'])
def update_reviewer(id:int,reviewer:Reviewer):
    db =  Session()
    result: ReviewerModels = db.query(ReviewerModels).filter(ReviewerModels.rev_id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    ReviewerModels(db).update_reviewer(id,reviewer)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Se ha modificado el revisor con id:"+ str(id)})


@reviewer_router.delete('/reviewer/{id}', tags=['Reviewer'], status_code=200)
def delete_reviewer(id: int):
    db = Session()
    result: ReviewerModels = db.query(ReviewerModels).filter(ReviewerModels.rev_id == id)
    final = result.first()
    if not final:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El id "+ str(id)+" no existe")
    ReviewerService(db).delete_reviewer(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado el revisor con id:"+ str(id)})
    
    
