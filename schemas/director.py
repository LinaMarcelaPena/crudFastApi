from pydantic import BaseModel, Field
from typing import Optional 

class Director(BaseModel):
        dir_id: Optional[int] = None
        dir_fname: str = Field(max_length=30,min_length=3)
        dir_lname: str = Field(max_length=30,min_length=3)
        
        class Config:
            schema_extra = {
                "example":{
                    'dir_fname': 'Claire',
                    'dir_lname': "Denis",
                }
            }

