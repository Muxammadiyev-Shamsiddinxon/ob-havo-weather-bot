from aiogram.types import InputFile
from loader import dp
import os

from handlers.haftalikobhavo import haftalik_obhavo



from aiogram.types import Message, CallbackQuery

from keyboards.inline.Viloyatlar_menu import viloyatlarmenu

from keyboards.inline.andijon import andijon_tumanlari, Andijonmenu, Baliqchimenu, Buzmenu, Buloqboshimenu, \
    Izboskanmenu, Jalolquduqmenu, Marhamatmenu, Oltinkulmenu, Paxtaobodmenu, Qurgontepamenu, Shahrixonmenu, Ulugnormenu, \
    Xujaobodmenu, Xonabodmenu, Asakamenu

from keyboards.inline.buxoro import buxoro_tumanlari, Buxoromenu, Gijduvonmenu, Jondormenu, Kogonmenu, Olotmenu, \
    Peshkumenu, Qorakulmenu, Qorovulbozormenu, Romitanmenu, Shofirkonmenu, Vobkentmenu

from keyboards.inline.fargona import fargona_tumanlari, Fargonamenu, Yozyovonmenu, Beshariqmenu, Bogdodmenu, \
    Buvaydamenu, Dangaramenu, Furqatmenu, Uzbekistonmenu, Oltiariqmenu, Quqonmenu, Qushtepamenu, Quvamenu, Rishtonmenu, \
    Suxmenu, Toshloqmenu, Uchkuprikmenu

from keyboards.inline.jizzax import jizzax_tumanlari, Jizzaxmenu, Zominmenu, Arnasoymenu, Baxmalmenu, Dustlikmenu, \
    Forishmenu, Gallaorolmenu, Mirzachulmenu, Paxtakormenu, Yangiobodmenu, Zafarobodmenu, Zarbandmenu

from keyboards.inline.namangan import namangan_tumanlari, Namanganmenu, Chortoqmenu, Chustmenu, Kosonsoymenu, \
    Mingbuloqmenu, Norinmenu, Popmenu, Turaqurgonmenu, Uchqurgonmenu, Uychimenu, Yangiqurgonmenu

from keyboards.inline.navoiy import navoiy_tumanlari, Navoiymenu, Zarafshonmenu, Karmanamenu, Konimexmenu, Navbahormenu, \
    Nurotamenu, Qiziltepamenu, Tomdimenu, Uchquduqmenu, Xatirchimenu

from keyboards.inline.qashqadaryo import qashqadaryo_tumanlari, Qarshimenu, Chiroqchimenu, Dehqonobodmenu, Guzormenu, \
    Kasbimenu, Kitobmenu, Kosonmenu, Mirishkormenu, Muborakmenu, Nishonmenu, Qamashimenu, Shahrisabzmenu, Yakkabogmenu

from keyboards.inline.qoraqalpogiston import qoraqalpoq_tumanlari, Nukusmenu, Amudaryomenu, Beruniymenu, Chimboymenu, \
    Elliktepamenu, Kegeylimenu, Muynoqmenu, Xujaylimenu, Qonlikulmenu, Qorauzaqmenu, Qungirotmenu, Shumanaymenu, \
    Taxiatoshmenu, Taxtakupirmenu, Turtkulmenu

from keyboards.inline.samarqand import samarqand_tumanlari, Samarqandmenu, Urgutmenu, Bulungurmenu, Ishtixonmenu, \
    Jomboymenu, Kattaqurgonmenu, Narpaymenu, Nurobodmenu, Oqdaryomenu, Pastdargommenu, Paxtachimenu, Qushrabotmenu, \
    Tayloqmenu, Poyariqmenu

from keyboards.inline.sirdaryo import sirdaryo_tumanlari, Sirdaryomenu, Boyovutmenu, Gulistonmenu, Oqoltinmenu, \
    Sardobamenu, Sayxunobodmenu, Xavosmenu, Yangiyermenu

from keyboards.inline.surxondaryo import surxon_tumanlari, Termizmenu, Uzunmenu, Angormenu, Bandixonmenu, Boysunmenu, \
    Denovmenu, Jarqurgonmenu, Muzrabotmenu, Oltinsoymenu, Qiziriqmenu, Qumqurgonmenu, Sariosiyomenu, Sherobodmenu, \
    Shurchimenu

from keyboards.inline.toshkent import toshkent_tumanlari, Toshkentmenu, Bekobodmenu, Bukamenu, Bustonliqmenu, \
    Zangiotamenu, Oqqurgonmenu, Ohangaronmenu, Parkentmenu, Piskentmenu, Chinozmenu, Yuqorichirchiqmenu, Yangiyulmenu, \
    Urtachirchiqmenu, Qibraymenu, Quyichirchiqmenu

from keyboards.inline.xorazm import xorazm_tumanlari, Urganchmenu, Yangibozormenu, Bogotmenu, Gurlanmenu, Qushkupirmenu, \
    Shovotmenu, Xazoraspmenu, Xivamenu, Xonqamenu, Yangiariqmenu


#     Qoraqalpog'iston respublikasi uchun

@dp.callback_query_handler(text="Qoraqalpogiston")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    

#    Nukus   tumani uchun

@dp.callback_query_handler(text="Nukus")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nukus/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Nukusmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nukusdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nukusdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Amudaryo  tumani uchun


@dp.callback_query_handler(text="Amudaryo")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/manghit/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Amudaryomenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    



@dp.callback_query_handler(text="Amudaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Amudaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Beruniy tumani uchun


@dp.callback_query_handler(text="Beruniy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beruniy-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Beruniymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    



@dp.callback_query_handler(text="Beruniydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Beruniydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Chimboy tumani uchun


@dp.callback_query_handler(text="Chimboy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chimbaj/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Chimboymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chimboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chimboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Elliktepa tumani uchun


@dp.callback_query_handler(text="Elliktepa")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/boston-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Elliktepamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Elliktepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Elliktepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Kegeyli tumani uchun


@dp.callback_query_handler(text="Kegeyli")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kegeyli-shahar/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kegeylimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kegeylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kegeylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Muynoq tumani uchun


@dp.callback_query_handler(text="Muynoq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muynoq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Muynoqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muynoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muynoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xujayli tumani uchun

@dp.callback_query_handler(text="Xujayli")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khujayli/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xujaylimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    

@dp.callback_query_handler(text="Xujaylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xujaylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Qonlikul tumani uchun


@dp.callback_query_handler(text="Qonlikul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qanlikol/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qonlikulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qonlikuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qonlikuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qorauzaq tumani uchun


@dp.callback_query_handler(text="Qorauzaq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qoraozak/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qorauzaqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    

@dp.callback_query_handler(text="Qorauzaqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qorauzaqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qungirot tumani uchun


@dp.callback_query_handler(text="Qungirot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qongirot-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qungirotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qungirotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qungirotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Shumanay tumani uchun


@dp.callback_query_handler(text="Shumanay")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shumanay-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shumanaymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shumanaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shumanaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Taxiatosh tumani uchun

@dp.callback_query_handler(text="Taxiatosh")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Taxiatoshmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Taxiatoshdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Taxiatoshdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Taxtakupir tumani uchun


@dp.callback_query_handler(text="Taxtakupir")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/taxtakopir/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Taxtakupirmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Taxtakupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Taxtakupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Turtkul tumani uchun


@dp.callback_query_handler(text="Turtkul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/novyy-turtkul/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Turtkulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Turtkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Turtkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    







#    Toshkent viloyati



@dp.callback_query_handler(text="Toshkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    



#    Toshkent   shahar uchun

@dp.callback_query_handler(text="Toshkent shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/tashkent/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Toshkentmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Toshkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Toshkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Bekobod  tumani uchun



@dp.callback_query_handler(text="Bekobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/bekobod/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bekobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bekoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bekoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Buka tumani uchun

@dp.callback_query_handler(text="Buka")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/buka/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bukamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bukadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bukadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Bustonliq tumani uchun


@dp.callback_query_handler(text="Bustonliq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tashkent/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bustonliqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
      

@dp.callback_query_handler(text="Bustonliqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bustonliqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Zangiota tumani uchun


@dp.callback_query_handler(text="Zangiota")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zangiata/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Zangiotamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
      


@dp.callback_query_handler(text="Zangiotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zangiotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Oqqurgon tumani uchun


@dp.callback_query_handler(text="Oqqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqqo-rg-on/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oqqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    

@dp.callback_query_handler(text="Oqqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oqqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Ohangaron tumani uchun


@dp.callback_query_handler(text="Ohangaron")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ohangaron/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Ohangaronmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    

@dp.callback_query_handler(text="Ohangarondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Ohangarondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Parkent tumani uchun



@dp.callback_query_handler(text="Parkent")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/parkent/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Parkentmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Parkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Parkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Piskent tumani uchun

@dp.callback_query_handler(text="Piskent")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/piskent/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Piskentmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Piskentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Piskentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Chinoz tumani uchun



@dp.callback_query_handler(text="Chinoz")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/chinoz/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Chinozmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    

@dp.callback_query_handler(text="Chinozdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chinozdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yuqorichirchiq tumani uchun



@dp.callback_query_handler(text="Yuqorichirchiq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yuqorichirchiqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    



@dp.callback_query_handler(text="Yuqorichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yuqorichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yangiyul tumani uchun


@dp.callback_query_handler(text="Yangiyul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/yangiyul/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangiyulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiyuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiyuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Urtachirchiq tumani uchun



@dp.callback_query_handler(text="Urtachirchiq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Urtachirchiqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Urtachirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Urtachirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qibray tumani uchun



@dp.callback_query_handler(text="Qibray")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo( "https://uz.meteotrend.com/week-forecast/uz/qibray/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qibraymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qibraydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qibraydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Quyichirchiq tumani uchun


@dp.callback_query_handler(text="Quyichirchiq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Quyichirchiqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quyichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quyichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    









#    Surxondaryo viloyati



@dp.callback_query_handler(text="Surxondaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


#    Termiz   tumani uchun


@dp.callback_query_handler(text="Termiz")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/termez/" ,id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Termizmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
       

@dp.callback_query_handler(text="Termizdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Termizdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Uzun  tumani uchun


@dp.callback_query_handler(text="Uzun")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/angor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uzunmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
      

@dp.callback_query_handler(text="Uzundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uzundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Angor tumani uchun


@dp.callback_query_handler(text="Angor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/angor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Angormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Angordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    
    


@dp.callback_query_handler(text="Angordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Bandixon tumani uchun


@dp.callback_query_handler(text="Bandixon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tashkent/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bandixonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bandixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bandixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Boysun tumani uchun


@dp.callback_query_handler(text="Boysun")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/termez/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Boysunmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Boysundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Boysundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Denov tumani uchun


@dp.callback_query_handler(text="Denov")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/denov/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Denovmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Denovdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Denovdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Jarqurgon tumani uchun


@dp.callback_query_handler(text="Jarqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/minor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Jarqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jarqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jarqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Muzrabot tumani uchun


@dp.callback_query_handler(text="Muzrabot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xalqobod_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Muzrabotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muzrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muzrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Oltinsoy tumani uchun


@dp.callback_query_handler(text="Oltinsoy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shorchi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oltinsoymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltinsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltinsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qiziriq tumani uchun


@dp.callback_query_handler(text="Qiziriq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sariq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qiziriqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qiziriqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qiziriqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Qumqurgon  tumani uchun


@dp.callback_query_handler(text="Qumqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sherobod/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qumqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qumqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qumqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Sariosiyo tumani uchun


@dp.callback_query_handler(text="Sariosiyo")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/denov/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Sariosiyomenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sariosiyodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sariosiyodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Sherobod tumani uchun


@dp.callback_query_handler(text="Sherobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sherobod/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Sherobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sheroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sheroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Shurchi tumani uchun


@dp.callback_query_handler(text="Shurchi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shorchi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shurchimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shurchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shurchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#    Andijon viloyati



@dp.callback_query_handler(text="Andijon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


#    Andijonshahar   tumani uchun


@dp.callback_query_handler(text="Andijon shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/andijon_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Andijonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Andijondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Andijondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Baliqchi  tumani uchun


@dp.callback_query_handler(text="Baliqchi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/baliqchi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Baliqchimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Baliqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Baliqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Buz tumani uchun


@dp.callback_query_handler(text="Buz")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bo-z/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Buzmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Buloqboshi tumani uchun

@dp.callback_query_handler(text="Buloqboshi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/buloqboshi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Buloqboshimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buloqboshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buloqboshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Izboskan tumani uchun


@dp.callback_query_handler(text="Izboskan")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/izboskan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Izboskanmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Izboskandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Izboskandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Jalolquduq tumani uchun

@dp.callback_query_handler(text="Jalolquduq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jalolquduq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Jalolquduqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jalolquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jalolquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Marhamat tumani uchun


@dp.callback_query_handler(text="Marhamat")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/marhamat/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Marhamatmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Marhamatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Marhamatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Oltinkul tumani uchun

@dp.callback_query_handler(text="Oltinkul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oltinko-l/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oltinkulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltinkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltinkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Paxtaobod tumani uchun


@dp.callback_query_handler(text="Paxtaobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/paxtaobod_5/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Paxtaobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qurgontepa tumani uchun

@dp.callback_query_handler(text="Qurgontepa")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qurghontepa/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qurgontepamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qurgontepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qurgontepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Shahrixon  tumani uchun

@dp.callback_query_handler(text="Shahrixon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shahrixon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shahrixonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shahrixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shahrixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Ulugnor tumani uchun


@dp.callback_query_handler(text="Ulugnor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqoltin/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Ulugnormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Ulugnordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Ulugnordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xujaobod tumani uchun

@dp.callback_query_handler(text="Xujaobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khujaobod/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xujaobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xujaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xujaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xonabod tumani uchun


@dp.callback_query_handler(text="Xonabod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xonobod_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xonabodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xonaboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xonaboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Asaka tumani uchun


@dp.callback_query_handler(text="Asaka")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/asaka/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Asakamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Asakadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Asakadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    





#    Buxoro viloyati



@dp.callback_query_handler(text="Buxoro")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


#    Buxoroshahar   tumani uchun


@dp.callback_query_handler(text="Buxoro shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/buhara/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Buxoromenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buxorodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buxorodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Gijduvon  tumani uchun


@dp.callback_query_handler(text="Gijduvon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ghijduwon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Gijduvonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gijduvondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gijduvondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Jondor tumani uchun


@dp.callback_query_handler(text="Jondor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jondor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Jondormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jondordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jondordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Kogon tumani uchun



@dp.callback_query_handler(text="Kogon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kogon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kogonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kogondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kogondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Olot tumani uchun



@dp.callback_query_handler(text="Olot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/olot/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Olotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Olotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Olotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Peshku tumani uchun


@dp.callback_query_handler(text="Peshku")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/peski/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Peshkumenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Peshkudan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Peshkudan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qorakul tumani uchun



@dp.callback_query_handler(text="Qorakul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karakul_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qorakulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qorakuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qorakuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Qorovulbozor  tumani uchun

@dp.callback_query_handler(text="Qorovulbozor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qorovulbozor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qorovulbozormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qorovulbozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qorovulbozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Romitan tumani uchun



@dp.callback_query_handler(text="Romitan")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/romiton/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Romitanmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Romitandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Romitandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Shofirkon tumani uchun



@dp.callback_query_handler(text="Shofirkon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shofirkon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shofirkonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shofirkondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shofirkondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Vobkent  tumani uchun


@dp.callback_query_handler(text="Vobkent")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/wobkent/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Vobkentmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Vobkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Vobkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#    Fargona viloyati



@dp.callback_query_handler(text="Fargona")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


#    Fargonashahar   tumani uchun



@dp.callback_query_handler(text="Fargona shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/fergana/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Fargonamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Fargonadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Fargonadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Yozyovon  tumani uchun


@dp.callback_query_handler(text="Yozyovon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yozyovon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yozyovonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yozyovondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yozyovondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Beshariq tumani uchun


@dp.callback_query_handler(text="Beshariq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beshariq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Beshariqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Beshariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Beshariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Bogdod tumani uchun


@dp.callback_query_handler(text="Bogdod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bag-dod/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bogdodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)

    


@dp.callback_query_handler(text="Bogdoddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bogdoddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Buvayda tumani uchun


@dp.callback_query_handler(text="Buvayda")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiqo-rg-on_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Buvaydamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buvaydadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Buvaydadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Dangara tumani uchun



@dp.callback_query_handler(text="Dangara")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/dang-ara/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Dangaramenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dangaradan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dangaradan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Furqat tumani uchun




@dp.callback_query_handler(text="Furqat")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/navbahor_3/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Furqatmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Furqatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Furqatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Uzbekiston tumani uchun


    


@dp.callback_query_handler(text="Uzbekiston")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/o-zbekiston/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uzbekistonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uzbekistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uzbekistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Oltiariq tumani uchun




@dp.callback_query_handler(text="Oltiariq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oltiariq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oltiariqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oltiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Quqon tumani uchun


@dp.callback_query_handler(text="Quqon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kokand/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Quqonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quqondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quqondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Qushtepa  tumani uchun


@dp.callback_query_handler(text="Qushtepa")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qo-shtepa/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qushtepamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushtepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushtepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Quva tumani uchun


@dp.callback_query_handler(text="Quva")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/quva/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Quvamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quvadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Quvadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Rishton tumani uchun



@dp.callback_query_handler(text="Rishton")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/rishton/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Rishtonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Rishtondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Rishtondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Sux tumani uchun



@dp.callback_query_handler(text="Sux")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ravon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Suxmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Suxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Suxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Toshloq tumani uchun


@dp.callback_query_handler(text="Toshloq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/toshloq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Toshloqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Toshloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Toshloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Uchkuprik tumani uchun



@dp.callback_query_handler(text="Uchkuprik")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchko-prik/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uchkuprikmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchkuprikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchkuprikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    






#    Jizzax viloyati



@dp.callback_query_handler(text="Jizzax")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


#    Jizzaxshahar   tumani uchun


@dp.callback_query_handler(text="Jizzax shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jizzakh/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Jizzaxmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jizzaxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jizzaxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Zomin tumani uchun



@dp.callback_query_handler(text="Zomin")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zomin/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Zominmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zomindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zomindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#     Arnasoy tumani uchun



@dp.callback_query_handler(text="Arnasoy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/g-oliblar/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Arnasoymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Arnasoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Arnasoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Baxmal tumani uchun


@dp.callback_query_handler(text="Baxmal")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/usmat-shaharchasi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Baxmalmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Baxmaldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Baxmaldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Dustlik tumani uchun

@dp.callback_query_handler(text="Dustlik")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/dustlik/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Dustlikmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dustlikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dustlikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Forish tumani uchun


@dp.callback_query_handler(text="Forish")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/gulzor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Forishmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Forishdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Forishdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Gallaorol tumani uchun

@dp.callback_query_handler(text="Gallaorol")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qoytosh/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Gallaorolmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gallaoroldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gallaoroldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Mirzachul tumani uchun


@dp.callback_query_handler(text="Mirzachul")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/mirzadala/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Mirzachulmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mirzachuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mirzachuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Paxtakor tumani uchun



@dp.callback_query_handler(text="Paxtakor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/paxtakor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Paxtakormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtakordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtakordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yangiobod tumani uchun



@dp.callback_query_handler(text="Yangiobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiqishloq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangiobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangioboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangioboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Zafarobod  tumani uchun


@dp.callback_query_handler(text="Zafarobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zafarobod/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Zafarobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zafaroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zafaroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Zarband tumani uchun



@dp.callback_query_handler(text="Zarband")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zarbdor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Zarbandmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zarbanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zarbanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    







#    Xorazm viloyati



@dp.callback_query_handler(text="Xorazm")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


#    Urganch   shahar uchun

@dp.callback_query_handler(text="Urganch")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Urganchmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)

    


@dp.callback_query_handler(text="Urganchdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Urganchdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yangibozor tumani uchun



@dp.callback_query_handler(text="Yangibozor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangibozormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangibozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangibozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Bogot   tumani uchun


@dp.callback_query_handler(text="Bogot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bogotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bogotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bogotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Gurlan tumani uchun



@dp.callback_query_handler(text="Gurlan")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/gurlan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Gurlanmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gurlandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gurlandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Qushkupir tumani uchun


@dp.callback_query_handler(text="Qushkupir")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qushkupir/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qushkupirmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushkupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushkupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Shovot tumani uchun




@dp.callback_query_handler(text="Shovot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/showot/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shovotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shovotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shovotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xazorasp tumani uchun



@dp.callback_query_handler(text="Xazorasp")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/hazorasp/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xazoraspmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xazoraspdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xazoraspdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xiva tumani uchun


@dp.callback_query_handler(text="Xiva")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khiva/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xivamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xivadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xivadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Xonqa tumani uchun


@dp.callback_query_handler(text="Xonqa")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xonqamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xonqadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xonqadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yangiariq tumani uchun


@dp.callback_query_handler(text="Yangiariq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiariq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangiariqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#    Namangan viloyati



@dp.callback_query_handler(text="Namangan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


#    Namanganshahri   shahar  uchun


@dp.callback_query_handler(text="Namangan shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/namangan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Namanganmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Namangandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Namangandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Chortoq tumani uchun


@dp.callback_query_handler(text="Chortoq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chortoq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Chortoqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chortoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chortoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Chust   tumani uchun


@dp.callback_query_handler(text="Chust")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chust-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Chustmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chustdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chustdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Kosonsoy tumani uchun

@dp.callback_query_handler(text="Kosonsoy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/namangan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kosonsoymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosonsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kosonsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Mingbuloq tumani uchun


@dp.callback_query_handler(text="Mingbuloq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jomasho-y/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Mingbuloqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mingbuloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mingbuloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Norin tumani uchun


@dp.callback_query_handler(text="Norin")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/norinkapa/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Norinmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Norindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Norindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Pop tumani uchun


@dp.callback_query_handler(text="Pop")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/pop/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Popmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Popdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Popdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Turaqurgon tumani uchun


@dp.callback_query_handler(text="Turaqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/turagurghon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Turaqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Turaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Turaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Uchqurgon tumani uchun


@dp.callback_query_handler(text="Uchqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchqurghon-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uchqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Uychi tumani uchun


@dp.callback_query_handler(text="Uychi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uychi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uychimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uychidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uychidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Yangiqurgon tumani uchun


@dp.callback_query_handler(text="Yangiqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/namangan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangiqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    









#    Navoiy viloyati



@dp.callback_query_handler(text="Navoiy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


#    Navoiyshahri   shahar  uchun


@dp.callback_query_handler(text="Navoiy shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/navoiy/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Navoiymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Navoiydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Navoiydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Zarafshon  tumani uchun

@dp.callback_query_handler(text="Zarafshon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zarafshan/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Zarafshonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zarafshondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Zarafshondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Karmana   tumani uchun

@dp.callback_query_handler(text="Karmana")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karmana-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Karmanamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Karmanadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Karmanadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Konimex tumani uchun


@dp.callback_query_handler(text="Konimex")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/konimex/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Konimexmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Konimexdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Konimexdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Navbahor tumani uchun
  


@dp.callback_query_handler(text="Navbahor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beshrabot/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Navbahormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Navbahordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Navbahordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Nurota tumani uchun


@dp.callback_query_handler(text="Nurota")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nurata/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Nurotamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nurotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nurotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qiziltepa tumani uchun


@dp.callback_query_handler(text="Qiziltepa")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qiziltepa/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qiziltepamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qiziltepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qiziltepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Tomdi tumani uchun



@dp.callback_query_handler(text="Tomdi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tomdibuloq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Tomdimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Tomdidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Tomdidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Uchquduq tumani uchun



@dp.callback_query_handler(text="Uchquduq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchquduq-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Uchquduqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Uchquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Xatirchi tumani uchun



@dp.callback_query_handler(text="Xatirchi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangirabot/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xatirchimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xatirchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xatirchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    







#    Qashqadaryo viloyati



@dp.callback_query_handler(text="Qashqadaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


#    Qarshi   shahar  uchun


@dp.callback_query_handler(text="Qarshi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karshi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qarshimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qarshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qarshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Chiroqchi  tumani uchun



@dp.callback_query_handler(text="Chiroqchi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chiroqchi/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Chiroqchimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chiroqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Chiroqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Dehqonobod   tumani uchun



@dp.callback_query_handler(text="Dehqonobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qiziltepa_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Dehqonobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dehqonoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Dehqonoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Guzor tumani uchun


@dp.callback_query_handler(text="Guzor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/guzor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Guzormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Guzordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Guzordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Kasbi tumani uchun



@dp.callback_query_handler(text="Kasbi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muglon-shahar/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kasbimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kasbidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kasbidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Kitob tumani uchun



@dp.callback_query_handler(text="Kitob")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kitob/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kitobmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kitobdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kitobdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#    Koson  tumani uchun



@dp.callback_query_handler(text="Koson")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/koson-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kosonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kosondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kosondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Mirishkor tumani uchun



@dp.callback_query_handler(text="Mirishkor")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangi-mirishkor/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Mirishkormenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mirishkordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Mirishkordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Muborak tumani uchun



@dp.callback_query_handler(text="Muborak")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muborak-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Muborakmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muborakdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Muborakdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Nishon tumani uchun



@dp.callback_query_handler(text="Nishon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nishon-tumani/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Nishonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nishondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nishondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Qamashi tumani uchun



@dp.callback_query_handler(text="Qamashi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qamashi-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qamashimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qamashidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qamashidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Shahrisabz tumani uchun



@dp.callback_query_handler(text="Shahrisabz")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shahrisabz/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Shahrisabzmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shahrisabzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Shahrisabzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yakkabog tumani uchun



@dp.callback_query_handler(text="Yakkabog")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yakkabog-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yakkabogmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yakkabogdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yakkabogdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    












#    Samarqand viloyati



@dp.callback_query_handler(text="Samarqand")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


#    Samarqand   shahar  uchun


@dp.callback_query_handler(text="Samarqand shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/samarkand/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Samarqandmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Samarqanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Samarqanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Urgut  tumani uchun



@dp.callback_query_handler(text="Urgut")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/toyloq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Urgutmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Urgutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Urgutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Bulungur   tumani uchun




@dp.callback_query_handler(text="Bulungur")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bulungur/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Bulungurmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bulungurdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Bulungurdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Ishtixon tumani uchun

    


@dp.callback_query_handler(text="Ishtixon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ishtixon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Ishtixonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Ishtixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Ishtixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Jomboy tumani uchun




@dp.callback_query_handler(text="Jomboy")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jomboy/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Jomboymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jomboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Jomboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Kattaqurgon tumani uchun




@dp.callback_query_handler(text="Kattaqurgon")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kattaqorgon/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Kattaqurgonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kattaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Kattaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#    Narpay  tumani uchun


@dp.callback_query_handler(text="Narpay")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqtosh/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Narpaymenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Narpaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Narpaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Nurobod tumani uchun



@dp.callback_query_handler(text="Nurobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/samarkand/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Nurobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nuroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Nuroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Oqdaryo tumani uchun




@dp.callback_query_handler(text="Oqdaryo")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/loyish/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oqdaryomenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oqdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oqdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Pastdargom tumani uchun


    


@dp.callback_query_handler(text="Pastdargom")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/samarkand/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Pastdargommenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Pastdargomdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Pastdargomdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Paxtachi tumani uchun


    


@dp.callback_query_handler(text="Paxtachi")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ziyodin/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Paxtachimenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtachidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Paxtachidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Poyariq tumani uchun




@dp.callback_query_handler(text="Poyariq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/payariq-shahri/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Poyariqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Poyariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Poyariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Qushrabot tumani uchun



@dp.callback_query_handler(text="Qushrabot")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qushrabot/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Qushrabotmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Qushrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    






#   Tayloq tumani uchun

    


@dp.callback_query_handler(text="Tayloq")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/toyloq/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Tayloqmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Tayloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Tayloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    





#    Sirdaryo viloyati



@dp.callback_query_handler(text="Sirdaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


#    Sirdaryo   shahar  uchun


    


@dp.callback_query_handler(text="Sirdaryo shahar")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sirdaryo_2/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Sirdaryomenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sirdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sirdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#  Boyovut  tumani uchun



@dp.callback_query_handler(text="Boyovut")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/boyovut/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Boyovutmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Boyovutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Boyovutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Guliston   tumani uchun



@dp.callback_query_handler(text="Guliston")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/guliston/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Gulistonmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gulistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Gulistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Oqoltin tumani uchun



@dp.callback_query_handler(text="Oqoltin")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqoltin_3/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Oqoltinmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oqoltindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Oqoltindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    




#   Sardoba  tumani uchun



@dp.callback_query_handler(text="Sardoba")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sardoba/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Sardobamenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sardobadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sardobadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    



#   Sayxunobod tumani uchun

@dp.callback_query_handler(text="Sayxunobod")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sayxun/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Sayxunobodmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sayxunoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Sayxunoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#    Xavos  tumani uchun


@dp.callback_query_handler(text="Xavos")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xovos/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Xavosmenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xavosdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Xavosdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    


#   Yangiyer tumani uchun


@dp.callback_query_handler(text="Yangiyer")
async def buy_courses(call: CallbackQuery):
    id = call.data
    haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jangier/",id)
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.jpg")
    await call.message.answer_photo(rasm, reply_markup=Yangiyermenu)
    await call.message.delete()
    os.remove(f"rasmlar/{id}.jpg")
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiyerdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)
    


@dp.callback_query_handler(text="Yangiyerdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    









@dp.callback_query_handler(text="🔙Ortga")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)
    





