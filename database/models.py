from database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


# Таблица пользователей
class User(Base):
    __tablename__= 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_phone_number = Column(Integer, nullable=False)
    user_name = Column(String, nullable=False)
    user_reg_date = Column(DateTime, default=datetime.now())

# Таблица паролей
class Password(Base):
    __tablename__= 'passwords'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)

    user_fk = relationship(User)

# Таблица карт
class Card(Base):
    __tablename__= 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    card_holder = Column(String)
    card_exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float)
    card_added_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User)


#Таблица кинотеатров
class Cinema(Base):
    __tablename__= 'cinemas'
    cinema_id = Column(Integer, autoincrement=True, primary_key=True)
    cinema_name = Column(String, nullable=False)
    cinema_location = Column(String, nullable=False)
    cinema_contact = Column(String)
    cinema_star = Column(Integer)
    cinema_card_number = Column(Integer, nullable=False)
    cinema_balance = Column(Float, nullable=False)

# Таблица залов в кинотеатре и стоимость
class Hall(Base):
    __tablename__= 'halls'
    cinema_id = Column(Integer, ForeignKey('cinemas.cinema_id'), nullable=False)
    hall_id = Column(Integer, autoincrement=True, primary_key=True)
    hall_class = Column(String, nullable=False)
    hall_number_of_seats = Column(Integer, nullable=False)
    hall_price = Column(Integer, nullable=False)

    cinema_fk = relationship(Cinema)

# Таблица фильмов
class Movie(Base):
    __tablename__= 'movies'
    movie_id = Column(Integer, autoincrement=True, primary_key=True)
    movie_name = Column(String, nullable=False)
    movie_production = Column(String, nullable=False)
    movie_release_year = Column(Integer, nullable=False)
    movie_genre = Column(String, nullable=False)
    movie_duration = Column(Integer, nullable=False)
    movie_description = Column(String, default=None)




# Таблица сеансов
class Session(Base):
    __tablename__= 'sessions'
    session_id = Column(Integer, autoincrement=True, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'), nullable=False)
    hall_id = Column(Integer, ForeignKey('halls.hall_id'), nullable=False)
    session_datetime = Column(DateTime, nullable=False)

    movie_fk = relationship(Movie)
    hall_fk = relationship(Hall)

class Order(Base):
    __tablename__= 'orders'
    order_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    session_id = Column(Integer, ForeignKey('sessions.session_id'), nullable=False)
    order_number_position = Column(Integer, nullable=False)
    order_exp_date = Column(DateTime, default=datetime.now())
    order_status = Column(String, default='Ожидает оплату')

    user_fk = relationship(User)
    session_fk = relationship(Session)


# Таблица платежей
class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    card_from = Column(Integer, ForeignKey('cards.card_id'), nullable=False)
    amount = Column(Float, nullable=False)
    card_to = Column(Integer, ForeignKey('cinemas.cinema_id'), nullable=False)
    tansaction_date = Column(DateTime, default=datetime.now())

    card_fk = relationship(Card)
    cinema_fk = relationship(Cinema)





