import json
import re
from datetime import datetime, timedelta
import datetime
from asyncio import Lock

start_lock = Lock()


#from aiogram.types import InputMediaPhoto, InputMediaVideo


from aiogram import Dispatcher, Bot, types, executor
import sqlite3
from aiogram.utils.exceptions import BotBlocked, BadRequest, MessageTextIsEmpty

# from keyboard import adm, iad, kb0, kb1, kb2, kb3, kb4
# from config import *
import os


from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


# 'proxy_url': PROXY_URL,
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def to_start(msg: types.Message):  # SUBSCRIBE='ads'
    await msg.answer('Hello')



@dp.message_handler()
async def on_startup(_):
    print('❇Бот запущен!❇')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)

