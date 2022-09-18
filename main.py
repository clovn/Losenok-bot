from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
obr = True
i = 0


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Прислать задание'))
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name} Я твой бот-помощник, я буду помогать тебе с домашним заданием если тебе нужна будет помощь", reply_markup=keyboard)


@dp.message_handler(text='Прислать задание')
async def process_start_command(message: types.Message):
    if obr:
        await bot.send_message(message.from_user.id, 'Пришли фото')


@dp.message_handler(content_types=['photo'])
async def process_start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Прислать задание'))
    await message.photo[-1].download(f'photos/{message.photo[-1].file_id}.jpg')
    await bot.send_message(message.from_user.id, 'Менеджер ответит вам в ближайшее время')


if __name__ == '__main__':
    executor.start_polling(dp)