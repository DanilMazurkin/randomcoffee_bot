from aiogram import types
from core.telegram import dp
from core.messages import MESSAGE_FOR_START, BUTTON_REGISTER, RANDOM_WITHOUT_REGISTER
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.keyboard.start_keyboard import keyboard_for_start


@dp.message_handler(CommandStart())
async def process_start_command(message: types.Message):
    """Эта функция обрабатывает команду start"""
    await message.reply(
        MESSAGE_FOR_START,
        reply_markup=keyboard_for_start()
    )


@dp.message_handler(lambda message: message.text == BUTTON_REGISTER)
async def registration(message: types.Message):
    await message.reply(
        "Функционал регистрации..."
    )


@dp.message_handler(lambda message: message.text == RANDOM_WITHOUT_REGISTER)
async def search_without_register(message: types.Message):
    await TelegramUser.create(
        chat_id=message.from_user.id
    )
    await message.reply(
        "Функционал поиска анонимных собеседников.."
    )
