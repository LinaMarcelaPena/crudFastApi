from typing import Optional
from pydantic import BaseModel, Field


class Genres(BaseModel):
        id: Optional[int] = None
        gen_title: str = Field(max_length=15,min_length=3)
        

        class Config:
            schema_extra = {
                "example":{
                    "gen_title": "Action"
                }
            }
