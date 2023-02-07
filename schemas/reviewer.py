from pydantic import BaseModel, Field
from typing import Optional 

class Reviewer(BaseModel):
        rev_id : Optional[int] = None
        rev_name: str = Field(max_length=15,min_length=3)
        
        class Config:
            schema_extra = {
                "example":{
                    'rev_name': 'righty sock'
                }
            }

