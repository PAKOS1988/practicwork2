from database.models import Cinema, Hall
from database import get_db

def add_cinema_db(cinema_name:str,
                  cinema_location:str,
                  cinema_contact:str,
                  cinema_star:int,
                  cinema_card_number:int,
                  cinema_balance:int):
    db = next(get_db())
    add_cinema = Cinema(cinema_name = cinema_name,
                        cinema_location = cinema_location,
                        cinema_contact = cinema_contact,
                        cinema_star = cinema_star,
                        cinema_card_number = cinema_card_number,
                        cinema_balance = cinema_balance)
    db.add(add_cinema)
    db.commit()
    return "Кинотеатр добавлен"

def add_hall_db(hall_class: str,
                cinema_id:int,
                hall_number_of_seats: int,
                hall_price:float):
    db = next(get_db())
    cheker_cinema_id = db.query(Cinema).filter_by(cinema_id=cinema_id).first()
    if cheker_cinema_id:
        add_hall = Hall(hall_class=hall_class,
                        cinema_id=cinema_id,
                        hall_number_of_seats=hall_number_of_seats,
                        hall_price=hall_price)
        db.add(add_hall)
        db.commit()

        return "Зал успешно добавлен"
    return "Вы ввели неверный ID кинотеатра"

def delete_cinema_db(cinema_id: int):
    db = next(get_db())
    cinema = db.query(Cinema).filter_by(cinema_id=cinema_id).first()
    if cinema:
        db.delete(cinema)
        db.commit()
        return "Кинотеатр успешно удален"
    else:
        return "Кинотеатр не найден"


def delete_hall_db(hall_id: int):
    db = next(get_db())
    hall = db.query(Hall).filter_by(hall_id=hall_id).first()
    if hall:
        db.delete(hall)
        db.commit()
        return "Зал успешно удален"
    else:
        return "Зал не найден"





