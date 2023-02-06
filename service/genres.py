
#importo el modelo de genres para poder usarlo aqui en el servicio le asigno el nombre de GenresModel que es 
#el que voy a usar para llamar al servicio
from models.genres import Genres as GenresModel

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
# traer la lista de generos por el titulo 
    def get_generes_for_title(self,genre_title:str):
        result = self.db.query(GenresModel).filter(GenresModel.gen_title == genre_title.capitalize()).all()
        return result
# Traer la lista de peliculas por id        
    def get_generes_for_id(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).all()
        return result    

#funcion para crear generos 
    def create_genres(self, genres:GenresModel):
        new_genres = GenresModel(
            id = genres.id,
            gen_title = genres.gen_title.capitalize()
        )   
        #agregar genero
        self.db.add(new_genres)
        #siempre que refresca hace commit
        self.db.commit()
        return

