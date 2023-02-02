
#importo el modelo de genres para poder usarlo aqui en el servicio le asigno el nombre de GenresModel que es 
#el que voy a usar para llamar al servicio
from models.genres import Genre as GenresModel

#nombre de la clase del servicio / en esta parte se realizan las conexiones a la base de datos  
class GenresService ():
    #constructor de la clase GenresService  con la palabra reservada __init__
    def __init__(self,db) -> None:
        self.db = db

# funcion que trae toda la lista de generos 
    def get_genres(self):
        # se realiza conexion a la base de datos y se envia una consulta al modelo
        result = self.db.query(GenresModel).all() 
        return result

    

     