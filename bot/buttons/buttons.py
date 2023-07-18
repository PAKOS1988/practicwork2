from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def first_message_kb():
    kb_space = ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = KeyboardButton('Да')
    button_no = KeyboardButton('Нет')
    kb_space.add(button_yes, button_no)
    return kb_space

def choice_film_kb():
    lst_film = ['1','2','3','4'] #список фильмов подставить в нижнию генерацию
    return ReplyKeyboardMarkup([[KeyboardButton(x)] for x in lst_film], resize_keyboard=True) # строка генерации и возвращения вместо lst_film нужны фильмы

def choice_cinema_kb():
    lst_cinema = ['*','*','*','*','*'] # Список кинотеатров
    return ReplyKeyboardMarkup([[KeyboardButton(x)] for x in lst_cinema],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_cinema нужны кинотеатры

def choice_data_film_kb():
    lst_data_film=['*','*','*','*','*']
    return ReplyKeyboardMarkup([[KeyboardButton(x)] for x in lst_data_film],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_data_film нужны дата фильма

def choice_hall_kb():
    lst_hall=['*','*','*','*','*']
    return ReplyKeyboardMarkup([[KeyboardButton(x)] for x in lst_hall],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_hall нужны залы или тип/статус зала

def choice_position_kb():
    lst_position=['*','*','*','*','*']
    return ReplyKeyboardMarkup([[KeyboardButton(x)] for x in lst_position],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_position нужны свободные места
