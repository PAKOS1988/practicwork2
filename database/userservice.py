from database.models import Card, User, Password
from database import get_db


# Регистрация пользователя
def register_user_db(user_phone_number: int, user_name: str, password: str):
    # Проверка номера
    db = next(get_db())
    # Проверка номера
    checker = db.query(User).filter_by(user_phone_number=user_phone_number).first()
    if checker:
        return "Пользователь с таким номером уже есть в БД"
    # Если нет пользователя в БД
    new_user = User(user_phone_number=user_phone_number, user_name=user_name)
    db.add(new_user)
    db.commit()
    new_user_password = Password(user_id=new_user.user_id, password=password)
    db.add(new_user_password)
    db.commit()
    return "Пользователь успешно создан"


# Проверка пароля
def check_password_db(user_phone_number, password):
    db = next(get_db())
    cheker1 = db.query(User).filter_by(user_phone_number=user_phone_number).first()
    try:
        cheker2 = db.query(Password).filter_by(user_id=cheker1.user_id).first()
    except:
        cheker2 = False
    if cheker1 and cheker2.password == password:
        return cheker2.user_id
    if cheker1 != user_phone_number:
        return "Неверный номер телефона"
    if cheker2.password != password:
        return "Неверно введен пароль"


# Удаление пользователя
def delete_user_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()
        return "Пользователь успешно удален"
    else:
        return "Пользователь не найден"



# Личные данные  пользователя
def get_user_cabinet_db(user_id):
    db = next(get_db())
    cheker = db.query(User).filter_by(user_id=user_id).first()
    if cheker:
        return cheker
    return "Ошибка в данных"

def get_user_card_db(user_id):
    db = next(get_db())
    cheker = db.query(Card).filter_by(user_id=user_id).first()
    if cheker:
        return cheker
    return "У Вас нет привязанных карт"