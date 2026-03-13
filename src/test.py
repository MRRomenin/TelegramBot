import sqlalchemy

db_url = "postgresql://roman:1712@localhost:5432/db_telegram_bot"

try:
    engine = sqlalchemy.create_engine(db_url)
    connection = engine.connect()
    print("Подключение успешно!")
    connection.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")
