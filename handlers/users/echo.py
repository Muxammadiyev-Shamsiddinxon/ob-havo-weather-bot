from handlers.bugunobhavo import bugun_obhavo
from handlers.haftalikobhavo import haftalik_obhavo
from loader import dp



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
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nukusmenu)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text="Nukus Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Nukusmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nukus Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nukus/")
    await call.message.answer(xabar, reply_markup=Nukusmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nukusdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nukusdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Amudaryo  tumani uchun

@dp.callback_query_handler(text="Amudaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Amudaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Amudaryo Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/mangit/355693/current-weather/355693")
    await call.message.answer(xabar, reply_markup=Amudaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Amudaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/manghit/")
    await call.message.answer(xabar, reply_markup=Amudaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Amudaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Amudaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Beruniy tumani uchun

@dp.callback_query_handler(text="Beruniy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Beruniymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beruniy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beruni/355684/current-weather/355684")
    await call.message.answer(xabar, reply_markup=Beruniymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beruniy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beruniy-shahri/")
    await call.message.answer(xabar, reply_markup=Beruniymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beruniydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    #await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beruniydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Chimboy tumani uchun

@dp.callback_query_handler(text="Chimboy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chimboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chimboy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chimbay/355669/current-weather/355669")
    await call.message.answer(xabar, reply_markup=Chimboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chimboy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chimbaj/")
    await call.message.answer(xabar, reply_markup=Chimboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chimboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chimboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Elliktepa tumani uchun

@dp.callback_query_handler(text="Elliktepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Elliktepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Elliktepa Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ellikkala/721481/current-weather/721481")
    await call.message.answer(xabar, reply_markup=Elliktepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Elliktepa Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/boston-shahri/")
    await call.message.answer(xabar, reply_markup=Elliktepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Elliktepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Elliktepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Kegeyli tumani uchun

@dp.callback_query_handler(text="Kegeyli")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kegeylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kegeyli Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kegeyli/355689/current-weather/355689")
    await call.message.answer(xabar, reply_markup=Kegeylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kegeyli Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kegeyli-shahar/")
    await call.message.answer(xabar, reply_markup=Kegeylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kegeylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kegeylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Muynoq tumani uchun

@dp.callback_query_handler(text="Muynoq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muynoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muynoq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/muynoq/355668/current-weather/355668")
    await call.message.answer(xabar, reply_markup=Muynoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muynoq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muynoq/")
    await call.message.answer(xabar, reply_markup=Muynoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muynoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muynoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xujayli tumani uchun

@dp.callback_query_handler(text="Xujayli")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xujaylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujayli Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khujayli/355667/current-weather/355667")
    await call.message.answer(xabar, reply_markup=Xujaylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujayli Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khujayli/")
    await call.message.answer(xabar, reply_markup=Xujaylimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujaylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujaylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Qonlikul tumani uchun

@dp.callback_query_handler(text="Qonlikul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qonlikulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qonlikul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Qonlikulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qonlikul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qanlikol/")
    await call.message.answer(xabar, reply_markup=Qonlikulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qonlikuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qonlikuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qorauzaq tumani uchun

@dp.callback_query_handler(text="Qorauzaq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorauzaq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karauzyak/355688/current-weather/355688")
    await call.message.answer(xabar, reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorauzaq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qoraozak/")
    await call.message.answer(xabar, reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorauzaqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorauzaqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qungirot tumani uchun

@dp.callback_query_handler(text="Qungirot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qungirotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qungirot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kungrad/355670/current-weather/355670")
    await call.message.answer(xabar, reply_markup=Qungirotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qungirot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qongirot-shahri/")
    await call.message.answer(xabar, reply_markup=Qungirotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qungirotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qungirotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Shumanay tumani uchun

@dp.callback_query_handler(text="Shumanay")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shumanaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shumanay Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shumanay/355682/current-weather/355682")
    await call.message.answer(xabar, reply_markup=Shumanaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shumanay Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shumanay-shahri/")
    await call.message.answer(xabar, reply_markup=Shumanaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shumanaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shumanaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Taxiatosh tumani uchun

@dp.callback_query_handler(text="Taxiatosh")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxiatosh Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/takhiatash/355671/current-weather/355671")
    await call.message.answer(xabar, reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxiatosh Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/")
    await call.message.answer(xabar, reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxiatoshdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxiatoshdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Taxtakupir tumani uchun

@dp.callback_query_handler(text="Taxtakupir")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxtakupir Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tahtakupyr/355672/current-weather/355672")
    await call.message.answer(xabar, reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxtakupir Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/taxtakopir/")
    await call.message.answer(xabar, reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxtakupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Taxtakupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Turtkul tumani uchun

@dp.callback_query_handler(text="Turtkul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Turtkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turtkul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/turtkul/355695/current-weather/355695")
    await call.message.answer(xabar, reply_markup=Turtkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turtkul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/novyy-turtkul/")
    await call.message.answer(xabar, reply_markup=Turtkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turtkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turtkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)







#    Toshkent viloyati



@dp.callback_query_handler(text="Toshkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)



#    Toshkent   tumani uchun

@dp.callback_query_handler(text="Toshkentshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Toshkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshkent Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tashkent/351199/current-weather/351199")
    await call.message.answer(xabar, reply_markup=Toshkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshkent Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tashkent/")
    await call.message.answer(xabar, reply_markup=Toshkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Bekobod  tumani uchun

@dp.callback_query_handler(text="Bekobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bekobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bekobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bekabad/356235/current-weather/356235")
    await call.message.answer(xabar, reply_markup=Bekobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bekobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bekobod/")
    await call.message.answer(xabar, reply_markup=Bekobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bekoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bekoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Buka tumani uchun

@dp.callback_query_handler(text="Buka")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bukamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buka Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/buka/356221/current-weather/356221")
    await call.message.answer(xabar, reply_markup=Bukamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buka Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/buka/")
    await call.message.answer(xabar, reply_markup=Bukamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bukadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bukadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Bustonliq tumani uchun

@dp.callback_query_handler(text="Bustonliq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bustonliqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bustonliq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gazalkent/356239/current-weather/356239")
    await call.message.answer(xabar, reply_markup=Bustonliqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bustonliq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tashkent/")
    await call.message.answer(xabar, reply_markup=Bustonliqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bustonliqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bustonliqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Zangiota tumani uchun

@dp.callback_query_handler(text="Zangiota")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zangiotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zangiota Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/eshongyzar/356224/current-weather/356224")
    await call.message.answer(xabar, reply_markup=Zangiotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zangiota Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zangiata/")
    await call.message.answer(xabar, reply_markup=Zangiotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zangiotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zangiotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Oqqurgon tumani uchun

@dp.callback_query_handler(text="Oqqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/akkurgan/356220/current-weather/356220")
    await call.message.answer(xabar, reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqqo-rg-on/")
    await call.message.answer(xabar, reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Ohangaron tumani uchun

@dp.callback_query_handler(text="Ohangaron")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ohangaronmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ohangaron Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kurama/356247/current-weather/356247")
    await call.message.answer(xabar, reply_markup=Ohangaronmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ohangaron Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ohangaron/")
    await call.message.answer(xabar, reply_markup=Ohangaronmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ohangarondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ohangarondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Parkent tumani uchun

@dp.callback_query_handler(text="Parkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Parkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Parkent Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/current-weather/356240")
    await call.message.answer(xabar, reply_markup=Parkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Parkent Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/parkent/")
    await call.message.answer(xabar, reply_markup=Parkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Parkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Parkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Piskent tumani uchun

@dp.callback_query_handler(text="Piskent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Piskentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Piskent Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/current-weather/356240")
    await call.message.answer(xabar, reply_markup=Piskentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Piskent Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/piskent/")
    await call.message.answer(xabar, reply_markup=Piskentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Piskentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Piskentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Chinoz tumani uchun

@dp.callback_query_handler(text="Chinoz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chinozmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chinoz Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chinoz/356222/current-weather/356222")
    await call.message.answer(xabar, reply_markup=Chinozmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chinoz Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chinoz/")
    await call.message.answer(xabar, reply_markup=Chinozmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chinozdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chinozdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yuqorichirchiq tumani uchun

@dp.callback_query_handler(text="Yuqorichirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yuqorichirchiq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirchik/356238/current-weather/356238")
    await call.message.answer(xabar, reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yuqorichirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/")
    await call.message.answer(xabar, reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yuqorichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yuqorichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yangiyul tumani uchun

@dp.callback_query_handler(text="Yangiyul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiyulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356245/current-weather/356245")
    await call.message.answer(xabar, reply_markup=Yangiyulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiyul/")
    await call.message.answer(xabar, reply_markup=Yangiyulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Urtachirchiq tumani uchun

@dp.callback_query_handler(text="Urtachirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urtachirchiq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tashkent/356223/current-weather/356223")
    await call.message.answer(xabar, reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urtachirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/")
    await call.message.answer(xabar, reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urtachirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urtachirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qibray tumani uchun

@dp.callback_query_handler(text="Qibray")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qibraymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qibray Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qibray/356227/current-weather/356227")
    await call.message.answer(xabar, reply_markup=Qibraymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qibray Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qibray/")
    await call.message.answer(xabar, reply_markup=Qibraymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qibraydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qibraydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Quyichirchiq tumani uchun

@dp.callback_query_handler(text="Quyichirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quyichirchiq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tashkent/356223/current-weather/356223")
    await call.message.answer(xabar, reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quyichirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_3/")
    await call.message.answer(xabar, reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quyichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quyichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
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
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Termizmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Termiz Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/termez/356042/current-weather/356042")
    await call.message.answer(xabar, reply_markup=Termizmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Termiz Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/termez/")
    await call.message.answer(xabar, reply_markup=Termizmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Termizdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Termizdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Uzun  tumani uchun

@dp.callback_query_handler(text="Uzun")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uzunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzun Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uzun/356054/current-weather/356054")
    await call.message.answer(xabar, reply_markup=Uzunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzun Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uzun/")
    await call.message.answer(xabar, reply_markup=Uzunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Angor tumani uchun

@dp.callback_query_handler(text="Angor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Angormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Angor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/angor/356043/current-weather/356043")
    await call.message.answer(xabar, reply_markup=Angormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Angor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/angor/")
    await call.message.answer(xabar, reply_markup=Angormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Angordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Angordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Bandixon tumani uchun

@dp.callback_query_handler(text="Bandixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bandixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bandixon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bandy-khan/356044/current-weather/356044")
    await call.message.answer(xabar, reply_markup=Bandixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bandixon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tashkent/")
    await call.message.answer(xabar, reply_markup=Bandixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bandixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bandixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Boysun tumani uchun

@dp.callback_query_handler(text="Boysun")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Boysunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boysun Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/baysun/356058/current-weather/356058")
    await call.message.answer(xabar, reply_markup=Boysunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boysun Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/boysun/")
    await call.message.answer(xabar, reply_markup=Boysunmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boysundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boysundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Denov tumani uchun

@dp.callback_query_handler(text="Denov")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Denovmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Denov Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/denau/356059/current-weather/356059")
    await call.message.answer(xabar, reply_markup=Denovmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Denov Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/denov/")
    await call.message.answer(xabar, reply_markup=Denovmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Denovdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Denovdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Jarqurgon tumani uchun

@dp.callback_query_handler(text="Jarqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jarqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jarkurghon/356047/weather-forecast/356047")
    await call.message.answer(xabar, reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jarqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/minor/")
    await call.message.answer(xabar, reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jarqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jarqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Muzrabot tumani uchun

@dp.callback_query_handler(text="Muzrabot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muzrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muzrabot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zang/356056/current-weather/356056")
    await call.message.answer(xabar, reply_markup=Muzrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muzrabot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xalqobod_2/")
    await call.message.answer(xabar, reply_markup=Muzrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muzrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muzrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Oltinsoy tumani uchun

@dp.callback_query_handler(text="Oltinsoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltinsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinsoy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karluk/356048/current-weather/356048")
    await call.message.answer(xabar, reply_markup=Oltinsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinsoy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shorchi/")
    await call.message.answer(xabar, reply_markup=Oltinsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qiziriq tumani uchun

@dp.callback_query_handler(text="Qiziriq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qiziriqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziriq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356055/current-weather/356055")
    await call.message.answer(xabar, reply_markup=Qiziriqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziriq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sariq/")
    await call.message.answer(xabar, reply_markup=Qiziriqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziriqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziriqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Qumqurgon  tumani uchun

@dp.callback_query_handler(text="Qumqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qumqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kumkurgan/356049/current-weather/356049")
    await call.message.answer(xabar, reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qumqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sherobod/")
    await call.message.answer(xabar, reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qumqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qumqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Sariosiyo tumani uchun

@dp.callback_query_handler(text="Sariosiyo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sariosiyomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sariosiyo Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sariasiya/356052/current-weather/356052")
    await call.message.answer(xabar, reply_markup=Sariosiyomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sariosiyo Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sariosiyo_2/")
    await call.message.answer(xabar, reply_markup=Sariosiyomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sariosiyodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sariosiyodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Sherobod tumani uchun

@dp.callback_query_handler(text="Sherobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sherobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sherobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("accuweather.com/uz/uz/sherabad/356053/current-weather/356053")
    await call.message.answer(xabar, reply_markup=Sherobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sherobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sherobod/")
    await call.message.answer(xabar, reply_markup=Sherobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sheroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sheroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Shurchi tumani uchun

@dp.callback_query_handler(text="Shurchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shurchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shurchi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shurchi/356063/current-weather/356063")
    await call.message.answer(xabar, reply_markup=Shurchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shurchi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shorchi/")
    await call.message.answer(xabar, reply_markup=Shurchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shurchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shurchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#    Andijon viloyati



@dp.callback_query_handler(text="Andijon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


#    Andijonshahar   tumani uchun

@dp.callback_query_handler(text="Andijonshahar")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Andijonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Andijon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/andijan/351828/current-weather/351828")
    await call.message.answer(xabar, reply_markup=Andijonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Andijon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/andijon_2/")
    await call.message.answer(xabar, reply_markup=Andijonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Andijondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Andijondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Baliqchi  tumani uchun

@dp.callback_query_handler(text="Baliqchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Baliqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baliqchi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/balykchi/351833/current-weather/351833")
    await call.message.answer(xabar, reply_markup=Baliqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baliqchi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/baliqchi/")
    await call.message.answer(xabar, reply_markup=Baliqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baliqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baliqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Buz tumani uchun

@dp.callback_query_handler(text="Buz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buz Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/boz/351834/current-weather/351834")
    await call.message.answer(xabar, reply_markup=Buzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buz Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bo-z/")
    await call.message.answer(xabar, reply_markup=Buzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Buloqboshi tumani uchun

@dp.callback_query_handler(text="Buloqboshi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buloqboshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buloqboshi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bulakbashi/351835/current-weather/351835")
    await call.message.answer(xabar, reply_markup=Buloqboshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buloqboshi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/buloqboshi/")
    await call.message.answer(xabar, reply_markup=Buloqboshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buloqboshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buloqboshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Izboskan tumani uchun

@dp.callback_query_handler(text="Izboskan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Izboskanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Izboskan Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/izbaskan/721284/current-weather/721284")
    await call.message.answer(xabar, reply_markup=Izboskanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Izboskan Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/izboskan/")
    await call.message.answer(xabar, reply_markup=Izboskanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Izboskandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Izboskandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Jalolquduq tumani uchun

@dp.callback_query_handler(text="Jalolquduq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jalolquduq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ahunbabayev/351831/current-weather/351831")
    await call.message.answer(xabar, reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jalolquduq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jalolquduq/")
    await call.message.answer(xabar, reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jalolquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jalolquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Marhamat tumani uchun

@dp.callback_query_handler(text="Marhamat")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Marhamatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Marhamat Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/marhamat/351840/current-weather/351840")
    await call.message.answer(xabar, reply_markup=Marhamatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Marhamat Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/marhamat/")
    await call.message.answer(xabar, reply_markup=Marhamatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Marhamatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Marhamatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Oltinkul tumani uchun

@dp.callback_query_handler(text="Oltinkul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltinkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinkul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/altynkul/351832/current-weather/351832")
    await call.message.answer(xabar, reply_markup=Oltinkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinkul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oltinko-l/")
    await call.message.answer(xabar, reply_markup=Oltinkulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltinkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Paxtaobod tumani uchun

@dp.callback_query_handler(text="Paxtaobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtaobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pakhtaabad/351844/current-weather/351844")
    await call.message.answer(xabar, reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtaobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/paxtaobod_5/")
    await call.message.answer(xabar, reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qurgontepa tumani uchun

@dp.callback_query_handler(text="Qurgontepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qurgontepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qurgontepa Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kurgantepa/351843/current-weather/351843")
    await call.message.answer(xabar, reply_markup=Qurgontepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qurgontepa Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qurghontepa/")
    await call.message.answer(xabar, reply_markup=Qurgontepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qurgontepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qurgontepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Shahrixon  tumani uchun

@dp.callback_query_handler(text="Shahrixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shahrixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrixon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shakhrikhan/351845/current-weather/351845")
    await call.message.answer(xabar, reply_markup=Shahrixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrixon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shahrixon/")
    await call.message.answer(xabar, reply_markup=Shahrixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Ulugnor tumani uchun

@dp.callback_query_handler(text="Ulugnor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ulugnormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ulugnor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/akaltyn/351830/current-weather/351830")
    await call.message.answer(xabar, reply_markup=Ulugnormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ulugnor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqoltin/")
    await call.message.answer(xabar, reply_markup=Ulugnormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ulugnordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ulugnordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xujaobod tumani uchun

@dp.callback_query_handler(text="Xujaobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xujaobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujaobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khodzhaabad/351838/current-weather/351838")
    await call.message.answer(xabar, reply_markup=Xujaobodmenu)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text="Xujaobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khujaobod/")
    await call.message.answer(xabar, reply_markup=Xujaobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xujaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xonabod tumani uchun

@dp.callback_query_handler(text="Xonabod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xonabodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonabod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khanabadskiy/351837/current-weather/351837")
    await call.message.answer(xabar, reply_markup=Xonabodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonabod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xonobod_2/")
    await call.message.answer(xabar, reply_markup=Xonabodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonaboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonaboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Asaka tumani uchun

@dp.callback_query_handler(text="Asaka")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Asakamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Asaka Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/assake/351846/current-weather/351846")
    await call.message.answer(xabar, reply_markup=Asakamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Asaka Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/asaka/")
    await call.message.answer(xabar, reply_markup=Asakamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Asakadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Asakadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)





#    Buxoro viloyati



@dp.callback_query_handler(text="Buxoro")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


#    Buxoroshahar   tumani uchun

@dp.callback_query_handler(text="Buxoroshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buxoromenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buxoro Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bukhara/352479/current-weather/352479")
    await call.message.answer(xabar, reply_markup=Buxoromenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buxoro Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/buhara/")
    await call.message.answer(xabar, reply_markup=Buxoromenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buxorodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buxorodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Gijduvon  tumani uchun

@dp.callback_query_handler(text="Gijduvon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gijduvonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gijduvon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gizhduvan/352490/current-weather/352490")
    await call.message.answer(xabar, reply_markup=Gijduvonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gijduvon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ghijduwon/")
    await call.message.answer(xabar, reply_markup=Gijduvonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gijduvondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gijduvondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Jondor tumani uchun

@dp.callback_query_handler(text="Jondor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jondormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jondor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zhondor/352486/current-weather/352486")
    await call.message.answer(xabar, reply_markup=Jondormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jondor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jondor/")
    await call.message.answer(xabar, reply_markup=Jondormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jondordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jondordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Kogon tumani uchun

@dp.callback_query_handler(text="Kogon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kogonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kogon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kagan/352492/current-weather/352492")
    await call.message.answer(xabar, reply_markup=Kogonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kogon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kogon/")
    await call.message.answer(xabar, reply_markup=Kogonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kogondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kogondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Olot tumani uchun

@dp.callback_query_handler(text="Olot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Olotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Olot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/alat/352480/current-weather/352480")
    await call.message.answer(xabar, reply_markup=Olotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Olot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/olot/")
    await call.message.answer(xabar, reply_markup=Olotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Olotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Olotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Peshku tumani uchun

@dp.callback_query_handler(text="Peshku")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Peshkumenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Peshku Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/peshku/720257/current-weather/720257")
    await call.message.answer(xabar, reply_markup=Peshkumenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Peshku Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/peski/")
    await call.message.answer(xabar, reply_markup=Peshkumenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Peshkudan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Peshkudan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qorakul tumani uchun

@dp.callback_query_handler(text="Qorakul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorakulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorakul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karakul/352482/current-weather/352482")
    await call.message.answer(xabar, reply_markup=Qorakulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorakul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karakul_2/")
    await call.message.answer(xabar, reply_markup=Qorakulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorakuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorakuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Qorovulbozor  tumani uchun

@dp.callback_query_handler(text="Qorovulbozor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorovulbozor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karaulbazar/352484/current-weather/352484")
    await call.message.answer(xabar, reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorovulbozor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qorovulbozor/")
    await call.message.answer(xabar, reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorovulbozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qorovulbozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Romitan tumani uchun

@dp.callback_query_handler(text="Romitan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Romitanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Romitan Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/romiton/720199/current-weather/720199")
    await call.message.answer(xabar, reply_markup=Romitanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Romitan Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/romiton/")
    await call.message.answer(xabar, reply_markup=Romitanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Romitandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Romitandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Shofirkon tumani uchun

@dp.callback_query_handler(text="Shofirkon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shofirkonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shofirkon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shafirkan/352494/current-weather/352494")
    await call.message.answer(xabar, reply_markup=Shofirkonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shofirkon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shofirkon/")
    await call.message.answer(xabar, reply_markup=Shofirkonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shofirkondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shofirkondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Vobkent  tumani uchun

@dp.callback_query_handler(text="Vobkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Vobkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Vobkent Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/vabkent/352496/current-weather/352496")
    await call.message.answer(xabar, reply_markup=Vobkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Vobkent Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/wobkent/")
    await call.message.answer(xabar, reply_markup=Vobkentmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Vobkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Vobkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#    Fargona viloyati



@dp.callback_query_handler(text="Fargona")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


#    Fargonashahar   tumani uchun

@dp.callback_query_handler(text="Fargonashahar")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Fargonamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Fargona Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/fergana/353238/current-weather/353238")
    await call.message.answer(xabar, reply_markup=Fargonamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Fargona Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/fergana/")
    await call.message.answer(xabar, reply_markup=Fargonamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Fargonadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Fargonadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Yozyovon  tumani uchun

@dp.callback_query_handler(text="Yozyovon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yozyovonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yozyovon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yaz%E2%80%9Dyavan/353257/current-weather/353257")
    await call.message.answer(xabar, reply_markup=Yozyovonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yozyovon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yozyovon/")
    await call.message.answer(xabar, reply_markup=Yozyovonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yozyovondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yozyovondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Beshariq tumani uchun

@dp.callback_query_handler(text="Beshariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Beshariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beshariq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beshariq/353247/current-weather/353247")
    await call.message.answer(xabar, reply_markup=Beshariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beshariq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beshariq/")
    await call.message.answer(xabar, reply_markup=Beshariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beshariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Beshariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Bogdod tumani uchun

@dp.callback_query_handler(text="Bogdod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bogdodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogdod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bagdod/721991/current-weather/721991")
    await call.message.answer(xabar, reply_markup=Bogdodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogdod Haftalik")
async def buy_courses(call: CallbackQuery):
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bag-dod/")
    await call.message.answer(xabar, reply_markup=Bogdodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogdoddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogdoddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Buvayda tumani uchun

@dp.callback_query_handler(text="Buvayda")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buvaydamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buvayda Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/buvayda/721803/current-weather/721803")
    await call.message.answer(xabar, reply_markup=Buvaydamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buvayda Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiqo-rg-on_2/")
    await call.message.answer(xabar, reply_markup=Buvaydamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buvaydadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Buvaydadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Dangara tumani uchun

@dp.callback_query_handler(text="Dangara")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dangaramenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dangara Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dangara/353248/current-weather/353248")
    await call.message.answer(xabar, reply_markup=Dangaramenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dangara Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/dang-ara/")
    await call.message.answer(xabar, reply_markup=Dangaramenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dangaradan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dangaradan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Furqat tumani uchun

@dp.callback_query_handler(text="Furqat")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Furqatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Furqat Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nawbahor/353251/current-weather/353251")
    await call.message.answer(xabar, reply_markup=Furqatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Furqat Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/navbahor_3/")
    await call.message.answer(xabar, reply_markup=Furqatmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Furqatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Furqatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Uzbekiston tumani uchun

@dp.callback_query_handler(text="Uzbekiston")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzbekiston Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yaypan/353262/current-weather/353262")
    await call.message.answer(xabar, reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzbekiston Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/o-zbekiston/")
    await call.message.answer(xabar, reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzbekistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uzbekistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Oltiariq tumani uchun

@dp.callback_query_handler(text="Oltiariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltiariq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/altyaryk/353245/current-weather/353245")
    await call.message.answer(xabar, reply_markup=Oltiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltiariq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oltiariq/")
    await call.message.answer(xabar, reply_markup=Oltiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oltiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Quqon tumani uchun

@dp.callback_query_handler(text="Quqon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quqonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quqon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kokand/353243/current-weather/353243")
    await call.message.answer(xabar, reply_markup=Quqonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quqon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kokand/")
    await call.message.answer(xabar, reply_markup=Quqonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quqondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quqondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Qushtepa  tumani uchun

@dp.callback_query_handler(text="Qushtepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushtepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushtepa Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/langar/1704277/current-weather/1704277")
    await call.message.answer(xabar, reply_markup=Qushtepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushtepa Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qo-shtepa/")
    await call.message.answer(xabar, reply_markup=Qushtepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushtepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushtepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Quva tumani uchun

@dp.callback_query_handler(text="Quva")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quvamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quva Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kuva/353259/current-weather/353259")
    await call.message.answer(xabar, reply_markup=Quvamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quva Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/quva/")
    await call.message.answer(xabar, reply_markup=Quvamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quvadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Quvadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Rishton tumani uchun

@dp.callback_query_handler(text="Rishton")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Rishtonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Rishton Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/rishton/353252/current-weather/353252")
    await call.message.answer(xabar, reply_markup=Rishtonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Rishton Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/rishton/")
    await call.message.answer(xabar, reply_markup=Rishtonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Rishtondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Rishtondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Sux tumani uchun

@dp.callback_query_handler(text="Sux")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Suxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sux Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sokh/353244/current-weather/353244")
    await call.message.answer(xabar, reply_markup=Suxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sux Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ravon/")
    await call.message.answer(xabar, reply_markup=Suxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Suxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Suxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Toshloq tumani uchun

@dp.callback_query_handler(text="Toshloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Toshloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshloq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/toshloq/353253/current-weather/353253")
    await call.message.answer(xabar, reply_markup=Toshloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshloq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/toshloq/")
    await call.message.answer(xabar, reply_markup=Toshloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Toshloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Uchkuprik tumani uchun

@dp.callback_query_handler(text="Uchkuprik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchkuprik Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchkuprik/353254/current-weather/353254")
    await call.message.answer(xabar, reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchkuprik Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchko-prik/")
    await call.message.answer(xabar, reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchkuprikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchkuprikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)






#    Jizzax viloyati



@dp.callback_query_handler(text="Jizzax")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


#    Jizzaxshahar   tumani uchun

@dp.callback_query_handler(text="Jizzaxshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jizzaxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jizzax Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Jizzaxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jizzax Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jizzakh/")
    await call.message.answer(xabar, reply_markup=Jizzaxmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jizzaxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jizzaxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Zomin tumani uchun

@dp.callback_query_handler(text="Zomin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zominmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zomin Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zaamin/354217/current-weather/354217")
    await call.message.answer(xabar, reply_markup=Zominmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zomin Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zomin/")
    await call.message.answer(xabar, reply_markup=Zominmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zomindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zomindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#     Arnasoy tumani uchun

@dp.callback_query_handler(text="Arnasoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Arnasoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Arnasoy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/arnasay/1618452/current-weather/1618452")
    await call.message.answer(xabar, reply_markup=Arnasoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Arnasoy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/g-oliblar/")
    await call.message.answer(xabar, reply_markup=Arnasoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Arnasoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Arnasoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Baxmal tumani uchun

@dp.callback_query_handler(text="Baxmal")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Baxmalmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baxmal Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/en/uz/bakhmal/721977/current-weather/721977")
    await call.message.answer(xabar, reply_markup=Baxmalmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baxmal Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/usmat-shaharchasi/")
    await call.message.answer(xabar, reply_markup=Baxmalmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baxmaldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Baxmaldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Dustlik tumani uchun

@dp.callback_query_handler(text="Dustlik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dustlikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dustlik Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dustlik/354202/current-weather/354202")
    await call.message.answer(xabar, reply_markup=Dustlikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dustlik Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/dustlik/")
    await call.message.answer(xabar, reply_markup=Dustlikmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dustlikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dustlikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Forish tumani uchun

@dp.callback_query_handler(text="Forish")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Forishmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Forish Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/farish/721469/current-weather/721469")
    await call.message.answer(xabar, reply_markup=Forishmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Forish Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/gulzor/")
    await call.message.answer(xabar, reply_markup=Forishmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Forishdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Forishdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Gallaorol tumani uchun

@dp.callback_query_handler(text="Gallaorol")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gallaorolmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gallaorol Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gallyaaral/354212/current-weather/354212")
    await call.message.answer(xabar, reply_markup=Gallaorolmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gallaorol Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qoytosh/")
    await call.message.answer(xabar, reply_markup=Gallaorolmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gallaoroldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gallaoroldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Mirzachul tumani uchun

@dp.callback_query_handler(text="Mirzachul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mirzachulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirzachul Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gagarin/354203/current-weather/354203")
    await call.message.answer(xabar, reply_markup=Mirzachulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirzachul Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/mirzadala/")
    await call.message.answer(xabar, reply_markup=Mirzachulmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirzachuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirzachuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Paxtakor tumani uchun

@dp.callback_query_handler(text="Paxtakor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtakormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtakor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pakhtakor/354205/current-weather/354205")
    await call.message.answer(xabar, reply_markup=Paxtakormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtakor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/paxtakor/")
    await call.message.answer(xabar, reply_markup=Paxtakormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtakordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtakordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yangiobod tumani uchun

@dp.callback_query_handler(text="Yangiobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Yangiobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiqishloq/")
    await call.message.answer(xabar, reply_markup=Yangiobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangioboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangioboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Zafarobod  tumani uchun

@dp.callback_query_handler(text="Zafarobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zafarobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zafarobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zafarabad/354209/current-weather/354209")
    await call.message.answer(xabar, reply_markup=Zafarobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zafarobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zafarobod/")
    await call.message.answer(xabar, reply_markup=Zafarobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zafaroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zafaroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Zarband tumani uchun

@dp.callback_query_handler(text="Zarband")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zarbandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarband Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Zarbandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarband Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zarbdor/")
    await call.message.answer(xabar, reply_markup=Zarbandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarbanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarbanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
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
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urganchmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urganch Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/urgench/356378/current-weather/356378")
    await call.message.answer(xabar, reply_markup=Urganchmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urganch Haftalik")
async def buy_courses(call: CallbackQuery):
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/")
    await call.message.answer(xabar, reply_markup=Urganchmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urganchdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urganchdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yangibozor tumani uchun

@dp.callback_query_handler(text="Yangibozor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangibozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangibozor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangibazar/356401/current-weather/356401")
    await call.message.answer(xabar, reply_markup=Yangibozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangibozor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangibozor_2/")
    await call.message.answer(xabar, reply_markup=Yangibozormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangibozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangibozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Bogot   tumani uchun

@dp.callback_query_handler(text="Bogot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bogotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bagat/356387/current-weather/356387")
    await call.message.answer(xabar, reply_markup=Bogotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/")
    await call.message.answer(xabar, reply_markup=Bogotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bogotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Gurlan tumani uchun

@dp.callback_query_handler(text="Gurlan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gurlanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gurlan Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gurlan/356381/current-weather/356381")
    await call.message.answer(xabar, reply_markup=Gurlanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gurlan Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/gurlan/")
    await call.message.answer(xabar, reply_markup=Gurlanmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gurlandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gurlandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Qushkupir tumani uchun

@dp.callback_query_handler(text="Qushkupir")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushkupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushkupir Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qushkupir/356384/current-weather/356384")
    await call.message.answer(xabar, reply_markup=Qushkupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushkupir Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qushkupir/")
    await call.message.answer(xabar, reply_markup=Qushkupirmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushkupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushkupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Shovot tumani uchun

@dp.callback_query_handler(text="Shovot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shovotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shovot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/showot/356385/current-weather/356385")
    await call.message.answer(xabar, reply_markup=Shovotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shovot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/showot/")
    await call.message.answer(xabar, reply_markup=Shovotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shovotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shovotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xazorasp tumani uchun

@dp.callback_query_handler(text="Xazorasp")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xazoraspmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xazorasp Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/hazorasp/356382/current-weather/356382")
    await call.message.answer(xabar, reply_markup=Xazoraspmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xazorasp Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/hazorasp/")
    await call.message.answer(xabar, reply_markup=Xazoraspmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xazoraspdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xazoraspdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xiva tumani uchun

@dp.callback_query_handler(text="Xiva")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xivamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xiva Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khiva/356380/current-weather/356380")
    await call.message.answer(xabar, reply_markup=Xivamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xiva Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/khiva/")
    await call.message.answer(xabar, reply_markup=Xivamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xivadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xivadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Xonqa tumani uchun

@dp.callback_query_handler(text="Xonqa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xonqamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonqa Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khonqa/356383/current-weather/356383")
    await call.message.answer(xabar, reply_markup=Xonqamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonqa Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgench/")
    await call.message.answer(xabar, reply_markup=Xonqamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonqadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xonqadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yangiariq tumani uchun

@dp.callback_query_handler(text="Yangiariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiariq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiaryk/356400/current-weather/356400")
    await call.message.answer(xabar, reply_markup=Yangiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiariq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiariq/")
    await call.message.answer(xabar, reply_markup=Yangiariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#    Namangan viloyati



@dp.callback_query_handler(text="Namangan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


#    Namanganshahri   shahar  uchun

@dp.callback_query_handler(text="Namanganshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Namanganmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Namangan Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/current-weather/355095")
    await call.message.answer(xabar, reply_markup=Namanganmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Namangan Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/namangan/")
    await call.message.answer(xabar, reply_markup=Namanganmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Namangandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Namangandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Chortoq tumani uchun

@dp.callback_query_handler(text="Chortoq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chortoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chortoq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/current-weather/355095")
    await call.message.answer(xabar, reply_markup=Chortoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chortoq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chortoq/")
    await call.message.answer(xabar, reply_markup=Chortoqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chortoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chortoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Chust   tumani uchun

@dp.callback_query_handler(text="Chust")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chustmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chust Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chust/355107/current-weather/355107")
    await call.message.answer(xabar, reply_markup=Chustmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chust Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chust-shahri/")
    await call.message.answer(xabar, reply_markup=Chustmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chustdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chustdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Kosonsoy tumani uchun

@dp.callback_query_handler(text="Kosonsoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kosonsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosonsoy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasansay/355108/current-weather/355108")
    await call.message.answer(xabar, reply_markup=Kosonsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosonsoy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kosonsoy/")
    await call.message.answer(xabar, reply_markup=Kosonsoymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosonsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosonsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Mingbuloq tumani uchun

@dp.callback_query_handler(text="Mingbuloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mingbuloq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhumashuy/355097/current-weather/355097")
    await call.message.answer(xabar, reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mingbuloq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jomasho-y/")
    await call.message.answer(xabar, reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mingbuloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mingbuloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Norin tumani uchun

@dp.callback_query_handler(text="Norin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Norinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Norin Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/naryn/355100/current-weather/355100")
    await call.message.answer(xabar, reply_markup=Norinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Norin Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jnorinkapa/")
    await call.message.answer(xabar, reply_markup=Norinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Norindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Norindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Pop tumani uchun

@dp.callback_query_handler(text="Pop")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Popmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pop Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pap/355102/current-weather/355102")
    await call.message.answer(xabar, reply_markup=Popmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pop Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/pop/")
    await call.message.answer(xabar, reply_markup=Popmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Popdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Popdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Turaqurgon tumani uchun

@dp.callback_query_handler(text="Turaqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turaqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/turakurgan/355103/current-weather/355103")
    await call.message.answer(xabar, reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turaqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/turagurghon/")
    await call.message.answer(xabar, reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Turaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Uchqurgon tumani uchun

@dp.callback_query_handler(text="Uchqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchkurgan/355110/current-weather/355110")
    await call.message.answer(xabar, reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchqurghon-shahri/")
    await call.message.answer(xabar, reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Uychi tumani uchun

@dp.callback_query_handler(text="Uychi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uychimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uychi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uychi/355111/current-weather/355111")
    await call.message.answer(xabar, reply_markup=Uychimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uychi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uychi/")
    await call.message.answer(xabar, reply_markup=Uychimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uychidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uychidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Yangiqurgon tumani uchun

@dp.callback_query_handler(text="Yangiqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangikurgan/355112/current-weather/355112")
    await call.message.answer(xabar, reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangiqorgon/")
    await call.message.answer(xabar, reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)









#    Navoiy viloyati



@dp.callback_query_handler(text="Navoiy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


#    Navoiyshahri   shahar  uchun

@dp.callback_query_handler(text="Navoiyshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Navoiymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navoiy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/current-weather/355115")
    await call.message.answer(xabar, reply_markup=Navoiymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navoiy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/navoiy/")
    await call.message.answer(xabar, reply_markup=Navoiymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navoiydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navoiydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Zarafshon  tumani uchun

@dp.callback_query_handler(text="Zarafshon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zarafshonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarafshon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zarafshan/355142/current-weather/355142")
    await call.message.answer(xabar, reply_markup=Zarafshonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarafshon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/zarafshan/")
    await call.message.answer(xabar, reply_markup=Zarafshonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarafshondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Zarafshondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Karmana   tumani uchun

@dp.callback_query_handler(text="Karmana")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Karmanamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Karmana Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/current-weather/355115")
    await call.message.answer(xabar, reply_markup=Karmanamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Karmana Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karmana-shahri/")
    await call.message.answer(xabar, reply_markup=Karmanamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Karmanadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Karmanadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Konimex tumani uchun

@dp.callback_query_handler(text="Konimex")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Konimexmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Konimex Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kanimekh/355133/current-weather/355133")
    await call.message.answer(xabar, reply_markup=Konimexmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Konimex Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/konimex/")
    await call.message.answer(xabar, reply_markup=Konimexmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Konimexdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Konimexdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Navbahor tumani uchun

@dp.callback_query_handler(text="Navbahor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Navbahormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navbahor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beshrabot/355118/current-weather/355118")
    await call.message.answer(xabar, reply_markup=Navbahormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navbahor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/beshrabot/")
    await call.message.answer(xabar, reply_markup=Navbahormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navbahordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Navbahordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Nurota tumani uchun

@dp.callback_query_handler(text="Nurota")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nurotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurota Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nurata/355117/current-weather/355117")
    await call.message.answer(xabar, reply_markup=Nurotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurota Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nurata/")
    await call.message.answer(xabar, reply_markup=Nurotamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qiziltepa tumani uchun

@dp.callback_query_handler(text="Qiziltepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qiziltepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziltepa Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kyzyltepa/355122/current-weather/355122")
    await call.message.answer(xabar, reply_markup=Qiziltepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziltepa Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qiziltepa/")
    await call.message.answer(xabar, reply_markup=Qiziltepamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziltepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qiziltepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Tomdi tumani uchun

@dp.callback_query_handler(text="Tomdi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Tomdimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tomdi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tamdybulak/355139/current-weather/355139")
    await call.message.answer(xabar, reply_markup=Tomdimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tomdi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/tomdibuloq/")
    await call.message.answer(xabar, reply_markup=Tomdimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tomdidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tomdidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Uchquduq tumani uchun

@dp.callback_query_handler(text="Uchquduq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchquduq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchquduq/355125/current-weather/355125")
    await call.message.answer(xabar, reply_markup=Uchquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchquduq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/uchquduq-shahri/")
    await call.message.answer(xabar, reply_markup=Uchquduqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Uchquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Xatirchi tumani uchun

@dp.callback_query_handler(text="Xatirchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xatirchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xatirchi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khatyrchi/720956/current-weather/720956")
    await call.message.answer(xabar, reply_markup=Xatirchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xatirchi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangirabot/")
    await call.message.answer(xabar, reply_markup=Xatirchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xatirchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xatirchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
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
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qarshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qarshi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qarshi/350541/current-weather/350541")
    await call.message.answer(xabar, reply_markup=Qarshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qarshi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/karshi/")
    await call.message.answer(xabar, reply_markup=Qarshimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qarshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qarshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Chiroqchi  tumani uchun

@dp.callback_query_handler(text="Chiroqchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chiroqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chiroqchi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirakchi/355641/current-weather/355641")
    await call.message.answer(xabar, reply_markup=Chiroqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chiroqchi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/chiroqchi/")
    await call.message.answer(xabar, reply_markup=Chiroqchimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chiroqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Chiroqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Dehqonobod   tumani uchun

@dp.callback_query_handler(text="Dehqonobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dehqonobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dekhkanabad/355653/current-weather/355653")
    await call.message.answer(xabar, reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dehqonobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qiziltepa_2/")
    await call.message.answer(xabar, reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dehqonoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Dehqonoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Guzor tumani uchun

@dp.callback_query_handler(text="Guzor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Guzormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guzor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guzar/355639/current-weather/355639")
    await call.message.answer(xabar, reply_markup=Guzormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guzor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/guzor/")
    await call.message.answer(xabar, reply_markup=Guzormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guzordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guzordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Kasbi tumani uchun

@dp.callback_query_handler(text="Kasbi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kasbimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kasbi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasbi/355660/current-weather/355660")
    await call.message.answer(xabar, reply_markup=Kasbimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kasbi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muglon-shahar/")
    await call.message.answer(xabar, reply_markup=Kasbimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kasbidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kasbidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Kitob tumani uchun

@dp.callback_query_handler(text="Kitob")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kitobmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kitob Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kitab/355643/current-weather/355643")
    await call.message.answer(xabar, reply_markup=Kitobmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kitob Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kitob/")
    await call.message.answer(xabar, reply_markup=Kitobmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kitobdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kitobdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#    Koson  tumani uchun

@dp.callback_query_handler(text="Koson")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kosonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Koson Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasan/355659/current-weather/355659")
    await call.message.answer(xabar, reply_markup=Kosonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Koson Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/koson-shahri/")
    await call.message.answer(xabar, reply_markup=Kosonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kosondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Mirishkor tumani uchun

@dp.callback_query_handler(text="Mirishkor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mirishkormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirishkor Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/en/uz/yangi-mirishkor/720478/current-weather/720478")
    await call.message.answer(xabar, reply_markup=Mirishkormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirishkor Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yangi-mirishkor/")
    await call.message.answer(xabar, reply_markup=Mirishkormenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirishkordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Mirishkordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Muborak tumani uchun

@dp.callback_query_handler(text="Muborak")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muborakmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muborak Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/mubarek/355663/current-weather/355663")
    await call.message.answer(xabar, reply_markup=Muborakmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muborak Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/muborak-shahri/")
    await call.message.answer(xabar, reply_markup=Muborakmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muborakdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Muborakdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Nishon tumani uchun

@dp.callback_query_handler(text="Nishon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nishonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nishon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nishon/720357/current-weather/720357")
    await call.message.answer(xabar, reply_markup=Nishonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nishon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/nishon-tumani/")
    await call.message.answer(xabar, reply_markup=Nishonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nishondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nishondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Qamashi tumani uchun

@dp.callback_query_handler(text="Qamashi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qamashimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qamashi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kamashi/355656/current-weather/355656")
    await call.message.answer(xabar, reply_markup=Qamashimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qamashi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qamashi-shahri/")
    await call.message.answer(xabar, reply_markup=Qamashimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qamashidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qamashidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Shahrisabz tumani uchun

@dp.callback_query_handler(text="Shahrisabz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrisabz Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shakhrisabz/355647/current-weather/355647")
    await call.message.answer(xabar, reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrisabz Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/shahrisabz/")
    await call.message.answer(xabar, reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrisabzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Shahrisabzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yakkabog tumani uchun

@dp.callback_query_handler(text="Yakkabog")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yakkabogmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yakkabog Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yakkabag/355665/current-weather/355665")
    await call.message.answer(xabar, reply_markup=Yakkabogmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yakkabog Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/yakkabog-shahri/")
    await call.message.answer(xabar, reply_markup=Yakkabogmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yakkabogdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yakkabogdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)











#    Samarqand viloyati



@dp.callback_query_handler(text="Samarqand")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


#    Samarqand   shahar  uchun

@dp.callback_query_handler(text="Samarqandshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Samarqandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Samarqand Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Samarqandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Samarqand Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/samarkand/")
    await call.message.answer(xabar, reply_markup=Samarqandmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Samarqanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Samarqanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Urgut  tumani uchun

@dp.callback_query_handler(text="Urgut")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urgutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urgut Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/urgut/355795/current-weather/355795")
    await call.message.answer(xabar, reply_markup=Urgutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urgut Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/urgut/")
    await call.message.answer(xabar, reply_markup=Urgutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urgutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Urgutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Bulungur   tumani uchun

@dp.callback_query_handler(text="Bulungur")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bulungurmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bulungur Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bulungur/355781/current-weather/355781")
    await call.message.answer(xabar, reply_markup=Bulungurmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bulungur Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/bulungur/")
    await call.message.answer(xabar, reply_markup=Bulungurmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bulungurdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Bulungurdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Ishtixon tumani uchun

@dp.callback_query_handler(text="Ishtixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ishtixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ishtixon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ishtykhan/355788/current-weather/355788")
    await call.message.answer(xabar, reply_markup=Ishtixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ishtixon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ishtixon/")
    await call.message.answer(xabar, reply_markup=Ishtixonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ishtixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Ishtixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Jomboy tumani uchun

@dp.callback_query_handler(text="Jomboy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jomboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jomboy Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhambay/355785/current-weather/355785")
    await call.message.answer(xabar, reply_markup=Jomboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jomboy Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jomboy/")
    await call.message.answer(xabar, reply_markup=Jomboymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jomboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jomboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Kattaqurgon tumani uchun

@dp.callback_query_handler(text="Kattaqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kattaqurgon Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kattaqurghon/355778/current-weather/355778")
    await call.message.answer(xabar, reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kattaqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/kattaqorgon/")
    await call.message.answer(xabar, reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kattaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kattaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#    Narpay  tumani uchun

@dp.callback_query_handler(text="Narpay")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Narpaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Narpay Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/aktash/355797/current-weather/355797")
    await call.message.answer(xabar, reply_markup=Narpaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Narpay Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqtosh/")
    await call.message.answer(xabar, reply_markup=Narpaymenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Narpaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Narpaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Nurobod tumani uchun

@dp.callback_query_handler(text="Nurobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nurobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nurobod/719969/current-weather/719969")
    await call.message.answer(xabar, reply_markup=Nurobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nurobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/juma/")
    await call.message.answer(xabar, reply_markup=Nurobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nuroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Nuroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Oqdaryo tumani uchun

@dp.callback_query_handler(text="Oqdaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqdaryo Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/laish/355792/current-weather/355792")
    await call.message.answer(xabar, reply_markup=Oqdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqdaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/loyish/")
    await call.message.answer(xabar, reply_markup=Oqdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Pastdargom tumani uchun

@dp.callback_query_handler(text="Pastdargom")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Pastdargommenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pastdargom Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhuma/355786/current-weather/355786")
    await call.message.answer(xabar, reply_markup=Pastdargommenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pastdargom Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/juma/")
    await call.message.answer(xabar, reply_markup=Pastdargommenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pastdargomdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Pastdargomdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Paxtachi tumani uchun

@dp.callback_query_handler(text="Paxtachi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtachimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtachi Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ziadin/355143/current-weather/355143")
    await call.message.answer(xabar, reply_markup=Paxtachimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtachi Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/ziyodin/")
    await call.message.answer(xabar, reply_markup=Paxtachimenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtachidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Paxtachidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Poyariq tumani uchun

@dp.callback_query_handler(text="Poyariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Poyariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Poyariq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/payariq/720402/current-weather/720402")
    await call.message.answer(xabar, reply_markup=Poyariqmenu)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text="Poyariq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/payariq-shahri/")
    await call.message.answer(xabar, reply_markup=Poyariqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Poyariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Poyariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Qushrabot tumani uchun

@dp.callback_query_handler(text="Qushrabot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushrabot Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/koshrabad/355789/current-weather/355789")
    await call.message.answer(xabar, reply_markup=Qushrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushrabot Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/qushrabot/")
    await call.message.answer(xabar, reply_markup=Qushrabotmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Qushrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)






#   Tayloq tumani uchun

@dp.callback_query_handler(text="Tayloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Tayloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tayloq Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/taylak/355794/current-weather/355794")
    await call.message.answer(xabar, reply_markup=Tayloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tayloq Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/toyloq/")
    await call.message.answer(xabar, reply_markup=Tayloqmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tayloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Tayloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)





#    Sirdaryo viloyati



@dp.callback_query_handler(text="Sirdaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


#    Sirdaryo   shahar  uchun

@dp.callback_query_handler(text="Sirdaryoshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sirdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sirdaryo Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/current-weather/355934")
    await call.message.answer(xabar, reply_markup=Sirdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sirdaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sirdaryo_2/")
    await call.message.answer(xabar, reply_markup=Sirdaryomenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sirdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sirdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#  Boyovut  tumani uchun

@dp.callback_query_handler(text="Boyovut")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Boyovutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boyovut Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/current-weather/355927")
    await call.message.answer(xabar, reply_markup=Boyovutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boyovut Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/boyovut/")
    await call.message.answer(xabar, reply_markup=Boyovutmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boyovutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Boyovutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Guliston   tumani uchun

@dp.callback_query_handler(text="Guliston")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gulistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guliston Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/current-weather/355927")
    await call.message.answer(xabar, reply_markup=Gulistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Guliston Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/guliston/")
    await call.message.answer(xabar, reply_markup=Gulistonmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gulistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Gulistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Oqoltin tumani uchun

@dp.callback_query_handler(text="Oqoltin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqoltinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqoltin Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/current-weather/355932")
    await call.message.answer(xabar, reply_markup=Oqoltinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqoltin Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/oqoltin_3/")
    await call.message.answer(xabar, reply_markup=Oqoltinmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqoltindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Oqoltindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)




#   Sardoba  tumani uchun

@dp.callback_query_handler(text="Sardoba")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sardobamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sardoba Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/current-weather/355932")
    await call.message.answer(xabar, reply_markup=Sardobamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sardoba Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sardoba/")
    await call.message.answer(xabar, reply_markup=Sardobamenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sardobadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sardobadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)



#   Sayxunobod tumani uchun

@dp.callback_query_handler(text="Sayxunobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sayxunobod Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/current-weather/355934")
    await call.message.answer(xabar, reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sayxunobod Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/sayxun/")
    await call.message.answer(xabar, reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sayxunoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Sayxunoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#    Xavos  tumani uchun

@dp.callback_query_handler(text="Xavos")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xavosmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xavos Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khavast/355928/current-weather/355928")
    await call.message.answer(xabar, reply_markup=Xavosmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xavos Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/xovos/")
    await call.message.answer(xabar, reply_markup=Xavosmenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xavosdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xavosdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)


#   Yangiyer tumani uchun

@dp.callback_query_handler(text="Yangiyer")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiyermenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyer Namoz Vaqtlari")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyer/355936/current-weather/355936")
    await call.message.answer(xabar, reply_markup=Yangiyermenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyer Haftalik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    xabar = haftalik_obhavo("https://uz.meteotrend.com/week-forecast/uz/jangier/")
    await call.message.answer(xabar, reply_markup=Yangiyermenu)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyerdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Yangiyerdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)









@dp.callback_query_handler(text="🔙Ortga")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=10)





