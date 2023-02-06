from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    # traer la lista de generos por el titulo
    def get_movies_for_title(self, title: str):
        result = self.db.query(MovieModel).filter(
            MovieModel.title == title.capitalize()).all()
        return result
    # Traer la lista de peliculas por id

    def get_movies_for_id(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).all()
        return result

    def get_movies_for_country(self, contry: str):
        result = self.db.query(MovieModel).filter(
            MovieModel.release_contry == contry.capitalize()).all()
        return result

    def create_movie(self, movie: MovieModel):
        new_movie = MovieModel(
            title=movie.title.capitalize(),
            overview=movie.overview,
            year=movie.year,
            time=movie.time,
            date_release=movie.date_release,
            release_contry=movie.release_contry.capitalize()
        )
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self,id:int, data:Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return

    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return
