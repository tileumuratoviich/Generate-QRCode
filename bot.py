from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import qrcode
import os
from dotenv import load_dotenv  

load_dotenv()  

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("QRCode jaratiw"))
        await message.reply("Assalawma áleykum, QRCode jaratiw ushin tańlań:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text =="QRCode jaratiw")
async def answer_for_button(message: types.Message):
	await message.reply("QRCode jaratiw ushin TEXT yamasa URL jiberiń!")

@dp.message_handler(commands=['dev'])
async def developers_handler(message: types.Message):
	keyboard = types.InlineKeyboardMarkup()
	button = types.InlineKeyboardButton("Developer", url="https://t.me/tileumuratoviich")
	keyboard.add(button)
	await message.answer(">Bot islew ||200 000UZS|| \n>Bot 1\\-2 hàpte araliģinda tayin boladi \n\nQalģan maģliwmatlar kelisim waqtinda aytiladi, developer menen baylanisiń:", parse_mode="MarkdownV2", reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help_users(message: types.Message):
	keyboard = types.InlineKeyboardMarkup()
	button = types.InlineKeyboardButton("Admin", url="https://t.me/tileumuratoviich")
	keyboard.add(button)
	await message.reply("Sizde qandayda bir mashqalalar bolsa admin menen baylanisiń!", reply_markup=keyboard)
	
@dp.message_handler(content_types=types.ContentType.TEXT)
async def generate_qr(message: types.Message):
	qr = qrcode.QRCode(box_size=10, border=4 )
	qr.add_data(message.text)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	img.save("qrcode.png")
	qr_file = types.InputFile("qrcode.png")
	
	await message.reply_photo(qr_file)
	await message.answer("Premium versiyada bundanda zor imkaniyatlar!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)