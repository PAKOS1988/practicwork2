from main import app
from database.userservice import register_user_db, check_password_db, delete_user_db, get_user_cabinet_db, get_user_card_db


# Регистрация пользователя
@app.post('/register_user')
async def register_user_api(user_phone_number:int, user_name:str, password:str):
    result = register_user_db(user_phone_number=user_phone_number, user_name=user_name, password=password)
    return {'status': 1, "message": result}

# Вход в аккаунт
@app.get('/login')
async def login_user_api(user_phone_number:int, password:str):
    result = check_password_db(user_phone_number=user_phone_number, password=password)
    return {'status': 1, "message": result}


# Удаление пользователя
@app.delete('/delete-user')
async def delete_user_api(user_id: int):
    result = delete_user_db(user_id=user_id)
    return {"status": 1, "message": result}


# вывод личных данных
@app.get('/user_cabinet')
async def get_user_cabinet_api(user_id:int):
    result = get_user_cabinet_db(user_id=user_id)
    result2 = get_user_card_db(user_id=user_id)
    return {'status': 1, "message": result+result2}