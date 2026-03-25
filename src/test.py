import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()


db_url = os.getenv('PG_LINK')

try:
    engine = sqlalchemy.create_engine(db_url)
    connection = engine.connect()
    print("Подключение успешно!")
    connection.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")
