import asyncio
from aiogram import types
from aiogram.types import ChatMemberUpdated
from data.config import ADMINS
from keyboards.inline.Viloyatlar_menu import viloyatlarmenu
from loader import dp, db, bot



@dp.message_handler(text="/start", user_id="5280188027")
async def bot_start(message: types.Message):
    xabar = f"Assalomu Alaykum. <b>Boshliq</b>\n<b>Ob-Havo</b> ma'lumotlari botingizga xush kelibsiz\n"
    await message.answer(xabar, reply_markup=viloyatlarmenu)


@dp.message_handler(text="/admin", user_id="5280188027")
async def admin_menu(message: types.Message):
    msg=f"/obunachilar - Barcha foydalanuvchilar.\n"
    msg+=f"/obunachilar_soni - Barcha foydalanuvchilar soni.\n"
    msg+=f"/reklama, Barcha foydalanuvchilarga reklama yuborish.\n\n\n"
    msg+=f"/baza_tozalash, Bazadagi barcha foydalanuvchilarni o'chiradi.\n"
    await message.answer(msg)


@dp.message_handler(text="/obunachilar_soni", user_id="5280188027")
async def obunachilar_soni(message: types.Message):
    users = db.select_all_users()
    x=f"<b>{len(users)}</b> - ta"
    await message.answer(x)



@dp.message_handler(text="/obunachilar", user_id="5280188027")
async def obunachilar(message: types.Message):
    users = db.select_all_users()
    n = 1
    for user in users:
        if user[2]:
            x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
            x+= f"ism__  <b>{user[1]}</b>\n"
            x += f"username__  @{user[2]}"
            n += 1
            await message.answer(x)
        else:
            x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
            x += f"ism__  <b>{user[1]}</b>\n"
            n += 1
            await message.answer(x)



@dp.message_handler(text="/reklama", user_id="5280188027")
async def send_reklama(message: types.Message):
    users = db.select_all_users()
    bordi = 0
    bormadi = 0
    for user in users:
        try:
            user_id = user[0]
            text = f"<b>Nosozlik tuzatildi uzr, /start tugmasini bosing yangilandi🔄</b>\n"
            text += f"<b>Endi ma'lumotlarni rasm ko'rinishida olishingiz mumkin!</b>\n\n"
            text += f"<b>Murojaat va taklif:</b>\n@Hacker_Attacks1👨‍💻"
            xabar = f"<b>Reklama yuborildi✅</b>  {user_id}"
            await bot.send_message(chat_id=user_id, text=text)
            await message.answer(text=xabar)
            bordi+=1
            await asyncio.sleep(0.5)
        except:
            user_id = user[0]
            xabar = f"<b>Reklama yuborilmadi❌</b>  {user_id}"
            await message.answer(text=xabar)
            bormadi+=1
            await asyncio.sleep(0.5)
    soni = f"{bordi}-ta Yuborildi✅\n{bormadi}-ta Yuborilmadi❌"
    await message.answer(text=soni)



@dp.message_handler(text="/baza_tozalash", user_id="5280188027")
async def baza_tozalash(message: types.Message):
    # db.delete_users()
    # await message.answer("baza tozalanadi !")

    #db.delete_users()
    await message.answer(" #db.delete_users() kodni izohdan olsangiz tozalanadi bu esa xavfli !")



# botdan chiqgan yoki kirganini bilib turadi
@dp.my_chat_member_handler()
async def some_handler(chat_member: ChatMemberUpdated):
    text = f"id: {chat_member.chat.id}\nism: {chat_member.from_user.full_name}\n"
    text += f"oldingi_status: {chat_member.old_chat_member.status}\n"
    text += f"hozirgi_status: {chat_member.new_chat_member.status}"
    await bot.send_message(chat_id=ADMINS[0], text=text)



