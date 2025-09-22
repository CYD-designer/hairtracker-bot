from aiogram import types

async def stats_command(message: types.Message):
    await message.answer(
        "Ваш прогресс:\n"
        "- Прогресс бар (например, 45%)\n"
        "- Достижения (7/30/90 дней подряд)\n"
        "- Календарь (✅/📸/💉)\n"
        "(Placeholder, картинки будут позже)"
    )
