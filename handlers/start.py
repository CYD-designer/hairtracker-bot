from aiogram import types
from utils.db import DB_PATH
import aiosqlite

async def start_command(message: types.Message):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)",
            (message.from_user.id, message.from_user.username)
        )
        await db.commit()
        
        cursor = await db.execute(
            "SELECT premium FROM users WHERE telegram_id=?",
            (message.from_user.id,)
        )
        row = await cursor.fetchone()
        
        if row and row[0] == 1:
            await message.answer(
                "Добро пожаловать! Сделайте первое фото сейчас, чтобы зафиксировать старт прогресса."
            )
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(types.KeyboardButton("Оформить подписку"))
            await message.answer(
                "Привет! Чтобы пользоваться ботом HairTracker, оформите подписку через Boosty/SBP.",
                reply_markup=keyboard
            )
