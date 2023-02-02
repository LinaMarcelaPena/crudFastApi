from typing import Optional
from pydantic import BaseModel, Field



class MovieCast(BaseModel):
        actor_id: int
        movie_id: int
        role: str = Field(max_length=30,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "actor_id": 1,
                    "movie_id":1,
                    "role":"Part of family"
                }
            }
