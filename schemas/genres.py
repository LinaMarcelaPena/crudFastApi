#archivos que nos dicen como debe ser la informacion que recibimos 
from typing import Optional
from pydantic import BaseModel, Field


class Genres(BaseModel):
    #se colocan los campos de la tabla genres y su tipo de dato
        id: Optional[int] = None
        #un titulo de tipo String maximo de 15 caracteres y minimo de 3 
        gen_title: str = Field(max_length=15,min_length=3)
        
        #se realiza una configuracion de verficacion para validar si 
        # los datos ingresados son los correctos esto nos permite realizar una prueba
        class Config:
            schema_extra = {
                "example":{
                    "gen_title": "Action"
                }
            }
