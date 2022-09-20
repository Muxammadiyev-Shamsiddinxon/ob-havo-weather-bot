from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.Viloyatlar_menu import viloyatlarmenu
from loader import dp



@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text)


@dp.message_handler()
async def bot_start(message: types.Message):
    name=message.from_user.full_name
    xabar = f"<b>Iltimos men sizni tushunmayapman menga bo'limlar orqali murojat qiling ! </b>"
    await message.answer(xabar, reply_markup=viloyatlarmenu)



