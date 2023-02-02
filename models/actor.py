from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Actor(Base):

    __tablename__ = "actor"

    id = Column(Integer,primary_key = True)
    actor_first_name = Column(String)
    actor_last_name = Column(String)
    actor_gender = Column(String)

    #movie_casts = relationship("MovieCast", back_populates = "actors")




