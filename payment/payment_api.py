from database.paymentservice import payment_order_db, register_order_db
from datetime import datetime
from main import app


# Добавление заказа
@app.post('/add_order')
async def add_order_api(user_id:int,
                        session_id:int,
                        order_number_position:int):
    result = register_order_db(user_id=user_id,
                          session_id=session_id,
                          order_number_position=order_number_position)
    return {"status": 1, "message": result}

# Оплата заказа
@app.post('/payment_order')
async def payment_order_api(order_id:int,
                            user_id:int,
                            card_number:int,
                            amount:int,
                            cinema_id:int,
                            card_to:int):
    result = payment_order_db(order_id=order_id,
                              user_id=user_id,
                              card_number=card_number,
                              amount=amount,
                              cinema_id=cinema_id,
                              card_to=card_to)
    return {"status": 1, "message": result}