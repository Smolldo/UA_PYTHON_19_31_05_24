# import logging # для логів. запис звітів. відслідковування подій
# import asyncio # для роботи з асинхронними подіями

# from aiogram import Bot, Dispatcher
# from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.filters import CommandStart
# from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

# from films import films

# TOKEN = '7533224581:AAHzqXevBwBOvq8K4c3OkNAluxaZh4gYQvE'

# logging.basicConfig(level=logging.INFO) #записує дані про події на рівні ІНФО і ВИЩЕ(Error)

# bot = Bot(token=TOKEN) #створення об'єкту бота
# dp = Dispatcher(storage=MemoryStorage()) #ініціалізація диспатчера

# ADMINS = [1090774508] #адміни

# async def on_startup(dp):
#     logging.info('Bot started') # виведення логу про запуск бота

# @dp.message(CommandStart())  #декоратор для асинхрону. тригериться на команду "/start"
# async def command_start_handler(message: Message): #'/start'
#     film_choice = InlineKeyboardMarkup(inline_keyboard = []) #формуємо клавіатуру
#     for f in films:
#         button = InlineKeyboardButton(text=f, callback_data=f) #текст на клавіатуру
#         film_choice.inline_keyboard.append([button]) #додавання кнопки в список кнопок
#     await message.answer(text='Choose film', reply_markup=film_choice) #await - призупиняє інші асинхронні дії для свого першочергового виконання



# async def main():
#     await dp.start_polling(bot) #головна функція запуску бота

# if __name__ == '__main__':
#     asyncio.run(main()) #перевірка точки входу


import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from films import films

# Токен бота
TOKEN = '6825016568:AAHnONQDZ9C0YDvntpeW7hOf73SKzy2BV3E'

logging.basicConfig(level=logging.INFO)

# Ініціалізація бота і диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

ADMINS = [1090774508]

async def on_startup(dp):
    logging.info("Bot started!")

# Хендлер для обробки команди /start
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    # Створюємо інлайн-клавіатуру з кнопками фільмів
    film_choice = InlineKeyboardMarkup(inline_keyboard=[])
    for f in films:
        button = InlineKeyboardButton(text=f, callback_data=f)  # Кнопка з текстом і callback_data
        film_choice.inline_keyboard.append([button])  # Додаємо кнопку як окремий ряд до клавіатури
    await message.answer(text='Оберіть фільм:', reply_markup=film_choice)

# CallbackQueryHandler для обробки натискань кнопок
@dp.callback_query()
async def film_info_handler(callback: CallbackQuery):
    film_name = callback.data  # Отримуємо ім'я фільму з callback_data

    # Перевіряємо, чи є фільм у словнику
    if film_name not in films:
        await callback.message.answer("Фільм не знайдено. Спробуйте ще раз.")
        return  # Якщо фільму немає, зупиняємо подальшу обробку

    # Дістаємо інформацію про фільм зі словника
    film_data = films[film_name]
    photo = film_data.get('photo', 'no')  # Фото (банер) фільму
    director = film_data.get('director', 'Невідомо')  # Режисер
    year = film_data.get('year', 'Невідомо')  # Рік випуску
    genre = ', '.join(film_data.get('genre', []))  # Жанри (список перетворюємо на рядок)
    rating = film_data.get('rating', 'Невідомо')  # Рейтинг
    description = film_data.get('description', 'Опис відсутній')  # Опис фільму

    # Формуємо повідомлення
    film_info_message = (
        f"🎬 <b>{film_name}</b>\n"
        f"📅 Рік: {year}\n"
        f"🎭 Жанр: {genre}\n"
        f"🎥 Режисер: {director}\n"
        f"⭐ Рейтинг: {rating}\n\n"
        f"📝 Опис: {description}"
    )

    # Відправляємо фото і повідомлення з інформацією про фільм
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption=film_info_message, parse_mode='HTML')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())