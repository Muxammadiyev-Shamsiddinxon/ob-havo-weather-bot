import sqlite3
from aiogram import types
from loader import dp, db, bot
from keyboards.inline.Viloyatlar_menu import viloyatlarmenu



@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    # Foydalanuvchini bazaga qo'shamiz
    if username:
        try:
            db.add_user(id=id, name=name, username=username)
        except sqlite3.IntegrityError as err:
            pass
    else:
        try:
            db.add_user(id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass

    xabar=f"Assalomu Alaykum. <b>{name}.</b>\n<b>Ob-Havo</b> ma'lumotlari botiga xush kelibsiz\n"
    await message.answer(xabar)
    await message.answer(f"<b>Viloyatni tanlang</b>✅😎🌤🌤", reply_markup=viloyatlarmenu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{username}</b>\n "
    msg += f"<b>{name}</b>\n"
    msg += f" <b>{id}</b>\n\n"
    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id="5280188027", text=msg)


