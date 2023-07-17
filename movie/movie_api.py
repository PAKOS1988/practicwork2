from main import app
from database.movieservice import add_movie_db, delete_movie_db, info_movie_db
from datetime import datetime


# Добавление фильма
@app.post('/add_movie')
async def add_movie_api(movie_name: str,
                        movie_production:str,
                        movie_release_year:int,
                        movie_genre:str,
                        movie_duration:int,
                        movie_description:str):
    result = add_movie_db(movie_name=movie_name,
                          movie_production=movie_production,
                          movie_release_year=movie_release_year,
                          movie_genre=movie_genre,
                          movie_duration=movie_duration,
                          movie_description=movie_description)


    return {"status": 1, "message": result}

# Удаление фильма
@app.post('/delete_movie')
async def del_movie_api(movie_id:int):
    result = delete_movie_db(movie_id=movie_id)
    return {"status": 1, "message": result}

@app.post('/about_movie')
async def info_movie_api(movie_id:int):
    result = info_movie_db(movie_id=movie_id)
    return {"status": 1, "message": result}