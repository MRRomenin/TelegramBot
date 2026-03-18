from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.create_bot import pg_db
# import asyncpg
# from src.db_handler.db_class import .create_table_create


# from src.db_handler.db_class import PostgresHandler


start_router = Router()

# create_table = pg_db.execute_query()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, введите ФИО, и номер телефона')



# @start_router.message(Command('start_2'))
# async def cmd_start_2(message: Message):
#     await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
#
@start_router.message(F.text)
async def save_db(message: Message):
    # user_text = message.text
    # print(type(user_text))
    # await message.answer(f"You read {user_text}")
    # user_id = message.from_user.id
    username = message.from_user.username
    text = message.text

    await pg_db.execute_query(username, text)

    # mess = pg_db.add_message(user_id, username, text)
    # await pg_db.execute_query.add_message(user_id, username, text)
    # mess.register_next_step_handler(code, asyncio.run(claimcode()))
    # mess.add_message(user_id, text)
    # d = {user_id, username, text}

    # print(a)

    await message.answer('Сообщение отправлено')
