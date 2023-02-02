from sqlalchemy import Column, Integer, String

from config.database import Base

class Genre(Base):


    #nombre de la tabla
     __tablename__ = "genres"

     #campos de la tabla genres segun modelo de la base de datos
     #llave primaria o identificador
     id = Column(Integer, primary_key=True, index=True)
     #titulo
     gen_title = Column(String)
      