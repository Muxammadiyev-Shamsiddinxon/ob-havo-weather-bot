
#   1- funksiya bu  parsing qilingan kodlar returngacha yani bugun def funksiyasigacha

import  re
sonlar = "[0-9]+.?[0-9]*"
from ast import parse
import requests
from bs4 import BeautifulSoup


def bugun_obhavo(url):
    # bu saytdan olib beradi malumotlar
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }


    site = requests.get(url=url, headers=headers)
    htmldom = BeautifulSoup(site.text, "lxml")

    hudud = htmldom.find("h1", class_="header-loc").text.strip()  # hudud

    kun = htmldom.find("div", class_="content-module subnav-pagination").text.strip()
    bugun = f"Bugun {kun}."  # javob

    hozir_temp = htmldom.find("div", class_="display-temp").text.strip()
    hozir_havo = htmldom.find("div", class_="phrase").text.strip()
    temp = f"{hozir_havo} havo {hozir_temp}  \n"  # javob

    umumiy_temp = htmldom.findAll("div", class_="row first")[0].text
    umumiy_temp = re.findall(sonlar, umumiy_temp)
    a = umumiy_temp[0]
    b = umumiy_temp[1]
    max_temp = max(a, b)
    min_temp = min(a, b)

    max_min = f"🌡Yuqori temperatura --> {max_temp}C\n🌡Past temperatura -----> {min_temp}C"  # javob

    umumiy = htmldom.find("div", class_="left").text.strip()
    umumiy1 = re.findall(sonlar, umumiy)
    if len(umumiy1) == 5:
        shamol = f"🌬Shamol -------------------> {re.findall(sonlar, umumiy)[1]}km/soat"
        namlik = f"💧Namlik -------------------> {re.findall(sonlar, umumiy)[3]} "
    else:
        shamol = f"🌬Shamol -----------------> {re.findall(sonlar, umumiy)[0]}km/soat"
        namlik = f"💧Namlik ------------------> {re.findall(sonlar, umumiy)[2]} "
    shamol_namlik = f"<b>{shamol} \n{namlik}</b>"  # javob

    umumiy2 = htmldom.find("div", class_="right").text.strip()
    bosim = f"⛈Bosim -------------------> ↓ {re.findall(sonlar, umumiy2)[0]}mb"
    tuman = f"☁️Tumanli -----------------> {re.findall(sonlar, umumiy2)[1]}"
    bulut = f"\nEng pastgi bulut {re.findall(sonlar, umumiy2)[3]}metr masofada"
    b_t_b = f"<b>{bosim}\n{tuman}\n{bulut}</b>"  # javob

    quyosh1 = htmldom.findAll("span", class_="text-value")[0].text.strip()
    quyosh2 = htmldom.findAll("span", class_="text-value")[1].text.strip()
    quyosh = f"🌤 Quyosh chiqishi ___{quyosh1}___\n🌥 Quyosh botishi ___{quyosh2}___"  # javob

    javob = f"<b>{hudud}\n\n{bugun}\n{temp}\n{max_min}\n{shamol_namlik}\n{b_t_b}\n\n\n{quyosh}</b>"
    return javob








#   haftalik ob havo parsing

def haftalik_obhavo(url):
    # bu saytdan olib beradi malumotlarni
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }



    site = requests.get(url=url, headers=headers)
    htmldom = BeautifulSoup(site.text, "lxml")

    hudud = htmldom.find("h1", class_="header-loc").text.strip()
    hudud = f"<b>Haftalik ob-havo.</b>\n<b>{hudud}</b>\n\n"

    yogingarchilik = []
    yogingarchilik_javob = htmldom.find("div").findAll("div", class_="precip")
    for k in yogingarchilik_javob:
        yogingarchilik.append(k.text.strip())

    maxtemp = []
    maxtemp_javob = htmldom.find("div").findAll("span", class_="high")
    for k in maxtemp_javob:
        maxtemp.append(k.text.strip())

    mintemp = []
    mintemp_javob = htmldom.find("div").findAll("span", class_="low")
    for k in mintemp_javob:
        mintemp.append(k.text.strip().replace("/", ""))

    havo = []
    havo_javob = htmldom.find("div").findAll("div", class_="phrase")
    for k in havo_javob:
        havo.append(k.text.strip())

    cheslo = []
    cheslo_javob = htmldom.find("div").findAll("span", class_="module-header sub date")
    for k in cheslo_javob:
        cheslo.append(k.text.strip())

    kun = []
    kun_javob = htmldom.find("div").findAll("span", class_="module-header dow date")
    for k in kun_javob:
        k = k.text.strip()
        if k == "Jum":
            k = "Juma"
        elif k == "Shan":
            k = "Shanba"
        elif k == "Dush":
            k = f"{k}anba"
        elif k == "Sesh":
            k = f"{k}anba"
        else:
            k = f"{k}shanba"
        kun.append(k)

    kun0 = f"<b>Sana: {cheslo[0]}</b>\n{kun[0]} {havo[0]}\n🌡Yuqori temperatura ---->{maxtemp[0]}C\n🌡Past temperatura ------->{mintemp[0]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[0]}\n\n"
    kun1 = f"<b>Sana: {cheslo[1]}</b>\n{kun[1]} {havo[1]}\n🌡Yuqori temperatura ---->{maxtemp[1]}C\n🌡Past temperatura ------->{mintemp[1]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[1]}\n\n"
    kun2 = f"<b>Sana: {cheslo[2]}</b>\n{kun[2]} {havo[2]}\n🌡Yuqori temperatura ---->{maxtemp[2]}C\n🌡Past temperatura ------->{mintemp[2]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[2]}\n\n"
    kun3 = f"<b>Sana: {cheslo[3]}</b>\n{kun[3]} {havo[3]}\n🌡Yuqori temperatura ---->{maxtemp[3]}C\n🌡Past temperatura ------->{mintemp[3]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[3]}\n\n"
    kun4 = f"<b>Sana: {cheslo[4]}</b>\n{kun[4]} {havo[4]}\n🌡Yuqori temperatura ---->{maxtemp[4]}C\n🌡Past temperatura ------->{mintemp[4]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[4]}\n\n"
    kun5 = f"<b>Sana: {cheslo[5]}</b>\n{kun[5]} {havo[5]}\n🌡Yuqori temperatura ---->{maxtemp[5]}C\n🌡Past temperatura ------->{mintemp[5]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[5]}\n\n"
    kun6 = f"<b>Sana: {cheslo[6]}</b>\n{kun[6]} {havo[6]}\n🌡Yuqori temperatura ---->{maxtemp[6]}C\n🌡Past temperatura ------->{mintemp[6]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[6]}\n\n"
    kun7 = f"<b>Sana: {cheslo[7]}</b>\n{kun[7]} {havo[7]}\n🌡Yuqori temperatura ---->{maxtemp[7]}C\n🌡Past temperatura ------->{mintemp[7]}C\n⛈Yog'ingarchilik    --------->{yogingarchilik[7]}\n\n"

    javob = f"<b>{hudud}{kun0}{kun1}{kun2}{kun3}{kun4}{kun5}{kun6}{kun7}</b>"
    return javob







from aiogram import types
import asyncio
from loader import dp

from aiogram import Bot, Dispatcher, executor, types
import logging



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
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)

#    Nukus   tumani uchun

@dp.callback_query_handler(text="Nukus")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nukusmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nukus Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Nukusmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nukus Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/daily-weather-forecast/355666")
    await call.message.answer(xabar, reply_markup=Nukusmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nukusdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nukusdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Amudaryo  tumani uchun

@dp.callback_query_handler(text="Amudaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Amudaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Amudaryo Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/mangit/355693/current-weather/355693")
    await call.message.answer(xabar, reply_markup=Amudaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Amudaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/mangit/355693/daily-weather-forecast/355693")
    await call.message.answer(xabar, reply_markup=Amudaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Amudaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Amudaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Beruniy tumani uchun

@dp.callback_query_handler(text="Beruniy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Beruniymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beruniy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beruni/355684/current-weather/355684")
    await call.message.answer(xabar, reply_markup=Beruniymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beruniy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/beruni/355684/daily-weather-forecast/355684")
    await call.message.answer(xabar, reply_markup=Beruniymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beruniydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beruniydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Chimboy tumani uchun

@dp.callback_query_handler(text="Chimboy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chimboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chimboy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chimbay/355669/current-weather/355669")
    await call.message.answer(xabar, reply_markup=Chimboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chimboy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chimbay/355669/daily-weather-forecast/355669")
    await call.message.answer(xabar, reply_markup=Chimboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chimboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chimboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Elliktepa tumani uchun

@dp.callback_query_handler(text="Elliktepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Elliktepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Elliktepa Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ellikkala/721481/current-weather/721481")
    await call.message.answer(xabar, reply_markup=Elliktepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Elliktepa Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/ellikkala/721481/daily-weather-forecast/721481")
    await call.message.answer(xabar, reply_markup=Elliktepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Elliktepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Elliktepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Kegeyli tumani uchun

@dp.callback_query_handler(text="Kegeyli")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kegeylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kegeyli Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kegeyli/355689/current-weather/355689")
    await call.message.answer(xabar, reply_markup=Kegeylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kegeyli Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kegeyli/355689/daily-weather-forecast/355689")
    await call.message.answer(xabar, reply_markup=Kegeylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kegeylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kegeylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Muynoq tumani uchun

@dp.callback_query_handler(text="Muynoq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muynoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muynoq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/muynoq/355668/current-weather/355668")
    await call.message.answer(xabar, reply_markup=Muynoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muynoq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/muynoq/355668/daily-weather-forecast/355668")
    await call.message.answer(xabar, reply_markup=Muynoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muynoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muynoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xujayli tumani uchun

@dp.callback_query_handler(text="Xujayli")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xujaylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujayli Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khujayli/355667/current-weather/355667")
    await call.message.answer(xabar, reply_markup=Xujaylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujayli Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khujayli/355667/daily-weather-forecast/355667")
    await call.message.answer(xabar, reply_markup=Xujaylimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujaylidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujaylidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Qonlikul tumani uchun

@dp.callback_query_handler(text="Qonlikul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qonlikulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qonlikul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Qonlikulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qonlikul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/daily-weather-forecast/355666")
    await call.message.answer(xabar, reply_markup=Qonlikulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qonlikuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qonlikuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qorauzaq tumani uchun

@dp.callback_query_handler(text="Qorauzaq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorauzaq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karauzyak/355688/current-weather/355688")
    await call.message.answer(xabar, reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorauzaq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/daily-weather-forecast/355666")
    await call.message.answer(xabar, reply_markup=Qorauzaqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorauzaqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorauzaqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qungirot tumani uchun

@dp.callback_query_handler(text="Qungirot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qungirotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qungirot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kungrad/355670/current-weather/355670")
    await call.message.answer(xabar, reply_markup=Qungirotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qungirot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kungrad/355670/daily-weather-forecast/355670")
    await call.message.answer(xabar, reply_markup=Qungirotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qungirotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qungirotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Shumanay tumani uchun

@dp.callback_query_handler(text="Shumanay")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shumanaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shumanay Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shumanay/355682/current-weather/355682")
    await call.message.answer(xabar, reply_markup=Shumanaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shumanay Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/shumanay/355682/daily-weather-forecast/355682")
    await call.message.answer(xabar, reply_markup=Shumanaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shumanaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shumanaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Taxiatosh tumani uchun

@dp.callback_query_handler(text="Taxiatosh")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxiatosh Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/takhiatash/355671/current-weather/355671")
    await call.message.answer(xabar, reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxiatosh Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/takhiatash/355671/daily-weather-forecast/355671")
    await call.message.answer(xabar, reply_markup=Taxiatoshmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxiatoshdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxiatoshdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Taxtakupir tumani uchun

@dp.callback_query_handler(text="Taxtakupir")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxtakupir Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tahtakupyr/355672/current-weather/355672")
    await call.message.answer(xabar, reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxtakupir Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/tahtakupyr/355672/daily-weather-forecast/355672")
    await call.message.answer(xabar, reply_markup=Taxtakupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxtakupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Taxtakupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Turtkul tumani uchun

@dp.callback_query_handler(text="Turtkul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Turtkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turtkul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/turtkul/355695/current-weather/355695")
    await call.message.answer(xabar, reply_markup=Turtkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turtkul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/turtkul/355695/daily-weather-forecast/355695")
    await call.message.answer(xabar, reply_markup=Turtkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turtkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qoraqalpoq_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turtkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)







#    Toshkent viloyati



@dp.callback_query_handler(text="Toshkent")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)



#    Toshkent   tumani uchun

@dp.callback_query_handler(text="Toshkentshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Toshkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshkent Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tashkent/351199/current-weather/351199")
    await call.message.answer(xabar, reply_markup=Toshkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshkent Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/tashkent/351199/daily-weather-forecast/351199")
    await call.message.answer(xabar, reply_markup=Toshkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Bekobod  tumani uchun

@dp.callback_query_handler(text="Bekobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bekobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bekobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bekabad/356235/current-weather/356235")
    await call.message.answer(xabar, reply_markup=Bekobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bekobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bekabad/356235/daily-weather-forecast/356235")
    await call.message.answer(xabar, reply_markup=Bekobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bekoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bekoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Buka tumani uchun

@dp.callback_query_handler(text="Buka")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bukamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buka Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/buka/356221/current-weather/356221")
    await call.message.answer(xabar, reply_markup=Bukamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buka Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/buka/356221/daily-weather-forecast/356221")
    await call.message.answer(xabar, reply_markup=Bukamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bukadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bukadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Bustonliq tumani uchun

@dp.callback_query_handler(text="Bustonliq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bustonliqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bustonliq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gazalkent/356239/current-weather/356239")
    await call.message.answer(xabar, reply_markup=Bustonliqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bustonliq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/gazalkent/356239/daily-weather-forecast/356239")
    await call.message.answer(xabar, reply_markup=Bustonliqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bustonliqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bustonliqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Zangiota tumani uchun

@dp.callback_query_handler(text="Zangiota")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zangiotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zangiota Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/eshongyzar/356224/current-weather/356224")
    await call.message.answer(xabar, reply_markup=Zangiotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zangiota Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/eshongyzar/356224/daily-weather-forecast/356224")
    await call.message.answer(xabar, reply_markup=Zangiotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zangiotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zangiotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Oqqurgon tumani uchun

@dp.callback_query_handler(text="Oqqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/akkurgan/356220/current-weather/356220")
    await call.message.answer(xabar, reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/akkurgan/356220/daily-weather-forecast/356220")
    await call.message.answer(xabar, reply_markup=Oqqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Ohangaron tumani uchun

@dp.callback_query_handler(text="Ohangaron")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ohangaronmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ohangaron Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kurama/356247/current-weather/356247")
    await call.message.answer(xabar, reply_markup=Ohangaronmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ohangaron Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kurama/356247/daily-weather-forecast/356247")
    await call.message.answer(xabar, reply_markup=Ohangaronmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ohangarondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ohangarondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Parkent tumani uchun

@dp.callback_query_handler(text="Parkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Parkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Parkent Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/current-weather/356240")
    await call.message.answer(xabar, reply_markup=Parkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Parkent Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/daily-weather-forecast/356240")
    await call.message.answer(xabar, reply_markup=Parkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Parkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Parkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Piskent tumani uchun

@dp.callback_query_handler(text="Piskent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Piskentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Piskent Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/current-weather/356240")
    await call.message.answer(xabar, reply_markup=Piskentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Piskent Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/parkent/356240/daily-weather-forecast/356240")
    await call.message.answer(xabar, reply_markup=Piskentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Piskentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Piskentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Chinoz tumani uchun

@dp.callback_query_handler(text="Chinoz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chinozmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chinoz Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chinoz/356222/current-weather/356222")
    await call.message.answer(xabar, reply_markup=Chinozmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chinoz Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chinoz/356222/daily-weather-forecast/356222")
    await call.message.answer(xabar, reply_markup=Chinozmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chinozdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chinozdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yuqorichirchiq tumani uchun

@dp.callback_query_handler(text="Yuqorichirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yuqorichirchiq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirchik/356238/current-weather/356238")
    await call.message.answer(xabar, reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yuqorichirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chirchik/356238/daily-weather-forecast/356238")
    await call.message.answer(xabar, reply_markup=Yuqorichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yuqorichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yuqorichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yangiyul tumani uchun

@dp.callback_query_handler(text="Yangiyul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiyulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356245/current-weather/356245")
    await call.message.answer(xabar, reply_markup=Yangiyulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356245/daily-weather-forecast/356245")
    await call.message.answer(xabar, reply_markup=Yangiyulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Urtachirchiq tumani uchun

@dp.callback_query_handler(text="Urtachirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urtachirchiq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirchiq/356223/current-weather/356223")
    await call.message.answer(xabar, reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urtachirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chirchiq/356223/daily-weather-forecast/356223")
    await call.message.answer(xabar, reply_markup=Urtachirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urtachirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urtachirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qibray tumani uchun

@dp.callback_query_handler(text="Qibray")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qibraymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qibray Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qibray/356227/current-weather/356227")
    await call.message.answer(xabar, reply_markup=Qibraymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qibray Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/qibray/356227/daily-weather-forecast/356227")
    await call.message.answer(xabar, reply_markup=Qibraymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qibraydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qibraydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Quyichirchiq tumani uchun

@dp.callback_query_handler(text="Quyichirchiq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quyichirchiq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirchiq/356223/current-weather/356223")
    await call.message.answer(xabar, reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quyichirchiq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chirchiq/356223/daily-weather-forecast/356223")
    await call.message.answer(xabar, reply_markup=Quyichirchiqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quyichirchiqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=toshkent_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quyichirchiqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)









#    Surxondaryo viloyati



@dp.callback_query_handler(text="Surxondaryo")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


#    Termiz   tumani uchun

@dp.callback_query_handler(text="Termiz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Termizmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Termiz Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/termez/356042/current-weather/356042")
    await call.message.answer(xabar, reply_markup=Termizmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Termiz Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/termez/356042/daily-weather-forecast/356042")
    await call.message.answer(xabar, reply_markup=Termizmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Termizdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Termizdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Uzun  tumani uchun

@dp.callback_query_handler(text="Uzun")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uzunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzun Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uzun/356054/current-weather/356054")
    await call.message.answer(xabar, reply_markup=Uzunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzun Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/uzun/356054/daily-weather-forecast/356054")
    await call.message.answer(xabar, reply_markup=Uzunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Angor tumani uchun

@dp.callback_query_handler(text="Angor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Angormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Angor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/angor/356043/current-weather/356043")
    await call.message.answer(xabar, reply_markup=Angormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Angor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/angor/356043/daily-weather-forecast/356043")
    await call.message.answer(xabar, reply_markup=Angormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Angordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Angordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Bandixon tumani uchun

@dp.callback_query_handler(text="Bandixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bandixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bandixon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bandy-khan/356044/current-weather/356044")
    await call.message.answer(xabar, reply_markup=Bandixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bandixon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bandy-khan/356044/daily-weather-forecast/356044")
    await call.message.answer(xabar, reply_markup=Bandixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bandixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bandixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Boysun tumani uchun

@dp.callback_query_handler(text="Boysun")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Boysunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boysun Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/baysun/356058/current-weather/356058")
    await call.message.answer(xabar, reply_markup=Boysunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boysun Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/baysun/356058/daily-weather-forecast/356058")
    await call.message.answer(xabar, reply_markup=Boysunmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boysundan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boysundan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Denov tumani uchun

@dp.callback_query_handler(text="Denov")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Denovmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Denov Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/denau/356059/current-weather/356059")
    await call.message.answer(xabar, reply_markup=Denovmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Denov Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/denau/356059/daily-weather-forecast/356059")
    await call.message.answer(xabar, reply_markup=Denovmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Denovdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Denovdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Jarqurgon tumani uchun

@dp.callback_query_handler(text="Jarqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jarqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jarkurghon/356047/weather-forecast/356047")
    await call.message.answer(xabar, reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jarqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/jarkurghon/356047/daily-weather-forecast/356047")
    await call.message.answer(xabar, reply_markup=Jarqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jarqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jarqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Muzrabot tumani uchun

@dp.callback_query_handler(text="Muzrabot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muzrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muzrabot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zang/356056/current-weather/356056")
    await call.message.answer(xabar, reply_markup=Muzrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muzrabot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/zang/356056/daily-weather-forecast/356056")
    await call.message.answer(xabar, reply_markup=Muzrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muzrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muzrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Oltinsoy tumani uchun

@dp.callback_query_handler(text="Oltinsoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltinsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinsoy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karluk/356048/current-weather/356048")
    await call.message.answer(xabar, reply_markup=Oltinsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinsoy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/karluk/356048/daily-weather-forecast/356048")
    await call.message.answer(xabar, reply_markup=Oltinsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qiziriq tumani uchun

@dp.callback_query_handler(text="Qiziriq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qiziriqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziriq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356055/current-weather/356055")
    await call.message.answer(xabar, reply_markup=Qiziriqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziriq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangiyul/356055/daily-weather-forecast/356055")
    await call.message.answer(xabar, reply_markup=Qiziriqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziriqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziriqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Qumqurgon  tumani uchun

@dp.callback_query_handler(text="Qumqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qumqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kumkurgan/356049/current-weather/356049")
    await call.message.answer(xabar, reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qumqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kumkurgan/356049/daily-weather-forecast/356049")
    await call.message.answer(xabar, reply_markup=Qumqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qumqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qumqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Sariosiyo tumani uchun

@dp.callback_query_handler(text="Sariosiyo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sariosiyomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sariosiyo Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sariasiya/356052/current-weather/356052")
    await call.message.answer(xabar, reply_markup=Sariosiyomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sariosiyo Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sariasiya/356052/daily-weather-forecast/356052")
    await call.message.answer(xabar, reply_markup=Sariosiyomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sariosiyodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sariosiyodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Sherobod tumani uchun

@dp.callback_query_handler(text="Sherobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sherobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sherobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("accuweather.com/uz/uz/sherabad/356053/current-weather/356053")
    await call.message.answer(xabar, reply_markup=Sherobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sherobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("accuweather.com/uz/uz/sherabad/356053/daily-weather-forecast/356053")
    await call.message.answer(xabar, reply_markup=Sherobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sheroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sheroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Shurchi tumani uchun

@dp.callback_query_handler(text="Shurchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shurchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shurchi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shurchi/356063/current-weather/356063")
    await call.message.answer(xabar, reply_markup=Shurchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shurchi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/shurchi/356063/daily-weather-forecast/356063")
    await call.message.answer(xabar, reply_markup=Shurchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shurchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=surxon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shurchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#    Andijon viloyati



@dp.callback_query_handler(text="Andijon")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


#    Andijonshahar   tumani uchun

@dp.callback_query_handler(text="Andijonshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Andijonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Andijon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/andijan/351828/current-weather/351828")
    await call.message.answer(xabar, reply_markup=Andijonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Andijon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/andijan/351828/daily-weather-forecast/351828")
    await call.message.answer(xabar, reply_markup=Andijonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Andijondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Andijondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Baliqchi  tumani uchun

@dp.callback_query_handler(text="Baliqchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Baliqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baliqchi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/balykchi/351833/current-weather/351833")
    await call.message.answer(xabar, reply_markup=Baliqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baliqchi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/balykchi/351833/daily-weather-forecast/351833")
    await call.message.answer(xabar, reply_markup=Baliqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baliqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baliqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Buz tumani uchun

@dp.callback_query_handler(text="Buz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buz Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/boz/351834/current-weather/351834")
    await call.message.answer(xabar, reply_markup=Buzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buz Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/boz/351834/daily-weather-forecast/351834")
    await call.message.answer(xabar, reply_markup=Buzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Buloqboshi tumani uchun

@dp.callback_query_handler(text="Buloqboshi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buloqboshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buloqboshi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bulakbashi/351835/current-weather/351835")
    await call.message.answer(xabar, reply_markup=Buloqboshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buloqboshi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bulakbashi/351835/daily-weather-forecast/351835")
    await call.message.answer(xabar, reply_markup=Buloqboshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buloqboshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buloqboshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Izboskan tumani uchun

@dp.callback_query_handler(text="Izboskan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Izboskanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Izboskan Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/izbaskan/721284/current-weather/721284")
    await call.message.answer(xabar, reply_markup=Izboskanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Izboskan Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/izbaskan/721284/daily-weather-forecast/721284")
    await call.message.answer(xabar, reply_markup=Izboskanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Izboskandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Izboskandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Jalolquduq tumani uchun

@dp.callback_query_handler(text="Jalolquduq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jalolquduq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ahunbabayev/351831/current-weather/351831")
    await call.message.answer(xabar, reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jalolquduq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/ahunbabayev/351831/daily-weather-forecast/351831")
    await call.message.answer(xabar, reply_markup=Jalolquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jalolquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jalolquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Marhamat tumani uchun

@dp.callback_query_handler(text="Marhamat")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Marhamatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Marhamat Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/marhamat/351840/current-weather/351840")
    await call.message.answer(xabar, reply_markup=Marhamatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Marhamat Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/marhamat/351840/daily-weather-forecast/351840")
    await call.message.answer(xabar, reply_markup=Marhamatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Marhamatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Marhamatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Oltinkul tumani uchun

@dp.callback_query_handler(text="Oltinkul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltinkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinkul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/altynkul/351832/current-weather/351832")
    await call.message.answer(xabar, reply_markup=Oltinkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinkul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/altynkul/351832/daily-weather-forecast/351832")
    await call.message.answer(xabar, reply_markup=Oltinkulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinkuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltinkuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Paxtaobod tumani uchun

@dp.callback_query_handler(text="Paxtaobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtaobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pakhtaabad/351844/current-weather/351844")
    await call.message.answer(xabar, reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtaobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/pakhtaabad/351844/daily-weather-forecast/351844")
    await call.message.answer(xabar, reply_markup=Paxtaobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qurgontepa tumani uchun

@dp.callback_query_handler(text="Qurgontepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qurgontepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qurgontepa Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kurgantepa/351843/current-weather/351843")
    await call.message.answer(xabar, reply_markup=Qurgontepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qurgontepa Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kurgantepa/351843/daily-weather-forecast/351843")
    await call.message.answer(xabar, reply_markup=Qurgontepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qurgontepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qurgontepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Shahrixon  tumani uchun

@dp.callback_query_handler(text="Shahrixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shahrixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrixon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shakhrikhan/351845/current-weather/351845")
    await call.message.answer(xabar, reply_markup=Shahrixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrixon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/shakhrikhan/351845/daily-weather-forecast/351845")
    await call.message.answer(xabar, reply_markup=Shahrixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Ulugnor tumani uchun

@dp.callback_query_handler(text="Ulugnor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ulugnormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ulugnor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/akaltyn/351830/current-weather/351830")
    await call.message.answer(xabar, reply_markup=Ulugnormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ulugnor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/akaltyn/351830/daily-weather-forecast/351830")
    await call.message.answer(xabar, reply_markup=Ulugnormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ulugnordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ulugnordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xujaobod tumani uchun

@dp.callback_query_handler(text="Xujaobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xujaobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujaobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khodzhaabad/351838/current-weather/351838")
    await call.message.answer(xabar, reply_markup=Xujaobodmenu)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="Xujaobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khodzhaabad/351838/daily-weather-forecast/351838")
    await call.message.answer(xabar, reply_markup=Xujaobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujaoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xujaoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xonabod tumani uchun

@dp.callback_query_handler(text="Xonabod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xonabodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonabod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khanabadskiy/351837/current-weather/351837")
    await call.message.answer(xabar, reply_markup=Xonabodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonabod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khanabadskiy/351837/daily-weather-forecast/351837")
    await call.message.answer(xabar, reply_markup=Xonabodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonaboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonaboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Asaka tumani uchun

@dp.callback_query_handler(text="Asaka")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Asakamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Asaka Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/assake/351846/current-weather/351846")
    await call.message.answer(xabar, reply_markup=Asakamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Asaka Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/assake/351846/daily-weather-forecast/351846")
    await call.message.answer(xabar, reply_markup=Asakamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Asakadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=andijon_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Asakadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)





#    Buxoro viloyati



@dp.callback_query_handler(text="Buxoro")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


#    Buxoroshahar   tumani uchun

@dp.callback_query_handler(text="Buxoroshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buxoromenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buxoro Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bukhara/352479/current-weather/352479")
    await call.message.answer(xabar, reply_markup=Buxoromenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buxoro Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bukhara/352479/daily-weather-forecast/352479")
    await call.message.answer(xabar, reply_markup=Buxoromenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buxorodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buxorodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Gijduvon  tumani uchun

@dp.callback_query_handler(text="Gijduvon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gijduvonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gijduvon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gizhduvan/352490/current-weather/352490")
    await call.message.answer(xabar, reply_markup=Gijduvonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gijduvon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/gizhduvan/352490/daily-weather-forecast/352490")
    await call.message.answer(xabar, reply_markup=Gijduvonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gijduvondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gijduvondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Jondor tumani uchun

@dp.callback_query_handler(text="Jondor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jondormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jondor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zhondor/352486/current-weather/352486")
    await call.message.answer(xabar, reply_markup=Jondormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jondor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/zhondor/352486/daily-weather-forecast/352486")
    await call.message.answer(xabar, reply_markup=Jondormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jondordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jondordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Kogon tumani uchun

@dp.callback_query_handler(text="Kogon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kogonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kogon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kagan/352492/current-weather/352492")
    await call.message.answer(xabar, reply_markup=Kogonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kogon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kagan/352492/daily-weather-forecast/352492")
    await call.message.answer(xabar, reply_markup=Kogonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kogondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kogondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Olot tumani uchun

@dp.callback_query_handler(text="Olot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Olotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Olot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/alat/352480/current-weather/352480")
    await call.message.answer(xabar, reply_markup=Olotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Olot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/alat/352480/daily-weather-forecast/352480")
    await call.message.answer(xabar, reply_markup=Olotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Olotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Olotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Peshku tumani uchun

@dp.callback_query_handler(text="Peshku")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Peshkumenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Peshku Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/peshku/720257/current-weather/720257")
    await call.message.answer(xabar, reply_markup=Peshkumenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Peshku Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/daily-weather-forecast/355666")
    await call.message.answer(xabar, reply_markup=Peshkumenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Peshkudan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Peshkudan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qorakul tumani uchun

@dp.callback_query_handler(text="Qorakul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorakulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorakul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karakul/352482/current-weather/352482")
    await call.message.answer(xabar, reply_markup=Qorakulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorakul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/karakul/352482/daily-weather-forecast/352482")
    await call.message.answer(xabar, reply_markup=Qorakulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorakuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorakuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Qorovulbozor  tumani uchun

@dp.callback_query_handler(text="Qorovulbozor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorovulbozor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/karaulbazar/352484/current-weather/352484")
    await call.message.answer(xabar, reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorovulbozor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/karaulbazar/352484/daily-weather-forecast/352484")
    await call.message.answer(xabar, reply_markup=Qorovulbozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorovulbozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qorovulbozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Romitan tumani uchun

@dp.callback_query_handler(text="Romitan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Romitanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Romitan Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/romiton/720199/current-weather/720199")
    await call.message.answer(xabar, reply_markup=Romitanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Romitan Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/romiton/720199/daily-weather-forecast/720199")
    await call.message.answer(xabar, reply_markup=Romitanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Romitandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Romitandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Shofirkon tumani uchun

@dp.callback_query_handler(text="Shofirkon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shofirkonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shofirkon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shafirkan/352494/current-weather/352494")
    await call.message.answer(xabar, reply_markup=Shofirkonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shofirkon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/shafirkan/352494/daily-weather-forecast/352494")
    await call.message.answer(xabar, reply_markup=Shofirkonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shofirkondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shofirkondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Vobkent  tumani uchun

@dp.callback_query_handler(text="Vobkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Vobkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Vobkent Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/vabkent/352496/current-weather/352496")
    await call.message.answer(xabar, reply_markup=Vobkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Vobkent Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/vabkent/352496/daily-weather-forecast/352496")
    await call.message.answer(xabar, reply_markup=Vobkentmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Vobkentdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=buxoro_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Vobkentdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#    Fargona viloyati



@dp.callback_query_handler(text="Fargona")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


#    Fargonashahar   tumani uchun

@dp.callback_query_handler(text="Fargonashahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Fargonamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Fargona Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/fergana/353238/current-weather/353238")
    await call.message.answer(xabar, reply_markup=Fargonamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Fargona Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/fergana/353238/daily-weather-forecast/353238")
    await call.message.answer(xabar, reply_markup=Fargonamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Fargonadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Fargonadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Yozyovon  tumani uchun

@dp.callback_query_handler(text="Yozyovon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yozyovonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yozyovon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yaz%E2%80%9Dyavan/353257/current-weather/353257")
    await call.message.answer(xabar, reply_markup=Yozyovonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yozyovon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yaz%E2%80%9Dyavan/353257/daily-weather-forecast/353257")
    await call.message.answer(xabar, reply_markup=Yozyovonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yozyovondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yozyovondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Beshariq tumani uchun

@dp.callback_query_handler(text="Beshariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Beshariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beshariq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beshariq/353247/current-weather/353247")
    await call.message.answer(xabar, reply_markup=Beshariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beshariq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/beshariq/353247/daily-weather-forecast/353247")
    await call.message.answer(xabar, reply_markup=Beshariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beshariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Beshariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Bogdod tumani uchun

@dp.callback_query_handler(text="Bogdod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bogdodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogdod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bagdod/721991/current-weather/721991")
    await call.message.answer(xabar, reply_markup=Bogdodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogdod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bagdod/721991/daily-weather-forecast/721991")
    await call.message.answer(xabar, reply_markup=Bogdodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogdoddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogdoddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Buvayda tumani uchun

@dp.callback_query_handler(text="Buvayda")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Buvaydamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buvayda Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/buvayda/721803/current-weather/721803")
    await call.message.answer(xabar, reply_markup=Buvaydamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buvayda Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/buvayda/721803/daily-weather-forecast/721803")
    await call.message.answer(xabar, reply_markup=Buvaydamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buvaydadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Buvaydadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Dangara tumani uchun

@dp.callback_query_handler(text="Dangara")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dangaramenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dangara Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dangara/353248/current-weather/353248")
    await call.message.answer(xabar, reply_markup=Dangaramenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dangara Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dangara/353248/daily-weather-forecast/353248")
    await call.message.answer(xabar, reply_markup=Dangaramenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dangaradan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dangaradan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Furqat tumani uchun

@dp.callback_query_handler(text="Furqat")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Furqatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Furqat Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nawbahor/353251/current-weather/353251")
    await call.message.answer(xabar, reply_markup=Furqatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Furqat Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nawbahor/353251/daily-weather-forecast/353251")
    await call.message.answer(xabar, reply_markup=Furqatmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Furqatdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Furqatdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Uzbekiston tumani uchun

@dp.callback_query_handler(text="Uzbekiston")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzbekiston Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yaypan/353262/current-weather/353262")
    await call.message.answer(xabar, reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzbekiston Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yaypan/353262/daily-weather-forecast/353262")
    await call.message.answer(xabar, reply_markup=Uzbekistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzbekistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uzbekistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Oltiariq tumani uchun

@dp.callback_query_handler(text="Oltiariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oltiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltiariq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/altyaryk/353245/current-weather/353245")
    await call.message.answer(xabar, reply_markup=Oltiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltiariq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/altyaryk/353245/daily-weather-forecast/353245")
    await call.message.answer(xabar, reply_markup=Oltiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oltiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Quqon tumani uchun

@dp.callback_query_handler(text="Quqon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quqonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quqon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kokand/353243/current-weather/353243")
    await call.message.answer(xabar, reply_markup=Quqonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quqon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kokand/353243/daily-weather-forecast/353243")
    await call.message.answer(xabar, reply_markup=Quqonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quqondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quqondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Qushtepa  tumani uchun

@dp.callback_query_handler(text="Qushtepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushtepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushtepa Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/langar/1704277/current-weather/1704277")
    await call.message.answer(xabar, reply_markup=Qushtepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushtepa Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/langar/1704277/daily-weather-forecast/1704277")
    await call.message.answer(xabar, reply_markup=Qushtepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushtepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushtepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Quva tumani uchun

@dp.callback_query_handler(text="Quva")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Quvamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quva Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kuva/353259/current-weather/353259")
    await call.message.answer(xabar, reply_markup=Quvamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quva Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kuva/353259/daily-weather-forecast/353259")
    await call.message.answer(xabar, reply_markup=Quvamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quvadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Quvadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Rishton tumani uchun

@dp.callback_query_handler(text="Rishton")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Rishtonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Rishton Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/rishton/353252/current-weather/353252")
    await call.message.answer(xabar, reply_markup=Rishtonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Rishton Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/rishton/353252/daily-weather-forecast/353252")
    await call.message.answer(xabar, reply_markup=Rishtonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Rishtondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Rishtondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Sux tumani uchun

@dp.callback_query_handler(text="Sux")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Suxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sux Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sokh/353244/current-weather/353244")
    await call.message.answer(xabar, reply_markup=Suxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sux Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sokh/353244/daily-weather-forecast/353244")
    await call.message.answer(xabar, reply_markup=Suxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Suxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Suxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Toshloq tumani uchun

@dp.callback_query_handler(text="Toshloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Toshloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshloq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/toshloq/353253/current-weather/353253")
    await call.message.answer(xabar, reply_markup=Toshloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshloq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/toshloq/353253/daily-weather-forecast/353253")
    await call.message.answer(xabar, reply_markup=Toshloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Toshloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Uchkuprik tumani uchun

@dp.callback_query_handler(text="Uchkuprik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchkuprik Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchkuprik/353254/current-weather/353254")
    await call.message.answer(xabar, reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchkuprik Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/uchkuprik/353254/daily-weather-forecast/353254")
    await call.message.answer(xabar, reply_markup=Uchkuprikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchkuprikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=fargona_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchkuprikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)






#    Jizzax viloyati



@dp.callback_query_handler(text="Jizzax")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


#    Jizzaxshahar   tumani uchun

@dp.callback_query_handler(text="Jizzaxshahar")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jizzaxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jizzax Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Jizzaxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jizzax Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/daily-weather-forecast/348390")
    await call.message.answer(xabar, reply_markup=Jizzaxmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jizzaxdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jizzaxdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Zomin tumani uchun

@dp.callback_query_handler(text="Zomin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zominmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zomin Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zaamin/354217/current-weather/354217")
    await call.message.answer(xabar, reply_markup=Zominmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zomin Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/zaamin/354217/daily-weather-forecast/354217")
    await call.message.answer(xabar, reply_markup=Zominmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zomindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zomindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#     Arnasoy tumani uchun

@dp.callback_query_handler(text="Arnasoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Arnasoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Arnasoy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/arnasay/1618452/current-weather/1618452")
    await call.message.answer(xabar, reply_markup=Arnasoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Arnasoy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/arnasay/1618452/daily-weather-forecast/1618452")
    await call.message.answer(xabar, reply_markup=Arnasoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Arnasoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Arnasoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Baxmal tumani uchun

@dp.callback_query_handler(text="Baxmal")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Baxmalmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baxmal Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/en/uz/bakhmal/721977/current-weather/721977")
    await call.message.answer(xabar, reply_markup=Baxmalmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baxmal Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/en/uz/bakhmal/721977/daily-weather-forecast/721977")
    await call.message.answer(xabar, reply_markup=Baxmalmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baxmaldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Baxmaldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Dustlik tumani uchun

@dp.callback_query_handler(text="Dustlik")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dustlikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dustlik Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dustlik/354202/current-weather/354202")
    await call.message.answer(xabar, reply_markup=Dustlikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dustlik Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dustlik/354202/daily-weather-forecast/354202")
    await call.message.answer(xabar, reply_markup=Dustlikmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dustlikdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dustlikdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Forish tumani uchun

@dp.callback_query_handler(text="Forish")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Forishmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Forish Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/farish/721469/current-weather/721469")
    await call.message.answer(xabar, reply_markup=Forishmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Forish Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/farish/721469/daily-weather-forecast/721469")
    await call.message.answer(xabar, reply_markup=Forishmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Forishdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Forishdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Gallaorol tumani uchun

@dp.callback_query_handler(text="Gallaorol")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gallaorolmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gallaorol Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gallyaaral/354212/current-weather/354212")
    await call.message.answer(xabar, reply_markup=Gallaorolmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gallaorol Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/gallyaaral/354212/daily-weather-forecast/354212")
    await call.message.answer(xabar, reply_markup=Gallaorolmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gallaoroldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gallaoroldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Mirzachul tumani uchun

@dp.callback_query_handler(text="Mirzachul")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mirzachulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirzachul Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gagarin/354203/current-weather/354203")
    await call.message.answer(xabar, reply_markup=Mirzachulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirzachul Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/gagarin/354203/daily-weather-forecast/354203")
    await call.message.answer(xabar, reply_markup=Mirzachulmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirzachuldan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirzachuldan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Paxtakor tumani uchun

@dp.callback_query_handler(text="Paxtakor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtakormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtakor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pakhtakor/354205/current-weather/354205")
    await call.message.answer(xabar, reply_markup=Paxtakormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtakor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/pakhtakor/354205/daily-weather-forecast/354205")
    await call.message.answer(xabar, reply_markup=Paxtakormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtakordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtakordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yangiobod tumani uchun

@dp.callback_query_handler(text="Yangiobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Yangiobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/daily-weather-forecast/348390")
    await call.message.answer(xabar, reply_markup=Yangiobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangioboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangioboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Zafarobod  tumani uchun

@dp.callback_query_handler(text="Zafarobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zafarobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zafarobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zafarabad/354209/current-weather/354209")
    await call.message.answer(xabar, reply_markup=Zafarobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zafarobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/zafarabad/354209/daily-weather-forecast/354209")
    await call.message.answer(xabar, reply_markup=Zafarobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zafaroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zafaroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Zarband tumani uchun

@dp.callback_query_handler(text="Zarband")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zarbandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarband Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/current-weather/348390")
    await call.message.answer(xabar, reply_markup=Zarbandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarband Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/jizzakh/348390/daily-weather-forecast/348390")
    await call.message.answer(xabar, reply_markup=Zarbandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarbanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=jizzax_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarbanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)







#    Xorazm viloyati



@dp.callback_query_handler(text="Xorazm")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


#    Urganch   shahar uchun

@dp.callback_query_handler(text="Urganch")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urganchmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urganch Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/urgench/356378/current-weather/356378")
    await call.message.answer(xabar, reply_markup=Urganchmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urganch Haftalik")
async def buy_courses(call: CallbackQuery):
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/urgench/356378/daily-weather-forecast/356378")
    await call.message.answer(xabar, reply_markup=Urganchmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urganchdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urganchdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yangibozor tumani uchun

@dp.callback_query_handler(text="Yangibozor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangibozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangibozor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangibazar/356401/current-weather/356401")
    await call.message.answer(xabar, reply_markup=Yangibozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangibozor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangibazar/356401/daily-weather-forecast/356401")
    await call.message.answer(xabar, reply_markup=Yangibozormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangibozordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangibozordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Bogot   tumani uchun

@dp.callback_query_handler(text="Bogot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bogotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bagat/356387/current-weather/356387")
    await call.message.answer(xabar, reply_markup=Bogotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bagat/356387/daily-weather-forecast/356387")
    await call.message.answer(xabar, reply_markup=Bogotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bogotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Gurlan tumani uchun

@dp.callback_query_handler(text="Gurlan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gurlanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gurlan Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/gurlan/356381/current-weather/356381")
    await call.message.answer(xabar, reply_markup=Gurlanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gurlan Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/gurlan/356381/daily-weather-forecast/356381")
    await call.message.answer(xabar, reply_markup=Gurlanmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gurlandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gurlandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Qushkupir tumani uchun

@dp.callback_query_handler(text="Qushkupir")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushkupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushkupir Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qushkupir/356384/current-weather/356384")
    await call.message.answer(xabar, reply_markup=Qushkupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushkupir Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/qushkupir/356384/daily-weather-forecast/356384")
    await call.message.answer(xabar, reply_markup=Qushkupirmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushkupirdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushkupirdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Shovot tumani uchun

@dp.callback_query_handler(text="Shovot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shovotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shovot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/showot/356385/current-weather/356385")
    await call.message.answer(xabar, reply_markup=Shovotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shovot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/showot/356385/daily-weather-forecast/356385")
    await call.message.answer(xabar, reply_markup=Shovotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shovotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shovotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xazorasp tumani uchun

@dp.callback_query_handler(text="Xazorasp")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xazoraspmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xazorasp Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/hazorasp/356382/current-weather/356382")
    await call.message.answer(xabar, reply_markup=Xazoraspmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xazorasp Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/hazorasp/356382/daily-weather-forecast/356382")
    await call.message.answer(xabar, reply_markup=Xazoraspmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xazoraspdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xazoraspdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xiva tumani uchun

@dp.callback_query_handler(text="Xiva")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xivamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xiva Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khiva/356380/current-weather/356380")
    await call.message.answer(xabar, reply_markup=Xivamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xiva Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khiva/356380/daily-weather-forecast/356380")
    await call.message.answer(xabar, reply_markup=Xivamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xivadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xivadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Xonqa tumani uchun

@dp.callback_query_handler(text="Xonqa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xonqamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonqa Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khonqa/356383/current-weather/356383")
    await call.message.answer(xabar, reply_markup=Xonqamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonqa Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khonqa/356383/daily-weather-forecast/356383")
    await call.message.answer(xabar, reply_markup=Xonqamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonqadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xonqadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yangiariq tumani uchun

@dp.callback_query_handler(text="Yangiariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiariq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiaryk/356400/current-weather/356400")
    await call.message.answer(xabar, reply_markup=Yangiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiariq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangiaryk/356400/daily-weather-forecast/356400")
    await call.message.answer(xabar, reply_markup=Yangiariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=xorazm_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#    Namangan viloyati



@dp.callback_query_handler(text="Namangan")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


#    Namanganshahri   shahar  uchun

@dp.callback_query_handler(text="Namanganshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Namanganmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Namangan Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/current-weather/355095")
    await call.message.answer(xabar, reply_markup=Namanganmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Namangan Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/daily-weather-forecast/355095")
    await call.message.answer(xabar, reply_markup=Namanganmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Namangandan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Namangandan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Chortoq tumani uchun

@dp.callback_query_handler(text="Chortoq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chortoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chortoq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/current-weather/355095")
    await call.message.answer(xabar, reply_markup=Chortoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chortoq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/namangan/355095/daily-weather-forecast/355095")
    await call.message.answer(xabar, reply_markup=Chortoqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chortoqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chortoqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Chust   tumani uchun

@dp.callback_query_handler(text="Chust")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chustmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chust Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chust/355107/current-weather/355107")
    await call.message.answer(xabar, reply_markup=Chustmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chust Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chust/355107/daily-weather-forecast/355107")
    await call.message.answer(xabar, reply_markup=Chustmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chustdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chustdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Kosonsoy tumani uchun

@dp.callback_query_handler(text="Kosonsoy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kosonsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosonsoy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasansay/355108/current-weather/355108")
    await call.message.answer(xabar, reply_markup=Kosonsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosonsoy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kasansay/355108/daily-weather-forecast/355108")
    await call.message.answer(xabar, reply_markup=Kosonsoymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosonsoydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosonsoydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Mingbuloq tumani uchun

@dp.callback_query_handler(text="Mingbuloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mingbuloq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhumashuy/355097/current-weather/355097")
    await call.message.answer(xabar, reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mingbuloq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dzhumashuy/355097/daily-weather-forecast/355097")
    await call.message.answer(xabar, reply_markup=Mingbuloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mingbuloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mingbuloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Norin tumani uchun

@dp.callback_query_handler(text="Norin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Norinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Norin Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/naryn/355100/current-weather/355100")
    await call.message.answer(xabar, reply_markup=Norinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Norin Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/naryn/355100/daily-weather-forecast/355100")
    await call.message.answer(xabar, reply_markup=Norinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Norindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Norindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Pop tumani uchun

@dp.callback_query_handler(text="Pop")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Popmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pop Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/pap/355102/current-weather/355102")
    await call.message.answer(xabar, reply_markup=Popmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pop Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/pap/355102/daily-weather-forecast/355102")
    await call.message.answer(xabar, reply_markup=Popmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Popdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Popdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Turaqurgon tumani uchun

@dp.callback_query_handler(text="Turaqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turaqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/turakurgan/355103/current-weather/355103")
    await call.message.answer(xabar, reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turaqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/turakurgan/355103/daily-weather-forecast/355103")
    await call.message.answer(xabar, reply_markup=Turaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Turaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Uchqurgon tumani uchun

@dp.callback_query_handler(text="Uchqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchkurgan/355110/current-weather/355110")
    await call.message.answer(xabar, reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/uchkurgan/355110/daily-weather-forecast/355110")
    await call.message.answer(xabar, reply_markup=Uchqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Uychi tumani uchun

@dp.callback_query_handler(text="Uychi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uychimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uychi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uychi/355111/current-weather/355111")
    await call.message.answer(xabar, reply_markup=Uychimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uychi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/uychi/355111/daily-weather-forecast/355111")
    await call.message.answer(xabar, reply_markup=Uychimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uychidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uychidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Yangiqurgon tumani uchun

@dp.callback_query_handler(text="Yangiqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangikurgan/355112/current-weather/355112")
    await call.message.answer(xabar, reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangikurgan/355112/daily-weather-forecast/355112")
    await call.message.answer(xabar, reply_markup=Yangiqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=namangan_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)









#    Navoiy viloyati



@dp.callback_query_handler(text="Navoiy")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


#    Navoiyshahri   shahar  uchun

@dp.callback_query_handler(text="Navoiyshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Navoiymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navoiy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/current-weather/355115")
    await call.message.answer(xabar, reply_markup=Navoiymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navoiy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/daily-weather-forecast/355115")
    await call.message.answer(xabar, reply_markup=Navoiymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navoiydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navoiydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Zarafshon  tumani uchun

@dp.callback_query_handler(text="Zarafshon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Zarafshonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarafshon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/zarafshan/355142/current-weather/355142")
    await call.message.answer(xabar, reply_markup=Zarafshonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarafshon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/zarafshan/355142/daily-weather-forecast/355142")
    await call.message.answer(xabar, reply_markup=Zarafshonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarafshondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Zarafshondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Karmana   tumani uchun

@dp.callback_query_handler(text="Karmana")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Karmanamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Karmana Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/current-weather/355115")
    await call.message.answer(xabar, reply_markup=Karmanamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Karmana Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/navoiy/355115/daily-weather-forecast/355115")
    await call.message.answer(xabar, reply_markup=Karmanamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Karmanadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Karmanadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Konimex tumani uchun

@dp.callback_query_handler(text="Konimex")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Konimexmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Konimex Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kanimekh/355133/current-weather/355133")
    await call.message.answer(xabar, reply_markup=Konimexmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Konimex Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kanimekh/355133/daily-weather-forecast/355133")
    await call.message.answer(xabar, reply_markup=Konimexmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Konimexdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Konimexdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Navbahor tumani uchun

@dp.callback_query_handler(text="Navbahor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Navbahormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navbahor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/beshrabot/355118/current-weather/355118")
    await call.message.answer(xabar, reply_markup=Navbahormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navbahor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/beshrabot/355118/daily-weather-forecast/355118")
    await call.message.answer(xabar, reply_markup=Navbahormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navbahordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Navbahordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Nurota tumani uchun

@dp.callback_query_handler(text="Nurota")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nurotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurota Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nurata/355117/current-weather/355117")
    await call.message.answer(xabar, reply_markup=Nurotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurota Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nurata/355117/daily-weather-forecast/355117")
    await call.message.answer(xabar, reply_markup=Nurotamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurotadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurotadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qiziltepa tumani uchun

@dp.callback_query_handler(text="Qiziltepa")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qiziltepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziltepa Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kyzyltepa/355122/current-weather/355122")
    await call.message.answer(xabar, reply_markup=Qiziltepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziltepa Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kyzyltepa/355122/daily-weather-forecast/355122")
    await call.message.answer(xabar, reply_markup=Qiziltepamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziltepadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qiziltepadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Tomdi tumani uchun

@dp.callback_query_handler(text="Tomdi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Tomdimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tomdi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/tamdybulak/355139/current-weather/355139")
    await call.message.answer(xabar, reply_markup=Tomdimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tomdi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/tamdybulak/355139/daily-weather-forecast/355139")
    await call.message.answer(xabar, reply_markup=Tomdimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tomdidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tomdidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Uchquduq tumani uchun

@dp.callback_query_handler(text="Uchquduq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Uchquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchquduq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/uchquduq/355125/current-weather/355125")
    await call.message.answer(xabar, reply_markup=Uchquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchquduq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/uchquduq/355125/daily-weather-forecast/355125")
    await call.message.answer(xabar, reply_markup=Uchquduqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchquduqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Uchquduqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Xatirchi tumani uchun

@dp.callback_query_handler(text="Xatirchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xatirchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xatirchi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khatyrchi/720956/current-weather/720956")
    await call.message.answer(xabar, reply_markup=Xatirchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xatirchi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khatyrchi/720956/daily-weather-forecast/720956")
    await call.message.answer(xabar, reply_markup=Xatirchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xatirchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=navoiy_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xatirchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)







#    Qashqadaryo viloyati



@dp.callback_query_handler(text="Qashqadaryo")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


#    Qarshi   shahar  uchun

@dp.callback_query_handler(text="Qarshi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qarshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qarshi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/qarshi/350541/current-weather/350541")
    await call.message.answer(xabar, reply_markup=Qarshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qarshi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/qarshi/350541/daily-weather-forecast/350541")
    await call.message.answer(xabar, reply_markup=Qarshimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qarshidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qarshidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Chiroqchi  tumani uchun

@dp.callback_query_handler(text="Chiroqchi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Chiroqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chiroqchi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/chirakchi/355641/current-weather/355641")
    await call.message.answer(xabar, reply_markup=Chiroqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chiroqchi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/chirakchi/355641/daily-weather-forecast/355641")
    await call.message.answer(xabar, reply_markup=Chiroqchimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chiroqchidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Chiroqchidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Dehqonobod   tumani uchun

@dp.callback_query_handler(text="Dehqonobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dehqonobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dekhkanabad/355653/current-weather/355653")
    await call.message.answer(xabar, reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dehqonobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dekhkanabad/355653/daily-weather-forecast/355653")
    await call.message.answer(xabar, reply_markup=Dehqonobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dehqonoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Dehqonoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Guzor tumani uchun

@dp.callback_query_handler(text="Guzor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Guzormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guzor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guzar/355639/current-weather/355639")
    await call.message.answer(xabar, reply_markup=Guzormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guzor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/guzar/355639/daily-weather-forecast/355639")
    await call.message.answer(xabar, reply_markup=Guzormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guzordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guzordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Kasbi tumani uchun

@dp.callback_query_handler(text="Kasbi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kasbimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kasbi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasbi/355660/current-weather/355660")
    await call.message.answer(xabar, reply_markup=Kasbimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kasbi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kasbi/355660/daily-weather-forecast/355660")
    await call.message.answer(xabar, reply_markup=Kasbimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kasbidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kasbidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Kitob tumani uchun

@dp.callback_query_handler(text="Kitob")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kitobmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kitob Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kitab/355643/current-weather/355643")
    await call.message.answer(xabar, reply_markup=Kitobmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kitob Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kitab/355643/daily-weather-forecast/355643")
    await call.message.answer(xabar, reply_markup=Kitobmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kitobdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kitobdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#    Koson  tumani uchun

@dp.callback_query_handler(text="Koson")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kosonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Koson Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kasan/355659/current-weather/355659")
    await call.message.answer(xabar, reply_markup=Kosonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Koson Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kasan/355659/daily-weather-forecast/355659")
    await call.message.answer(xabar, reply_markup=Kosonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kosondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Mirishkor tumani uchun

@dp.callback_query_handler(text="Mirishkor")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Mirishkormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirishkor Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/en/uz/yangi-mirishkor/720478/current-weather/720478")
    await call.message.answer(xabar, reply_markup=Mirishkormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirishkor Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/en/uz/yangi-mirishkor/720478/daily-weather-forecast/720478")
    await call.message.answer(xabar, reply_markup=Mirishkormenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirishkordan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Mirishkordan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Muborak tumani uchun

@dp.callback_query_handler(text="Muborak")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Muborakmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muborak Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/mubarek/355663/current-weather/355663")
    await call.message.answer(xabar, reply_markup=Muborakmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muborak Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/mubarek/355663/daily-weather-forecast/355663")
    await call.message.answer(xabar, reply_markup=Muborakmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muborakdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Muborakdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Nishon tumani uchun

@dp.callback_query_handler(text="Nishon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nishonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nishon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nishon/720357/current-weather/720357")
    await call.message.answer(xabar, reply_markup=Nishonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nishon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nishon/720357/daily-weather-forecast/720357")
    await call.message.answer(xabar, reply_markup=Nishonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nishondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nishondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Qamashi tumani uchun

@dp.callback_query_handler(text="Qamashi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qamashimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qamashi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kamashi/355656/current-weather/355656")
    await call.message.answer(xabar, reply_markup=Qamashimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qamashi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kamashi/355656/daily-weather-forecast/355656")
    await call.message.answer(xabar, reply_markup=Qamashimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qamashidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qamashidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Shahrisabz tumani uchun

@dp.callback_query_handler(text="Shahrisabz")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrisabz Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/shakhrisabz/355647/current-weather/355647")
    await call.message.answer(xabar, reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrisabz Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/shakhrisabz/355647/daily-weather-forecast/355647")
    await call.message.answer(xabar, reply_markup=Shahrisabzmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrisabzdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Shahrisabzdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yakkabog tumani uchun

@dp.callback_query_handler(text="Yakkabog")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yakkabogmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yakkabog Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yakkabag/355665/current-weather/355665")
    await call.message.answer(xabar, reply_markup=Yakkabogmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yakkabog Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yakkabag/355665/daily-weather-forecast/355665")
    await call.message.answer(xabar, reply_markup=Yakkabogmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yakkabogdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=qashqadaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yakkabogdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)











#    Samarqand viloyati



@dp.callback_query_handler(text="Samarqand")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


#    Samarqand   shahar  uchun

@dp.callback_query_handler(text="Samarqandshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Samarqandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Samarqand Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/current-weather/355666")
    await call.message.answer(xabar, reply_markup=Samarqandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Samarqand Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nukus/355666/daily-weather-forecast/355666")
    await call.message.answer(xabar, reply_markup=Samarqandmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Samarqanddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Samarqanddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Urgut  tumani uchun

@dp.callback_query_handler(text="Urgut")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Urgutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urgut Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/urgut/355795/current-weather/355795")
    await call.message.answer(xabar, reply_markup=Urgutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urgut Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/urgut/355795/daily-weather-forecast/355795")
    await call.message.answer(xabar, reply_markup=Urgutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urgutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Urgutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Bulungur   tumani uchun

@dp.callback_query_handler(text="Bulungur")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Bulungurmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bulungur Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/bulungur/355781/current-weather/355781")
    await call.message.answer(xabar, reply_markup=Bulungurmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bulungur Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/bulungur/355781/daily-weather-forecast/355781")
    await call.message.answer(xabar, reply_markup=Bulungurmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bulungurdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bulungurdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Ishtixon tumani uchun

@dp.callback_query_handler(text="Ishtixon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Ishtixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ishtixon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ishtykhan/355788/current-weather/355788")
    await call.message.answer(xabar, reply_markup=Ishtixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ishtixon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/ishtykhan/355788/daily-weather-forecast/355788")
    await call.message.answer(xabar, reply_markup=Ishtixonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ishtixondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Ishtixondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Jomboy tumani uchun

@dp.callback_query_handler(text="Jomboy")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Jomboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jomboy Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhambay/355785/current-weather/355785")
    await call.message.answer(xabar, reply_markup=Jomboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jomboy Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dzhambay/355785/daily-weather-forecast/355785")
    await call.message.answer(xabar, reply_markup=Jomboymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jomboydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Jomboydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Kattaqurgon tumani uchun

@dp.callback_query_handler(text="Kattaqurgon")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kattaqurgon Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/kattaqurghon/355778/current-weather/355778")
    await call.message.answer(xabar, reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kattaqurgon Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/kattaqurghon/355778/daily-weather-forecast/355778")
    await call.message.answer(xabar, reply_markup=Kattaqurgonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kattaqurgondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Kattaqurgondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#    Narpay  tumani uchun

@dp.callback_query_handler(text="Narpay")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Narpaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Narpay Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/aktash/355797/current-weather/355797")
    await call.message.answer(xabar, reply_markup=Narpaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Narpay Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/aktash/355797/daily-weather-forecast/355797")
    await call.message.answer(xabar, reply_markup=Narpaymenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Narpaydan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Narpaydan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Nurobod tumani uchun

@dp.callback_query_handler(text="Nurobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Nurobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/nurobod/719969/current-weather/719969")
    await call.message.answer(xabar, reply_markup=Nurobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nurobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/nurobod/719969/daily-weather-forecast/719969")
    await call.message.answer(xabar, reply_markup=Nurobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nuroboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Nuroboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Oqdaryo tumani uchun

@dp.callback_query_handler(text="Oqdaryo")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqdaryo Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/laish/355792/current-weather/355792")
    await call.message.answer(xabar, reply_markup=Oqdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqdaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/laish/355792/daily-weather-forecast/355792")
    await call.message.answer(xabar, reply_markup=Oqdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Pastdargom tumani uchun

@dp.callback_query_handler(text="Pastdargom")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Pastdargommenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pastdargom Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/dzhuma/355786/current-weather/355786")
    await call.message.answer(xabar, reply_markup=Pastdargommenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pastdargom Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/dzhuma/355786/daily-weather-forecast/355786")
    await call.message.answer(xabar, reply_markup=Pastdargommenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pastdargomdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Pastdargomdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Paxtachi tumani uchun

@dp.callback_query_handler(text="Paxtachi")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Paxtachimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtachi Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/ziadin/355143/current-weather/355143")
    await call.message.answer(xabar, reply_markup=Paxtachimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtachi Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/ziadin/355143/cdaily-weather-forecast/355143")
    await call.message.answer(xabar, reply_markup=Paxtachimenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtachidan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Paxtachidan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Poyariq tumani uchun

@dp.callback_query_handler(text="Poyariq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Poyariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Poyariq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/payariq/720402/current-weather/720402")
    await call.message.answer(xabar, reply_markup=Poyariqmenu)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="Poyariq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/payariq/720402/daily-weather-forecast/720402")
    await call.message.answer(xabar, reply_markup=Poyariqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Poyariqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Poyariqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Qushrabot tumani uchun

@dp.callback_query_handler(text="Qushrabot")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Qushrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushrabot Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/koshrabad/355789/current-weather/355789")
    await call.message.answer(xabar, reply_markup=Qushrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushrabot Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/koshrabad/355789/daily-weather-forecast/355789")
    await call.message.answer(xabar, reply_markup=Qushrabotmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushrabotdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Qushrabotdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)






#   Tayloq tumani uchun

@dp.callback_query_handler(text="Tayloq")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Tayloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tayloq Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/taylak/355794/current-weather/355794")
    await call.message.answer(xabar, reply_markup=Tayloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tayloq Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/taylak/355794/daily-weather-forecast/355794")
    await call.message.answer(xabar, reply_markup=Tayloqmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tayloqdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=samarqand_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Tayloqdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)





#    Sirdaryo viloyati



@dp.callback_query_handler(text="Sirdaryo")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


#    Sirdaryo   shahar  uchun

@dp.callback_query_handler(text="Sirdaryoshahri")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sirdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sirdaryo Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/current-weather/355934")
    await call.message.answer(xabar, reply_markup=Sirdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sirdaryo Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/daily-weather-forecast/355934")
    await call.message.answer(xabar, reply_markup=Sirdaryomenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sirdaryodan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sirdaryodan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#  Boyovut  tumani uchun

@dp.callback_query_handler(text="Boyovut")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Boyovutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boyovut Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/current-weather/355927")
    await call.message.answer(xabar, reply_markup=Boyovutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boyovut Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/daily-weather-forecast/355927")
    await call.message.answer(xabar, reply_markup=Boyovutmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boyovutdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Boyovutdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Guliston   tumani uchun

@dp.callback_query_handler(text="Guliston")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Gulistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guliston Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/current-weather/355927")
    await call.message.answer(xabar, reply_markup=Gulistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Guliston Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/guliston/355927/daily-weather-forecast/355927")
    await call.message.answer(xabar, reply_markup=Gulistonmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gulistondan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Gulistondan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Oqoltin tumani uchun

@dp.callback_query_handler(text="Oqoltin")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Oqoltinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqoltin Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/current-weather/355932")
    await call.message.answer(xabar, reply_markup=Oqoltinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqoltin Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/daily-weather-forecast/355932")
    await call.message.answer(xabar, reply_markup=Oqoltinmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqoltindan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Oqoltindan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)




#   Sardoba  tumani uchun

@dp.callback_query_handler(text="Sardoba")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sardobamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sardoba Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/current-weather/355932")
    await call.message.answer(xabar, reply_markup=Sardobamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sardoba Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sardoba/355932/daily-weather-forecast355932")
    await call.message.answer(xabar, reply_markup=Sardobamenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sardobadan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sardobadan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)



#   Sayxunobod tumani uchun

@dp.callback_query_handler(text="Sayxunobod")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sayxunobod Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/current-weather/355934")
    await call.message.answer(xabar, reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sayxunobod Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/sirdaryo/355934/daily-weather-forecast/355934")
    await call.message.answer(xabar, reply_markup=Sayxunobodmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sayxunoboddan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Sayxunoboddan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#    Xavos  tumani uchun

@dp.callback_query_handler(text="Xavos")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Xavosmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xavos Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/khavast/355928/current-weather/355928")
    await call.message.answer(xabar, reply_markup=Xavosmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xavos Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/khavast/355928/daily-weather-forecast/355928")
    await call.message.answer(xabar, reply_markup=Xavosmenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xavosdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Xavosdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)


#   Yangiyer tumani uchun

@dp.callback_query_handler(text="Yangiyer")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Tanlang</b>✅😎🌤🌤", reply_markup=Yangiyermenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyer Bugun")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = bugun_obhavo("https://www.accuweather.com/uz/uz/yangiyer/355936/current-weather/355936")
    await call.message.answer(xabar, reply_markup=Yangiyermenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyer Haftalik")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    xabar = haftalik_obhavo("https://www.accuweather.com/uz/uz/yangiyer/355936/daily-weather-forecast/355936")
    await call.message.answer(xabar, reply_markup=Yangiyermenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyerdan tumanlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer(f"<b>Tumanni tanlang</b>✅😎🌤🌤", reply_markup=sirdaryo_tumanlari)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Yangiyerdan viloyatlarga qayt")
async def buy_courses(call: CallbackQuery):
    #await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)














@dp.callback_query_handler(text="🔙Ortga")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Viloyatni tanlang", reply_markup=viloyatlarmenu)
    await call.answer(cache_time=60)





