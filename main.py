from fastapi import FastAPI
from database import Base, engine

#Создать все таблицы для базы данных

Base.metadata.create_all(bind=engine)

#Объект для фастапи
app = FastAPI()

from cinema import cinema_api
from user import user_api
from card import card_api
# from payment import payment_api


# запуск проекта фастапи
# uvicorn main:app --reload