import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv



# Загружаем переменные из .env файла
load_dotenv()

class PostgresHandler:
    def __init__(self, configs):
        self.pg_link = os.getenv(configs)
        self.connection = None


    async def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            if self.connection is None or self.connection.closed:
                self.connection = psycopg2.connect(dsn=self.pg_link)
                print("Соединение с PostgreSQL установлено")
        except Error as e:
            print(f"Ошибка подключения: {e}")
            self.connection = None



    async def execute_query(self, query, params=None, fetch=False):
        """Выполняет SQL-запрос."""
        await self.connect()
        result = None
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
                    print("выполнение запроса создания таблицы")
                    if fetch:
                        result = cursor.fetchall()
                        print(result)
                    self.connection.commit()
            except Error as e:
                print(f"Ошибка выполнения запроса: {e}")
                self.connection.rollback()
        return result

    def create_table_create(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                number_phone TEXT NOT NULL
            );
            """
        return create_table_query

    async def add_message(self, pool, user_id, username, text):
        """Записывает сообщение в БД."""
        async with pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO messages (user_id, name, number_phone) VALUES ($1, $2, $3)",
                user_id, username, text
            )

    async def close(self):
        """Закрывает соединение."""
        if self.connection and not self.connection.closed:
            await self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def __del__(self):
        """Деструктор для закрытия соединения."""
        self.close()

