import asyncio
from create_bot import create_bot, get_dispatcher, pg_db, scheduler
from handlers.start import start_router
from src.core.config import Parser
from src.error.error import ErrorLing
import logging
import sys
# from work_time.time_func import send_time_msg

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
    force=True
)

logger = logging.getLogger(__name__)

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()

    try:            # redo too
        pool = Parser('PG_LINK')
        print(pool.parser_url())
    except ErrorLing as e:
        print(f"not correct the link {e}")
        raise

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
    try:
        asyncio.run(main())
    except TypeError as e:
        print(f"{e}")
