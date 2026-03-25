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

from src.db_handler.db_class import create_table_create

start_router = Router()


class UserState(StatesGroup):
    unstarted = State()


@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.unstarted)
    create_table_create()
    await message.answer(
        "Привет, введите ФИО, и номер телефона через запятую",
        reply_markup=ReplyKeyboardRemove(),
    )


@start_router.message(F.text, UserState.unstarted)
async def save_db(message: Message) -> None:
    text = message.text
    data_list = [item.strip() for item in text.split(',')]
    await pg_db.execute_query(data_list[0], data_list[1])

    await message.answer('Сообщение отправлено',
                         reply_markup=ReplyKeyboardRemove())


@start_router.message(F.text, StateFilter(None))
async def handle_all_messages(message: Message) -> None:
    await message.answer(f"Сначала нажмите /start, чтобы запустить бота.")
