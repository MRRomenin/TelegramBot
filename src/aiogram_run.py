import asyncio
from create_bot import create_bot, get_dispatcher, pg_db, scheduler
from handlers.start import start_router
from src.core.config import Parser

# from work_time.time_func import send_time_msg



async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    pool = Parser('PG_LINK')
    print(pool.parser_url())
    bot = create_bot()
    dp = get_dispatcher()
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    # dp.message.middleware(DbMiddleware(pool))
    await dp.start_polling(bot)

# class DbMiddleware:
#     def __init__(self, pool):
#         self.pool = pool
#
#     async def __call__(self, handler, event, data):
#         data['pool'] = self.pool
#         return await handler(event, data)


if __name__ == "__main__":
    asyncio.run(main())
