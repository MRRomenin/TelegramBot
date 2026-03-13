from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.create_bot import pg_db
from src.db_handler.db_class import create_table_create

start_router = Router()



@start_router.message(CommandStart())
async def cmd_start(message: Message):
    pg_db.execute_query(create_table_create())
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart().'
                         ' Привет, введите ФИО, и номер телефона')


# @start_router.message(Command('start_2'))
# async def cmd_start_2(message: Message):
#     await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
#
# @start_router.message(F.text == '/start_3')
# async def cmd_start_3(message: Message):
#     await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')
