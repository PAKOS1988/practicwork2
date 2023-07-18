from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import psycopg2
def first_message_kb():
    kb_space = ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = KeyboardButton('Да')
    button_no = KeyboardButton('Нет')
    kb_space.add(button_yes, button_no)
    return kb_space

def choice_film_kb():
    conn = psycopg2.connect(host="localhost", port=5432, database="practicwork", user="postgres", password="UTMURMK6D19BK102")
    cur = conn.cursor()
    cur.execute("""SELECT movie_name FROM movies""")
    lst_film = cur.fetchall() #список фильмов подставить в нижнию генерацию
    return ReplyKeyboardMarkup([[KeyboardButton(x[0])] for x in lst_film], resize_keyboard=True) # строка генерации и возвращения вместо lst_film нужны фильмы

def choice_cinema_kb():
    conn = psycopg2.connect(host="localhost", port=5432, database="practicwork", user="postgres", password="UTMURMK6D19BK102")
    cur = conn.cursor()

    cur.execute("""SELECT cinema_name FROM cinemas""")
    lst_cinema = cur.fetchall() # Список кинотеатров
    return ReplyKeyboardMarkup([[KeyboardButton(x[0])] for x in lst_cinema],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_cinema нужны кинотеатры

def choice_data_film_kb():
    conn = psycopg2.connect(host="localhost", port=5432, database="practicwork", user="postgres", password="UTMURMK6D19BK102")
    cur = conn.cursor()

    cur.execute("""SELECT movie_release_year FROM movies""")
    lst_data_film = cur.fetchall()
    return ReplyKeyboardMarkup([[KeyboardButton(x[0])] for x in lst_data_film],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_data_film нужны дата фильма

def choice_hall_kb():
    conn = psycopg2.connect(host="localhost", port=5432, database="practicwork", user="postgres", password="UTMURMK6D19BK102")
    cur = conn.cursor()

    cur.execute("""SELECT cinema_id, hall_class FROM halls""")
    lst_hall = cur.fetchall()
    return ReplyKeyboardMarkup([[KeyboardButton(x[1])] for x in lst_hall],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_hall нужны залы или тип/статус зала

def choice_position_kb():
    conn = psycopg2.connect(host="localhost", port=5432, database="practicwork", user="postgres", password="UTMURMK6D19BK102")
    cur = conn.cursor()

    cur.execute("""SELECT order_number_position FROM orders""")
    lst_position = cur.fetchall()
    return ReplyKeyboardMarkup([[KeyboardButton(x[0])] for x in lst_position],
                               resize_keyboard=True)  # строка генерации и возвращения вместо lst_position нужны свободные места
