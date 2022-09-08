import sqlite3
import requests
import math
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from keyboards.inline.Viloyatlar_menu import viloyatlarmenu


import datetime as dt
from time import strftime


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.full_name

    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass

#await bot.send_message(chat_id=ADMINS[0], text=err)
#bitta tepada #quyilgan xatolikni kursatmaydi ..UNIQUE constraint failed: Users.id.. shuni kursatadi agar # olib tashlasak
    xabar=f"Assalomu Alaykum. <b>{name}.</b>\n<b>Ob-Havo</b> ma'lumotlari botiga xush kelibsiz\n"
    await message.answer(xabar)
    await message.answer(f"<b>Viloyatni tanlang</b>✅😎🌤🌤", reply_markup=viloyatlarmenu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{message.from_user.username}</b>\n "
    msg += f"<b>{message.from_user.full_name}</b>\n"
    msg += f" <b>{message.from_user.id}</b>\n\n"
    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."

    await bot.send_message(chat_id="5280188027", text=msg)
