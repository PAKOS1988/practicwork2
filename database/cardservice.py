from database.models import Card, User, Transaction
from database import get_db

# Добавляем карту
def add_user_card_to_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')
    #Проверка была ли добавлена карта
    checker = db.query(Card).filter_by(card_number=card_number).first()
    if checker:
        return "Карта уже существует"
    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return "Карта успешно добавлена"


#Удалить карту из сервиса
def delete_user_card_db(card_id, user_id):
    db = next(get_db())
    card_delete = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()
    if card_delete:
        db.delete(card_delete)
        db.commit()
        return "Карта удалена"
    return "Вы ввели неверные данные"


# Проверка баланса
def get_exact_card_balance_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first()
    return exact_card.card_balance