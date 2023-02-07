
from models.director import Director as DirModels
from models.movie import Movie as MovieModels


class MovieDirectorService():

    def __init__(self, db) -> None:
        self.db = db

    def get_director(self):
        result = self.db.query(DirModels.dir_id)
        return result
