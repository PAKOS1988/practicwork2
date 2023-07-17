from main import app
from database import add_hall_db, add_cinema_db, add_session_db
from datetime import datetime
from datetime import timedelta

# Добавление кинотеатра в БД
@app.post('/add_cinema')
async def add_cinema_api(cinema_name:str,
                         cinema_location:str,
                         cinema_contact:str,
                         cinema_star:int,
                         cinema_card_number:int,
                         cinema_balance:int):
    result = add_cinema_db(cinema_name = cinema_name,
                           cinema_location = cinema_location,
                           cinema_contact = cinema_contact,
                           cinema_star = cinema_star,
                           cinema_card_number = cinema_card_number,
                           cinema_balance = cinema_balance)

    return {"status": 1, "message": result}

# Добавление зала в кинотеатры в БД
@app.post('/add_hall')
async def add_hall_api(hall_class: str,
                       cinema_id:int,
                       hall_number_of_seats: int,
                       hall_price:float):
    result = add_hall_db(hall_class=hall_class,
                         cinema_id=cinema_id,
                         hall_number_of_seats=hall_number_of_seats,
                         hall_price=hall_price)

    return {"status": 1, "message": result}


@app.post('/add_session')
async def add_session_api(movie_id: int,
                          cinema_id: int,
                          hall_id: int,
                          session_datetime:datetime):
    result = add_session_db(movie_id = movie_id,
                           cinema_id = cinema_id,
                           hall_id = hall_id,
                           session_datetime = session_datetime)

    return {"status": 1, "message": result}
