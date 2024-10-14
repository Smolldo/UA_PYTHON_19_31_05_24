import logging # для логів. запис звітів. відслідковування подій
import asyncio # для роботи з асинхронними подіями

from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from films import films

TOKEN = '7533224581:AAHzqXevBwBOvq8K4c3OkNAluxaZh4gYQvE'

logging.basicConfig(level=logging.INFO) #записує дані про події на рівні ІНФО і ВИЩЕ(Error)

bot = Bot(token=TOKEN) #створення об'єкту бота
dp = Dispatcher(storage=MemoryStorage()) #ініціалізація диспатчера

ADMINS = [1090774508] #адміни

async def on_startup(dp):
    logging.info('Bot started') # виведення логу про запуск бота

@dp.message(CommandStart())  #декоратор для асинхрону. тригериться на команду "/start"
async def command_start_handler(message: Message): #'/start'
    film_choice = InlineKeyboardMarkup(inline_keyboard = []) #формуємо клавіатуру
    for f in films:
        button = InlineKeyboardButton(text=f, callback_data=f) #текст на клавіатуру
        film_choice.inline_keyboard.append([button]) #додавання кнопки в список кнопок
    await message.answer(text='Choose film', reply_markup=film_choice) #await - призупиняє інші асинхронні дії для свого першочергового виконання



async def main():
    await dp.start_polling(bot) #головна функція запуску бота

if __name__ == '__main__':
    asyncio.run(main()) #перевірка точки входу