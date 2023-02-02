from typing import Optional
from pydantic import BaseModel, Field


class Actor(BaseModel):
        id: Optional[int] = None
        actor_first_name: str = Field(max_length=15,min_length=3)
        actor_last_name: str = Field(max_length=15,min_length=3)
        actor_gender: str = Field(max_length=15,min_length=1)

        class Config:
            schema_extra = {
                "example":{
                    "actor_first_name": "Vin",
                    "actor_last_name":"Diesel",
                    "actor_gender":"M"
                }
            }
