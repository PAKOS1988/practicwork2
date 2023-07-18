from aiogram.dispatcher.filters.state import State, StatesGroup

class CinemaInfo(StatesGroup):
    # user_id = State()
    # user_name = State()
    # phone_user = State()

    user_film = State()
    user_time = State()
    user_cinema = State()
    user_hall = State()
    user_position = State()
