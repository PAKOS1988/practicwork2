from database.models import Movie
from database import get_db


# Добавление фильма
def add_movie_db(movie_name: str,
                movie_production:str,
                movie_release_year:int,
                movie_genre:str,
                movie_duration:int,
                movie_description:str):
    db = next(get_db())
    add_movie = Movie(movie_name=movie_name,
                      movie_production=movie_production,
                      movie_release_year=movie_release_year,
                      movie_genre=movie_genre,
                      movie_duration=movie_duration,
                      movie_description=movie_description)
    db.add(add_movie)
    db.commit()
    return "Фильм добавлен в библиотеку"


# Удаление фильма
def delete_movie_db(movie_id: int):
    db = next(get_db())
    movie = db.query(Movie).filter_by(movie_id=movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
        return "Фильм удален из библиотеки"
    return "Фильм не найден"

# Информация о фильме
def info_movie_db(movie_id: int):
    db = next(get_db())
    movie = db.query(Movie).filter_by(movie_id=movie_id).first()
    if movie:
        return movie
    else:
        movie = None
        return movie

