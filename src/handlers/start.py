from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.create_bot import pg_db
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
# from aiogram.filters import BaseFilter
from aiogram.types import (
    # KeyboardButton,
    # ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

# import asyncpg
# from src.db_handler.db_class import .create_table_create


# from src.db_handler.db_class import PostgresHandler


start_router = Router()

# create_table = pg_db.execute_query()

class UserState(StatesGroup):
    unstarted = State()



@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    # await message.answer('Привет, введите ФИО, и номер телефона')
    await state.set_state(UserState.unstarted)
    await message.answer(
        "Привет, введите ФИО, и номер телефона через запятуюч",
        reply_markup=ReplyKeyboardRemove(),
    )


@start_router.message(F.text, UserState.unstarted)
async def save_db(message: Message) -> None:
    # user_text = message.text
    # print(type(user_text))
    # await message.answer(f"You read {user_text}")
    # user_id = message.from_user.id
    # username = message.from_user.username
    # name = message.text
    text = message.text
    data_list = [item.strip() for item in text.split(',')]
    await pg_db.execute_query(data_list[0], data_list[1])

    # mess = pg_db.add_message(user_id, username, text)
    # await pg_db.execute_query.add_message(user_id, username, text)
    # mess.register_next_step_handler(code, asyncio.run(claimcode()))
    # mess.add_message(user_id, text)
    # d = {user_id, username, text}

    # print(a)

    await message.answer('Сообщение отправлено',
                         reply_markup = ReplyKeyboardRemove())


@start_router.message(F.text, StateFilter(None))
async def handle_all_messages(message: Message) -> None:
    await message.answer(f"Сначала нажмите /start, чтобы запустить бота.")
