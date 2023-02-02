from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from models.moviecast import MovieCast
from config.database import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(Integer,primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    time = Column(Float)
    date_release = Column(String)
    release_contry = Column(String)

    #movie_casts = relationship("MovieCast", back_populates = "movies")





    