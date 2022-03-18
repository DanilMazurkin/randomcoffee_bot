from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from settings.bot import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
