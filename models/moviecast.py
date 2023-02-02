from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.actor import Actor


class MovieCast(Base):

    __tablename__ = "movie_cast"

    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("actor.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    role = Column(String)


    # movies = relationship("Movie", back_populates = "movies_casts")    
    # actors = relationship("Actor",back_populates = "movie_casts")
