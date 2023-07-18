from database.models import User, Cinema, Card, Movie, Order, Session, Transaction
from database import get_db
from datetime import datetime

# Регистрация заказа
def register_order_db(user_id:int,
                      session_id:int,
                      order_number_position:int):
    db = next(get_db())
    # Проверка пользователя и сессии
    checker1 = db.query(User).filter_by(user_id=user_id).first()
    if checker1:
        checker2 = db.query(Session).filter_by(session_id=session_id).first()
        if checker2:
            new_order = Order(user_id=checker1.user_id,
                              session_id=checker2.session_id,
                              order_number_position=order_number_position,
                              order_exp_date=datetime.utcnow())
            db.add(new_order)
            db.commit()
            return "Заказ добавлен, пожалуйста оплатите!"
        return "Сессия не найдена"
    return "Пользователь не найден"

# Оплата заказа
def payment_order_db(order_id:int,
                     user_id:int,
                     card_number:int,
                     amount:int,
                     cinema_id:int,
                     card_to:int):
    db = next(get_db())
    checker_order = db.query(Order).filter_by(order_id=order_id).first()
    if checker_order:
        checker_user = db.query(User).filter_by(user_id=user_id).first()
        checker_user_card = db.query(Card).filter_by(user_id=user_id).first()
        checker_card_cinema = db.query(Cinema).filter_by(cinema_id=cinema_id).first()
        if (checker_user_card and checker_card_cinema and checker_user):
            if (checker_user.user_id == user_id and
                checker_user_card.card_number == card_number and
                checker_user_card.card_balance>=amount) and (checker_card_cinema.cinema_id == cinema_id and
                                                             checker_card_cinema.cinema_card_number == card_to):
                new_payment = Transaction(card_from=card_number,card_to=card_to,amount=amount,tansaction_date=datetime.utcnow())
                checker_user_card.card_balance -= amount
                checker_card_cinema.cinema_balance += amount
                checker_order.order_status = "Оплачено"
                db.add(new_payment)
                db.commit()
                return "Оплата завершена"
            return "Ошибка в данных"
        return "Введены неверные данные"
    return "Уточните номер заказа"

