import asyncio
from aiogram import types

from keyboards.inline.Viloyatlar_menu import viloyatlarmenu
from loader import dp, db, bot


@dp.message_handler(text="/start", user_id="5280188027")
async def bot_start(message: types.Message):
    name=message.from_user.full_name
    xabar = f"Assalomu Alaykum. <b>Boshliq</b>\n<b>Ob-Havo</b> ma'lumotlari botiga xush kelibsiz\n"
    await message.answer(xabar, reply_markup=viloyatlarmenu)



@dp.message_handler(text="/admin", user_id="5280188027")
async def get_all_users(message: types.Message):
    msg=f"/obunachilar - Barcha foydalanuvchilar.\n"
    msg+=f"/obunachilar_soni - Barcha foydalanuvchilar soni.\n"
    msg+=f"/reklama, Barcha foydalanuvchilarga reklama yuborish.\n\n\n"
    msg+=f"/baza_tozalash, Bazadagi barcha foydalanuvchilarni o'chiradi.\n"

    await message.answer(msg)




@dp.message_handler(text="/obunachilar_soni", user_id="5280188027")
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    x=f"<b>{len(users)}</b> - ta"
    await message.answer(x)






@dp.message_handler(text="/obunachilar", user_id="5280188027")
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    n = 1
    for user in users:
        x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
        x+= f"ismi__  <b>{user[1]}</b>\n"
        n += 1
        await message.answer(x)


@dp.message_handler(text="/reklama", user_id="5280188027")
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Assalom Alaykum, /start tugmasini bosing bot yangilandi🔄")
        await asyncio.sleep(0.5)


    await message.answer("<b>Reklama yuborildi !</b>" )

@dp.message_handler(text="/baza_tozalash", user_id="5280188027")
async def get_all_users(message: types.Message):
    #db.delete_users()  #Admin papkasidagi kodni izohdan olinsangiz tozalanadi bu esa xavfli !
    await message.answer("Admin papkasidagi kodni izohdan olsangiz tozalanadi bu esa xavfli !")







