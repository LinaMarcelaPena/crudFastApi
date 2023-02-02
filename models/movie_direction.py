from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class MovieDirection(Base):

    __tablename__ = "movie_direction"


    dir_id = Column(Integer, ForeignKey("director.dir_id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
