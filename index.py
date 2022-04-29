import config
import logging
import pyautogui, schedule

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from mss import mss

logging.basicConfig(level = logging.INFO)

bot = Bot(token = config.token, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

# Кнопки
@dp.message_handler(commands = "oversee")
async def cmd_inline_url(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True) # Изменение размера эконок
	# Первая кнопка
	button_1 = types.KeyboardButton(text='Скриншот!')
	keyboard.add(button_1)

	await message.answer("Что хотите сделать?", reply_markup=keyboard)

# Ответ на нажатие кнопки с запрашиванием пароля
@dp.message_handler(Text(equals = 'Скриншот!'))
async def answer_pass(message: types.Message):
	# создание скриншота 1-го монитора
	with mss() as sct:
		sct.shot(mon=0)
	# Путь к изображению(каждый раз новый скриншот будет заменять старый)
	photo = 'D:/Python2.0/monitor-1.png'

	# Отправка скриншота
	await message.answer("Присылаю снимок экрана...", reply_markup = types.ReplyKeyboardRemove())
	await bot.send_photo(message.from_user.id, types.InputFile(photo))


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
