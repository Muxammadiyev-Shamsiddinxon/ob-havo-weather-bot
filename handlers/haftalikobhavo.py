import requests
from bs4 import BeautifulSoup


def haftalik_obhavo(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "referer": "https://www.google.com/"
    }

    site = requests.get(url=url, headers=headers)
    htmldom = BeautifulSoup(site.text, "lxml")

    shahar_j = htmldom.find("div", class_="h1").findAll("a")
    shahar = f" Haftalik ob havo📆✅.\n"  # shu shahar nomi
    for k in shahar_j:
        shahar = shahar + "" + f"{k.text} "

    kunlar_j = htmldom.findAll("h5", class_="b0")
    kunlar_haftalik = []  # 1 haftalik cheslolar
    for k in kunlar_j:
        kunlar_haftalik.append(k.text.strip())

    umumiy_j = htmldom.findAll("div", class_="wtpo")
    shamol = []  # shamol
    for k in umumiy_j:
        shamol.append(k.findAll("b")[2].text)

    kun = htmldom.findAll("td", class_="dtm")
    kun_qismlari = []  # yani oqshom, kechqurun ,kunduzi, shular
    for k in kun:
        kun_qismlari.append(k.findAll("b")[0].text)
    mosvaqtlar = []  # 6:00 dan 12:00 gacha shunaqa oraliqlar
    for k in kun:
        mosvaqtlar.append(k.findAll("i")[0].text)

    havo_j = htmldom.findAll("td", class_="t0")
    havo = []  # havo haqida qisqacha
    for k in havo_j:
        havo.append(k.findAll("b")[2].text)

    temp_j = htmldom.findAll("td", class_="t0")
    temp_u = []
    for k in temp_j:
        temp_u.append({

            k.findAll("b")[0].text, k.findAll("b")[1].text.replace("\xa0", "")

        })

    temp = []  # temp umumiy
    for k in temp_u:
        k = list(k)
        umumiy = f"{min(k)}...{max(k)}"
        temp.append(umumiy)

    quyosh_j = htmldom.findAll("div", class_="f3")
    quyosh = []  # quyosh chiqishi botishi
    for k in quyosh_j:
        quyosh.append(k.findAll("b")[1].text)
        quyosh.append(k.findAll("b")[2].text)

    oy_j = htmldom.findAll("div", class_="f3")
    oy = []  # oy chiqishi botishi
    for k in oy_j:
        oy.append(k.findAll("b")[4].text)
        oy.append(k.findAll("b")[5].text)

    quyosh_oy0 = f"\n<b>☀Quyosh->({quyosh[0]},{quyosh[1]})\n🌙Oy-------->({oy[0]},{oy[1]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy1 = f"\n<b>☀Quyosh->({quyosh[2]},{quyosh[3]})\n🌙Oy-------->({oy[2]},{oy[3]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy2 = f"\n<b>☀Quyosh->({quyosh[4]},{quyosh[5]})\n🌙Oy-------->({oy[4]},{oy[5]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy3 = f"\n<b>☀Quyosh->({quyosh[6]},{quyosh[7]})\n🌙Oy-------->({oy[6]},{oy[7]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy4 = f"\n<b>☀Quyosh->({quyosh[8]},{quyosh[9]})\n🌙Oy-------->({oy[8]},{oy[9]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy5 = f"\n<b>☀Quyosh->({quyosh[10]},{quyosh[11]})\n🌙Oy-------->({oy[10]},{oy[11]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    quyosh_oy6 = f"\n<b>☀Quyosh->({quyosh[12]},{quyosh[13]})\n🌙Oy-------->({oy[12]},{oy[13]})</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖"

    if len(kun_qismlari) == 25:
        ertalab0 = f"<b>{shahar}</b>\n\n\n1️⃣\n<b>{kunlar_haftalik[0]}\n</b>\n{kun_qismlari[0]} {mosvaqtlar[0]}\n<b>{havo[0]}</b>: <b>{temp[0]}</b>\nShamol: {shamol[0]}\n"
        kun0 = ertalab0

        ertalab1 = f"\n\n\n2️⃣\n<b>{kunlar_haftalik[1]}</b>\n\n{kun_qismlari[2]} {mosvaqtlar[2]}\n<b>{havo[2]}</b>: <b>{temp[2]}</b>\n"
        kunduz1 = f"{kun_qismlari[3]} {mosvaqtlar[3]}\n<b>{havo[3]}</b>: <b>{temp[3]}</b>\nShamol: {shamol[2]}\n"
        kun1 = ertalab1 + "" + kunduz1

        ertalab2 = f"\n\n\n3️⃣\n<b>{kunlar_haftalik[2]}</b>\n\n{kun_qismlari[6]} {mosvaqtlar[6]}\n<b>{havo[6]}</b>: <b>{temp[6]}</b>\n"
        kunduz2 = f"{kun_qismlari[7]} {mosvaqtlar[7]}\n<b>{havo[7]}</b>: <b>{temp[7]}</b>\nShamol: {shamol[6]}\n"
        kun2 = ertalab2 + "" + kunduz2

        ertalab3 = f"\n\n\n4️⃣\n<b>{kunlar_haftalik[3]}</b>\n\n{kun_qismlari[10]} {mosvaqtlar[10]}\n<b>{havo[10]}</b>: <b>{temp[10]}</b>\n"
        kunduz3 = f"{kun_qismlari[11]} {mosvaqtlar[11]}\n<b>{havo[11]}</b>: <b>{temp[11]}</b>\nShamol: {shamol[10]}\n"
        kun3 = ertalab3 + "" + kunduz3

        ertalab4 = f"\n\n\n5️⃣\n<b>{kunlar_haftalik[4]}</b>\n\n{kun_qismlari[14]} {mosvaqtlar[14]}\n<b>{havo[14]}</b>: <b>{temp[14]}</b>\n"
        kunduz4 = f"{kun_qismlari[15]} {mosvaqtlar[15]}\n<b>{havo[15]}</b>: <b>{temp[15]}</b>\nShamol: {shamol[14]}\n"
        kun4 = ertalab4 + "" + kunduz4

        ertalab5 = f"\n\n\n6️⃣\n<b>{kunlar_haftalik[5]}</b>\n\n{kun_qismlari[18]} {mosvaqtlar[18]}\n<b>{havo[18]}</b>: <b>{temp[18]}</b>\n"
        kunduz5 = f"{kun_qismlari[19]} {mosvaqtlar[19]}\n<b>{havo[19]}</b>: <b>{temp[19]}</b>\nShamol: {shamol[18]}\n"
        kun5 = ertalab5 + "" + kunduz5

        ertalab6 = f"\n\n\n7️⃣\n<b>{kunlar_haftalik[6]}</b>\n\n{kun_qismlari[22]} {mosvaqtlar[22]}\n<b>{havo[22]}</b>: <b>{temp[22]}</b>\n"
        kunduz6 = f"{kun_qismlari[23]} {mosvaqtlar[23]}\n<b>{havo[23]}</b>: <b>{temp[23]}</b>\nShamol: {shamol[22]}\n"
        kun6 = ertalab6 + "" + kunduz6

        javob = kun0 + quyosh_oy0 + kun1 + quyosh_oy1 + kun2 + quyosh_oy2 + kun3 + quyosh_oy3 + kun4 + quyosh_oy4 + kun5 + quyosh_oy5 + kun6 + quyosh_oy6

    if len(kun_qismlari) == 26:
        ertalab0 = f"<b>{shahar}</b>\n\n\n1️⃣\n<b>{kunlar_haftalik[0]}\n</b>\n{kun_qismlari[0]} {mosvaqtlar[0]}\n<b>{havo[0]}</b>: <b>{temp[0]}</b>\nShamol: {shamol[0]}\n"
        kun0 = ertalab0

        ertalab1 = f"\n\n\n2️⃣\n<b>{kunlar_haftalik[1]}</b>\n\n{kun_qismlari[3]} {mosvaqtlar[3]}\n<b>{havo[3]}</b>: <b>{temp[3]}</b>\n"
        kunduz1 = f"{kun_qismlari[4]} {mosvaqtlar[4]}\n<b>{havo[4]}</b>: <b>{temp[4]}</b>\nShamol: {shamol[4]}\n"
        kun1 = ertalab1 + "" + kunduz1

        ertalab2 = f"\n\n\n3️⃣\n<b>{kunlar_haftalik[2]}</b>\n\n{kun_qismlari[7]} {mosvaqtlar[7]}\n<b>{havo[7]}</b>: <b>{temp[7]}</b>\n"
        kunduz2 = f"{kun_qismlari[8]} {mosvaqtlar[8]}\n<b>{havo[8]}</b>: <b>{temp[8]}</b>\nShamol: {shamol[8]}\n"
        kun2 = ertalab2 + "" + kunduz2

        ertalab3 = f"\n\n\n4️⃣\n<b>{kunlar_haftalik[3]}</b>\n\n{kun_qismlari[11]} {mosvaqtlar[11]}\n<b>{havo[11]}</b>: <b>{temp[11]}</b>\n"
        kunduz3 = f"{kun_qismlari[12]} {mosvaqtlar[12]}\n<b>{havo[12]}</b>: <b>{temp[12]}</b>\nShamol: {shamol[12]}\n"
        kun3 = ertalab3 + "" + kunduz3

        ertalab4 = f"\n\n\n5️⃣\n<b>{kunlar_haftalik[4]}</b>\n\n{kun_qismlari[15]} {mosvaqtlar[15]}\n<b>{havo[15]}</b>: <b>{temp[15]}</b>\n"
        kunduz4 = f"{kun_qismlari[16]} {mosvaqtlar[16]}\n<b>{havo[16]}</b>: <b>{temp[16]}</b>\nShamol: {shamol[16]}\n"
        kun4 = ertalab4 + "" + kunduz4

        ertalab5 = f"\n\n\n6️⃣\n<b>{kunlar_haftalik[5]}</b>\n\n{kun_qismlari[19]} {mosvaqtlar[19]}\n<b>{havo[19]}</b>: <b>{temp[19]}</b>\n"
        kunduz5 = f"{kun_qismlari[20]} {mosvaqtlar[20]}\n<b>{havo[20]}</b>: <b>{temp[20]}</b>\nShamol: {shamol[20]}\n"
        kun5 = ertalab5 + "" + kunduz5

        ertalab6 = f"\n\n\n7️⃣\n<b>{kunlar_haftalik[6]}</b>\n\n{kun_qismlari[23]} {mosvaqtlar[23]}\n<b>{havo[23]}</b>: <b>{temp[23]}</b>\n"
        kunduz6 = f"{kun_qismlari[24]} {mosvaqtlar[24]}\n<b>{havo[24]}</b>: <b>{temp[24]}</b>\nShamol: {shamol[24]}\n"
        kun6 = ertalab6 + "" + kunduz6

        javob = kun0 + quyosh_oy0 + kun1 + quyosh_oy1 + kun2 + quyosh_oy2 + kun3 + quyosh_oy3 + kun4 + quyosh_oy4 + kun5 + quyosh_oy5 + kun6 + quyosh_oy6

    if len(kun_qismlari) == 27:
        ertalab0 = f"<b>{shahar}</b>\n\n\n1️⃣\n<b>{kunlar_haftalik[0]}\n</b>\n{kun_qismlari[0]} {mosvaqtlar[0]}\n<b>{havo[0]}</b>: <b>{temp[0]}</b>\n"
        kunduz0 = f"{kun_qismlari[1]} {mosvaqtlar[1]}\n<b>{havo[1]}</b>: <b>{temp[1]}</b>\nShamol: {shamol[1]}\n"
        kun0 = ertalab0 + "" + kunduz0

        ertalab1 = f"\n\n\n2️⃣\n<b>{kunlar_haftalik[1]}</b>\n\n{kun_qismlari[4]} {mosvaqtlar[4]}\n<b>{havo[4]}</b>: <b>{temp[4]}</b>\n"
        kunduz1 = f"{kun_qismlari[5]} {mosvaqtlar[5]}\n<b>{havo[5]}</b>: <b>{temp[5]}</b>\nShamol: {shamol[5]}\n"
        kun1 = ertalab1 + "" + kunduz1

        ertalab2 = f"\n\n\n3️⃣\n<b>{kunlar_haftalik[2]}</b>\n\n{kun_qismlari[8]} {mosvaqtlar[8]}\n<b>{havo[8]}</b>: <b>{temp[8]}</b>\n"
        kunduz2 = f"{kun_qismlari[9]} {mosvaqtlar[9]}\n<b>{havo[9]}</b>: <b>{temp[9]}</b>\nShamol: {shamol[9]}\n"
        kun2 = ertalab2 + "" + kunduz2

        ertalab3 = f"\n\n\n4️⃣\n<b>{kunlar_haftalik[3]}</b>\n\n{kun_qismlari[12]} {mosvaqtlar[12]}\n<b>{havo[12]}</b>: <b>{temp[12]}</b>\n"
        kunduz3 = f"{kun_qismlari[13]} {mosvaqtlar[13]}\n<b>{havo[13]}</b>: <b>{temp[13]}</b>\nShamol: {shamol[13]}\n"
        kun3 = ertalab3 + "" + kunduz3

        ertalab4 = f"\n\n\n5️⃣\n<b>{kunlar_haftalik[4]}</b>\n\n{kun_qismlari[16]} {mosvaqtlar[16]}\n<b>{havo[16]}</b>: <b>{temp[16]}</b>\n"
        kunduz4 = f"{kun_qismlari[17]} {mosvaqtlar[17]}\n<b>{havo[17]}</b>: <b>{temp[17]}</b>\nShamol: {shamol[17]}\n"
        kun4 = ertalab4 + "" + kunduz4

        ertalab5 = f"\n\n\n6️⃣\n<b>{kunlar_haftalik[5]}</b>\n\n{kun_qismlari[20]} {mosvaqtlar[20]}\n<b>{havo[20]}</b>: <b>{temp[20]}</b>\n"
        kunduz5 = f"{kun_qismlari[21]} {mosvaqtlar[21]}\n<b>{havo[21]}</b>: <b>{temp[21]}</b>\nShamol: {shamol[21]}\n"
        kun5 = ertalab5 + "" + kunduz5

        ertalab6 = f"\n\n\n7️⃣\n<b>{kunlar_haftalik[6]}</b>\n\n{kun_qismlari[24]} {mosvaqtlar[24]}\n<b>{havo[24]}</b>: <b>{temp[24]}</b>\n"
        kunduz6 = f"{kun_qismlari[25]} {mosvaqtlar[25]}\n<b>{havo[25]}</b>: <b>{temp[25]}</b>\nShamol: {shamol[25]}\n"
        kun6 = ertalab6 + "" + kunduz6

        javob = kun0 + quyosh_oy0 + kun1 + quyosh_oy1 + kun2 + quyosh_oy2 + kun3 + quyosh_oy3 + kun4 + quyosh_oy4 + kun5 + quyosh_oy5 + kun6 + quyosh_oy6

    if len(kun_qismlari) == 28:
        ertalab0 = f"<b>{shahar}</b>\n\n\n1️⃣\n<b>{kunlar_haftalik[0]}\n</b>\n\n{kun_qismlari[1]} {mosvaqtlar[1]}\n<b>{havo[1]}</b>: <b>{temp[1]}</b>\n"
        kunduz0 = f"{kun_qismlari[2]} {mosvaqtlar[2]}\n<b>{havo[2]}</b>: <b>{temp[2]}</b>\nShamol: {shamol[2]}\n"
        kun0 = ertalab0 + "" + kunduz0

        ertalab1 = f"\n\n\n2️⃣\n<b>{kunlar_haftalik[1]}</b>\n\n{kun_qismlari[5]} {mosvaqtlar[5]}\n<b>{havo[5]}</b>: <b>{temp[5]}</b>\n"
        kunduz1 = f"{kun_qismlari[6]} {mosvaqtlar[6]}\n<b>{havo[6]}</b>: <b>{temp[6]}</b>\nShamol: {shamol[6]}\n"
        kun1 = ertalab1 + "" + kunduz1

        ertalab2 = f"\n\n\n3️⃣\n<b>{kunlar_haftalik[2]}</b>\n\n{kun_qismlari[9]} {mosvaqtlar[9]}\n<b>{havo[9]}</b>: <b>{temp[9]}</b>\n"
        kunduz2 = f"{kun_qismlari[10]} {mosvaqtlar[10]}\n<b>{havo[10]}</b>: <b>{temp[10]}</b>\nShamol: {shamol[10]}\n"
        kun2 = ertalab2 + "" + kunduz2

        ertalab3 = f"\n\n\n4️⃣\n<b>{kunlar_haftalik[3]}</b>\n\n{kun_qismlari[13]} {mosvaqtlar[13]}\n<b>{havo[13]}</b>: <b>{temp[13]}</b>\n"
        kunduz3 = f"{kun_qismlari[14]} {mosvaqtlar[14]}\n<b>{havo[14]}</b>: <b>{temp[14]}</b>\nShamol: {shamol[14]}\n"
        kun3 = ertalab3 + "" + kunduz3

        ertalab4 = f"\n\n\n5️⃣\n<b>{kunlar_haftalik[4]}</b>\n\n{kun_qismlari[17]} {mosvaqtlar[17]}\n<b>{havo[17]}</b>: <b>{temp[17]}</b>\n"
        kunduz4 = f"{kun_qismlari[18]} {mosvaqtlar[18]}\n<b>{havo[18]}</b>: <b>{temp[18]}</b>\nShamol: {shamol[18]}\n"
        kun4 = ertalab4 + "" + kunduz4

        ertalab5 = f"\n\n\n6️⃣\n<b>{kunlar_haftalik[5]}</b>\n\n{kun_qismlari[21]} {mosvaqtlar[21]}\n<b>{havo[21]}</b>: <b>{temp[21]}</b>\n"
        kunduz5 = f"{kun_qismlari[22]} {mosvaqtlar[22]}\n<b>{havo[22]}</b>: <b>{temp[22]}</b>\nShamol: {shamol[22]}\n"
        kun5 = ertalab5 + "" + kunduz5

        ertalab6 = f"\n\n\n7️⃣\n<b>{kunlar_haftalik[6]}</b>\n\n{kun_qismlari[25]} {mosvaqtlar[25]}\n<b>{havo[25]}</b>: <b>{temp[25]}</b>\n"
        kunduz6 = f"{kun_qismlari[26]} {mosvaqtlar[26]}\n<b>{havo[26]}</b>: <b>{temp[26]}</b>\nShamol: {shamol[26]}\n"
        kun6 = ertalab6 + "" + kunduz6

        javob = kun0 + quyosh_oy0 + kun1 + quyosh_oy1 + kun2 + quyosh_oy2 + kun3 + quyosh_oy3 + kun4 + quyosh_oy4 + kun5 + quyosh_oy5 + kun6 + quyosh_oy6

    return javob
