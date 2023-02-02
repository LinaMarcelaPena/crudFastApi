from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

from config.database import Base

class MoviesGenres(Base):

    __tablename__ = "movie_genres"

    movie_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer,ForeignKey("genres"))

    