from main import app
from database.cardservice import add_user_card_to_db, delete_user_card_db, get_exact_card_balance_db, add_balance_card_db
from datetime import datetime



# Добавление карты
@app.post('/add_user_card')
async def add_user_card_api(user_id:int, card_number:int, card_holder:str, card_name:str, card_exp_date:int):
    result = add_user_card_to_db(user_id=user_id,
                                 card_number=card_number,
                                 card_name=card_name,
                                 card_holder=card_holder,
                                 card_exp_date=card_exp_date,
                                 card_balance=0,
                                 card_added_date=datetime.now())
    return {"status": 1, "message": result}


#Удаление карты
@app.delete('/delete_user_card')
async def delete_user_card_api(card_id:int, user_id:int):
    result = delete_user_card_db(card_id=card_id,
                                 user_id=user_id)

    return {"status": 1, "message": result}



# Проверка баланса карты
@app.get('/balance_user_card')
async def balance_user_card_api(card_number: int):
    result = get_exact_card_balance_db(card_number=card_number)
    return {"status": 1, "message": result}

# Пополнение баланса карты
@app.post('/balance_user_card')
async def add_balance_card_api(card_number: int):
    result = add_balance_card_db(card_number=card_number)
    return {"status": 1, "message": result}