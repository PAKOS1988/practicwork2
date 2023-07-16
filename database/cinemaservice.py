from database.models import Cinema, Hall
from database import get_db

def add_cinema_db(cinema_name:str,
                  cinema_location:str,
                  cinema_contact:str,
                  cinema_star:int):
    db = next(get_db())
    add_cinema = Cinema(cinema_name = cinema_name,
                        cinema_location = cinema_location,
                        cinema_contact = cinema_contact,
                        cinema_star = cinema_star)
    db.add(add_cinema)
    db.commit()
    return "Кинотеатр добавлен"

def add_hall_db(hall_class: str,
                cinema_id:int,
                hall_number_of_seats: int,
                hall_price:float):
    db = next(get_db())
    add_hall = Hall(hall_class=hall_class,
                    cinema_id=cinema_id,
                    hall_number_of_seats=hall_number_of_seats,
                    hall_price=hall_price)
    db.add(add_hall)
    db.commit()

    return "Зал успешно добавлен"


