from aiogram import Dispatcher, executor, Bot
from config import config_bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters
from State.State import CinemaInfo
from buttons import buttons
from qrcode_dir.generated_qrcode import generate_qrcode
import qrcode

bot = Bot(config_bot.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help']) # Приветственное сообщение
async def greetings(message):
    await message.answer('* Приветствуем. Это бот для записи в кинотеатр. Хотите продолжить? *', reply_markup=buttons.first_message_kb())

@dp.message_handler(lambda msg: msg.text == 'Да', content_types=['text'])
async def choice_film(message):
    await message.answer('Выберите фильм который хотите посмотреть', reply_markup=buttons.choice_film_kb())
    await CinemaInfo.user_film.set()

@dp.message_handler(state=CinemaInfo.user_film)
async def choice_cinema(message, state=CinemaInfo.user_film):
    film = message.text
    await state.update_data(user_film=film)
    await message.answer('Выберите время просмотра фильма', reply_markup=buttons.choice_data_film_kb())
    await CinemaInfo.user_time.set()

@dp.message_handler(state=CinemaInfo.user_time)
async def choice_cinema(message, state=CinemaInfo.user_time):
    data = message.text
    await state.update_data(user_data=data)
    await message.answer('Выберите кинотеатр в котором хотите посмотреть фильм', reply_markup=buttons.choice_cinema_kb())
    await CinemaInfo.user_cinema.set()

@dp.message_handler(state=CinemaInfo.user_cinema)
async def choice_hall(message, state=CinemaInfo.user_cinema):
    cinema = message.text
    await state.update_data(user_cinema=cinema)
    await message.answer('Выберите зал', reply_markup=buttons.choice_hall_kb())
    await CinemaInfo.user_hall.set()

@dp.message_handler(state=CinemaInfo.user_hall)
async def choice_position(message, state=CinemaInfo.user_hall):
    hall = message.text
    await state.update_data(user_hall=hall)
    await message.answer('Выберите место где бы хотели посмотреть фильм', reply_markup=buttons.choice_position_kb())
    await CinemaInfo.user_position.set()

@dp.message_handler(state=CinemaInfo.user_position)
async def create_qrcode(message, state=CinemaInfo.user_position):
    position = message.text
    await state.update_data(user_position=position)
    all_info = await state.get_data()
    print(all_info)
    generate_qrcode(all_info)
    with open('img_qr_code.png', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)
    await state.finish()

executor.start_polling(dp)

