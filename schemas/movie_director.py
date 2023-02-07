from pydantic import BaseModel, Field
from typing import Optional 
from models.movie_direction import MovieDirection
from models.movie import Movie
from models.director import Director

class MovieDirector():
        dir_id: Director.dir_id
        movie_id: Movie.id
        

        class Config:
            schema_extra = {
                "example":{
                    'dir_id': Director.dir_id,
                    'movie_id': Movie.id,
                }
            }

