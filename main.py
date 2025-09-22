import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from utils.db import init_db
from utils.reminders import start_scheduler
from handlers.start import start_command
from handlers.add_entry import add_entry
from handlers.stats import stats_command

async def main():
    await init_db()
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.message.register(start_command, commands=["start"])
    dp.message.register(add_entry, commands=["add"])
    dp.message.register(stats_command, commands=["stats"])
    
    start_scheduler()
    
    print("Бот HairTracker запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
