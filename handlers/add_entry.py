from aiogram import types
from utils.db import DB_PATH
import aiosqlite

async def add_entry(message: types.Message):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT premium FROM users WHERE telegram_id=?",
            (message.from_user.id,)
        )
        row = await cursor.fetchone()
        if not row or row[0] != 1:
            await message.answer("Подписка не активна. Оформите подписку через кнопку.")
            return
        
    await message.answer("Пришлите фото или заметку для записи в дневник HairTracker.")
