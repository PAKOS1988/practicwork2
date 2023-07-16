from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Подключение к базе данных
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:road69@localhost:5432/practicwork'

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=10)

#Сессии для базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Общий класс для создания моделей данных
Base = declarative_base()

#Генерация подключений к БД
def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

#Импорт функционала для БД
from database.cinemaservice import *

