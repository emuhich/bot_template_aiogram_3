from aiogram import types
from aiogram.methods import SetMyCommands


async def set_default_commands():
    await SetMyCommands(commands=[
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="menu", description="📜 Главное меню"),
        types.BotCommand(command="help", description="Помощь"),
    ])
