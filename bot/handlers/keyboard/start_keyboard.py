from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from core.messages import BUTTON_REGISTER
from core.messages import RANDOM_WITHOUT_REGISTER


def keyboard_for_start() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(text=BUTTON_REGISTER)
    )

    keyboard.add(
        KeyboardButton(text=RANDOM_WITHOUT_REGISTER)
    )

    return keyboard
