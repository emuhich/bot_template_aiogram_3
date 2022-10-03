from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.misc.states import Test

user_router = Router()


@user_router.message(Command(commands=["start"]))
async def user_start(message: Message, state: FSMContext):
    await message.reply("Добро пожаловать")
    await state.set_state(Test.state_1)


@user_router.message(Test.state_1)
async def user_start(message: Message, state: FSMContext):
    await message.reply("В стейте")
