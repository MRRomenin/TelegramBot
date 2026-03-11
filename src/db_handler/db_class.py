import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

class PostgresHandler:
    def __init__(self, configs):
        self.pg_link = os.getenv(configs)
        # self.port = os.getenv("POSTGRES_PORT")
        # self.dbname = os.getenv("POSTGRES_DB")
        # self.user = os.getenv("POSTGRES_USER")
        # self.password = os.getenv("POSTGRES_PASSWORD")
        self.connection = None

    def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            if self.connection is None or self.connection.closed:
                self.connection = psycopg2.connect(dsn=self.pg_link)
                # self.connection = psycopg2.connect(
                #     host=self.host,
                #     port=self.port,
                #     dbname=self.dbname,
                #     user=self.user,
                #     password=self.password
                # )
                print("Соединение с PostgreSQL установлено")
        except Error as e:
            print(f"Ошибка подключения: {e}")
            self.connection = None

    def execute_query(self, query, params=None, fetch=False):
        """Выполняет SQL-запрос."""
        self.connect()
        result = None
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
                    if fetch:
                        result = cursor.fetchall()
                    self.connection.commit()
            except Error as e:
                print(f"Ошибка выполнения запроса: {e}")
                self.connection.rollback()
        return result

    def close(self):
        """Закрывает соединение."""
        if self.connection and not self.connection.closed:
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def __del__(self):
        """Деструктор для закрытия соединения."""
        self.close()
