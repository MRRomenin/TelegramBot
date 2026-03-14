from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.create_bot import pg_db
import asyncpg
# from src.db_handler.db_class import .create_table_create


# from src.db_handler.db_class import add_message


start_router = Router()

create_table = pg_db.create_table_create()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await pg_db.execute_query(create_table)
    await message.answer('Привет, введите ФИО, и номер телефона')



# @start_router.message(Command('start_2'))
# async def cmd_start_2(message: Message):
#     await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
#
# @start_router.message(F.text)
# async def save_db(message: Message, pool: asyncpg.Pool):
#     await message.answer("Сообщение сохранено!")
#     await pg_db.add_message(
#         message.from_user.id,
#         message.from_user.username,
#         message.text
#     )
#
#     await message.answer('Сообщение отправлено')
