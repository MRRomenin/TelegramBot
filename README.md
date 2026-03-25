# Telegram DB Writer Bot

Простой Telegram-бот, который принимает сообщения от пользователя и сохраняет их в базу данных postgreSQL.

## 🛠 Технологии
* **Язык:** Python 3.10+
* **Библиотека бота:** aiogram, asyncpg, dotenv
* **База данных:** PostgreSQL

## 🚀 Быстрый старт

### Клонирование репозитория
```bash
git clone [https://github.com/ваш-логин/название-репозитория.git]
(https://github.com/ваш-логин/название-репозитория.git)
cd название-репозитория
```

## .env файл

### Пример .env файла

```bash
TOKEN=ваш_токен_от_botfather
ADMINS=00000000,000000001
PG_LINK=postgresql://USER_LOGIN:USER_PASSWORD@HOST_API:PORT/NAME_BD
```

## Виртуальное окружение

### Рекомендуется использовать виртуальное окружение:

```bash
python -m venv venv
```  
source venv/bin/activate  # Для Linux/macOS  
venv\Scripts\activate  # Для Windows

```bash
pip install -r requirements.txt
```


## Запуск программы


```bash
python src/aiogram_run.py
```

В тг бота нужно ввести команду ```/start```
