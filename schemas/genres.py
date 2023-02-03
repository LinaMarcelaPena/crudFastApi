#archivos que nos dicen como debe ser la informacion que recibimos 
from typing import Optional
from pydantic import BaseModel, Field


class Genres(BaseModel):
    #se colocan los datos requeridos en la tabla genres y sus caracteristicas
        id: Optional[int] = None
        #un titulo de tipo String maximo de 15 caracteres y minimo de 3 
        gen_title: str = Field(max_length=15,min_length=3)
        
        #se realiza una configuracion de verficacion para validar si los dato ingresados son los correctoos
        class Config:
            schema_extra = {
                "example":{
                    "id":"1",
                    "gen_title": "Action"
                }
            }
