from database.models import Cinema, Hall, Session, Movie
from database import get_db
from datetime import datetime
from datetime import timedelta

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

# Вывод сеансов в определенном зале
def get_session_db(hall_id: int):
    db = next(get_db())
    get_session = db.query(Session).filter_by(hall_id=hall_id).first()
    if get_session:
        return get_session
    return "Сеансы не найдены"

# добавление Сеанса
def add_session_db(movie_id: int,
                   hall_id: int,
                   session_datetime:datetime):
    db = next(get_db())
    result_movie = db.query(Movie).filter_by(movie_id=movie_id).first()
    result_hall = db.query(Hall).filter_by(hall_id=hall_id).first()
    check_session = get_session_db(hall_id)
    print(result_movie)

    add_session = Session(movie_id=movie_id,
                          hall_id=hall_id,
                          session_datetime=session_datetime)

    db.add(add_session)
    db.commit()
    return "Сеанс добавлен"


# удаление сеанса
def delete_session_db(session_id: int):
    db = next(get_db())
    session = db.query(Session).filter_by(session_id=session_id).first()
    if session:
        db.delete(session)
        db.commit()
        return "Сеанс успешно удален"
    return "Сеанс не найден"

#Вывод всех сеансов

def get_all_session_db():
    db = next(get_db())
    session = db.query(Session).all()
    if session:
        return session


