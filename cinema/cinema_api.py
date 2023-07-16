from main import app
from database import add_hall_db, add_cinema_db

# Добавление кинотеатра в БД
@app.post('/add_cinema')
async def add_cinema_api(cinema_name:str,
                         cinema_location:str,
                         cinema_contact:str,
                         cinema_star:int):
    result = add_cinema_db(cinema_name = cinema_name,
                           cinema_location = cinema_location,
                           cinema_contact = cinema_contact,
                           cinema_star = cinema_star)

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
