import os
# import psycopg2
# from psycopg2 import Error
from dotenv import load_dotenv
import asyncpg
from src.error.error import ErrorConnect


# Загружаем переменные из .env файла
load_dotenv()

# maybe a separate file
def add_message() -> str:
    """Записывает сообщение в БД."""
    return "INSERT INTO customer (name, number_phone) VALUES ($1, $2)"


class PostgresHandler:
    def __init__(self, configs):
        self.pg_link = os.getenv(configs)
        self.connection = None


    async def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            if self.connection is None or self.connection.close:
                self.connection = await asyncpg.connect(dsn=self.pg_link) # need pool
                print("Соединение с PostgreSQL установлено")
        except ErrorConnect as e:
            print(f"Ошибка подключения: {e}")
            self.connection = None


    async def create_table_create(self) -> str:
        create_table_query = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                number_phone TEXT NOT NULL
            );
            """
        return create_table_query

    async def execute_query(self, username, text) -> None:
        """Выполняет SQL-запрос."""
        await self.connect()
        query_add = add_message()
        if self.connection:
            try:
                await self.connection.execute(query_add, username, text)
                print("выполнение запроса записи в customer")
                # self.connection.commit()
            except ErrorConnect as e:
                print(f"Ошибка выполнения запроса: {e}")
                # self.connection.rollback()


        # await message.answer("Сообщение сохранено в базе данных!")
        # async with pool.acquire() as conn:
        #     await conn.execute(
        #         "INSERT INTO messages (user_id, name, number_phone) VALUES ($1, $2, $3)",
        #         user_id, username, text
        #     )

    async def close(self):
        """Закрывает соединение."""
        if self.connection and not self.connection.close:
            await self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def __del__(self):
        """Деструктор для закрытия соединения."""
        self.close()