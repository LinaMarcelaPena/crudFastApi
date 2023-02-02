from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Director(Base):

# nombre de tabla
    __tablename__ = "director"

#atributos
    dir_id = Column(Integer, primary_key=True, index=True)
    dir_fname = Column(String)
    dir_lname = Column(String)