from models.director import Director as DirectorModels
from schemas.director import Director


class DirectorService():

    def __init__(self, db) -> None:
        self.db = db

    def get_director(self):
        result = self.db.query(DirectorModels).all()
        return result

    # traer la lista de generos por el titulo
    def get_director_first_name(self, first_name: str):
        result = self.db.query(DirectorModels).filter(
            DirectorModels.dir_fname == first_name.capitalize()).all()
        return result
    # Traer la lista de peliculas por id

    def get_movies_for_id(self, id: int):
        result = self.db.query(DirectorModels).filter(DirectorModels.dir_id == id).all()
        return result

    def get_movies_for_last_name(self, last_name: str):
        result = self.db.query(DirectorModels).filter(
            DirectorModels.dir_lname == last_name.capitalize()).all()
        return result

    def create_director(self, director: DirectorModels):
        new_director = DirectorModels(
            dir_fname=director.dir_fname.capitalize(),
            dir_lname =director.dir_lname.capitalize(),
            
        )
        self.db.add(new_director)
        self.db.commit()
        return

    def update_director(self,id:int, director:Director):
        direct = self.db.query(DirectorModels).filter(DirectorModels.dir_id == id).first()
        direct.dir_fname = director.dir_fname.capitalize()
        direct.dir_lname = director.dir_lname.capitalize()
        self.db.commit()
        return

    def delete_director(self, id: int):
        self.db.query(DirectorModels).filter(DirectorModels.dir_id == id).delete()
        self.db.commit()
        return
