import requests
from bs4 import BeautifulSoup
from PIL import Image,  ImageDraw, ImageFont

def haftalik_obhavo(url,id):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "referer": "https://www.google.com/"
    }

    site = requests.get(url=url, headers=headers)
    htmldom = BeautifulSoup(site.text, "lxml")


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

    # quyosh_oy0 = f"Quyosh\n({quyosh[0]},{quyosh[1]})\nOy\n({oy[0]},{oy[1]})"
    quyosh_oy1 = f"Quyosh\n({quyosh[2]},{quyosh[3]})\nOy\n({oy[2]},{oy[3]})"
    quyosh_oy2 = f"Quyosh\n({quyosh[4]},{quyosh[5]})\nOy\n({oy[4]},{oy[5]})"
    quyosh_oy3 = f"Quyosh\n({quyosh[6]},{quyosh[7]})\nOy\n({oy[6]},{oy[7]})"
    quyosh_oy4 = f"Quyosh\n({quyosh[8]},{quyosh[9]})\nOy\n({oy[8]},{oy[9]})"
    quyosh_oy5 = f"Quyosh\n({quyosh[10]},{quyosh[11]})\nOy\n({oy[10]},{oy[11]})"
    quyosh_oy6 = f"Quyosh\n({quyosh[12]},{quyosh[13]})\nOy\n({oy[12]},{oy[13]})"

    if len(kun_qismlari) == 25:

        image = Image.open('rasmlar/foto.jpg')

        draw = ImageDraw.Draw(image)
        haftaliklar = ImageFont.truetype("rasmlar/arial2.TTF", 23)
        draw.text((230, 4), id, font=haftaliklar, fill=(255, 255, 255)) # bu callback data <Misol Nukus Haftalik tugamasi> yoki boshqa tugma.

        kunlar = ImageFont.truetype(("rasmlar/arial2.TTF"), 18)
        draw.text((70, 41), kunlar_haftalik[1], font=kunlar, fill=(255, 255, 0))  #  haftaning kunlari
        draw.text((70, 169), kunlar_haftalik[2], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 296), kunlar_haftalik[3], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 421), kunlar_haftalik[4], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 550), kunlar_haftalik[5], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 669), kunlar_haftalik[6], font=kunlar, fill=(255, 255, 0))


        kun_qism = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((35, 70), f"{kun_qismlari[2].title()}", font=kun_qism, fill=(255,255,255))   #  kunning qismlari yani ertalab kunduzi kechga
        draw.text((35, 100), f"{kun_qismlari[3].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 200), f"{kun_qismlari[6].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 230), f"{kun_qismlari[7].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 327), f"{kun_qismlari[10].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 357), f"{kun_qismlari[11].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 455), f"{kun_qismlari[14].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 485), f"{kun_qismlari[15].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 576), f"{kun_qismlari[18].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 606), f"{kun_qismlari[19].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 704), f"{kun_qismlari[22].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 735), f"{kun_qismlari[23].title()}", font=kun_qism, fill=(255,255,255))


        quyosh_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((425, 71), f"{quyosh_oy1}", font=quyosh_razmer, fill=(255,255,255))  #   quyosh va oy
        draw.text((425, 200), f"{quyosh_oy2}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 327), f"{quyosh_oy3}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 452), f"{quyosh_oy4}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 576), f"{quyosh_oy5}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 703), f"{quyosh_oy6}", font=quyosh_razmer, fill=(255,255,255))



        draw.text((35, 85), f"{havo[2]} {temp[2]}", font=kun_qism, fill=(255, 255, 255))  # havo va temperatura
        draw.text((35, 115), f"{havo[3]} {temp[3]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 215), f"{havo[6]} {temp[6]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 245), f"{havo[7]} {temp[7]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 342), f"{havo[10]} {temp[10]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 372), f"{havo[11]} {temp[11]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 470), f"{havo[14]} {temp[14]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 497), f"{havo[15]} {temp[15]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 592), f"{havo[18]} {temp[18]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 622), f"{havo[19]} {temp[19]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 721), f"{havo[22]} {temp[22]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 751), f"{havo[23]} {temp[23]}", font=kun_qism, fill=(255, 255, 255))


        shamol_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)
        draw.text((90, 140), f"Shamol {shamol[2]}", font=shamol_razmer, fill=(255, 255, 255))  #   shamol tezligi
        draw.text((90, 270), f"Shamol {shamol[6]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 395), f"Shamol {shamol[10]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 517), f"Shamol {shamol[14]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 640), f"Shamol {shamol[18]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 775), f"Shamol {shamol[22]}", font=shamol_razmer, fill=(255, 255, 255))

        image.save(f'rasmlar/{id}.jpg')

    if len(kun_qismlari) == 26:

        image = Image.open('rasmlar/foto.jpg')

        draw = ImageDraw.Draw(image)
        haftaliklar = ImageFont.truetype("rasmlar/arial2.TTF", 23)
        draw.text((230, 4), id, font=haftaliklar, fill=(255, 255, 255)) # bu callback data <Misol Nukus Haftalik tugamasi> yoki boshqa tugma.

        kunlar = ImageFont.truetype(("rasmlar/arial2.TTF"), 18)
        draw.text((70, 41), kunlar_haftalik[1], font=kunlar, fill=(255, 255, 0))  #  haftaning kunlari
        draw.text((70, 169), kunlar_haftalik[2], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 296), kunlar_haftalik[3], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 421), kunlar_haftalik[4], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 550), kunlar_haftalik[5], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 669), kunlar_haftalik[6], font=kunlar, fill=(255, 255, 0))


        kun_qism = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((35, 70), f"{kun_qismlari[3].title()}", font=kun_qism, fill=(255,255,255))   #  kunning qismlari yani ertalab kunduzi kechga
        draw.text((35, 100), f"{kun_qismlari[4].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 200), f"{kun_qismlari[7].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 230), f"{kun_qismlari[8].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 327), f"{kun_qismlari[11].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 357), f"{kun_qismlari[12].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 455), f"{kun_qismlari[15].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 485), f"{kun_qismlari[16].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 576), f"{kun_qismlari[19].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 606), f"{kun_qismlari[20].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 704), f"{kun_qismlari[23].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 735), f"{kun_qismlari[24].title()}", font=kun_qism, fill=(255,255,255))


        quyosh_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((425, 71), f"{quyosh_oy1}", font=quyosh_razmer, fill=(255,255,255))  #   quyosh va oy
        draw.text((425, 200), f"{quyosh_oy2}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 327), f"{quyosh_oy3}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 452), f"{quyosh_oy4}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 576), f"{quyosh_oy5}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 703), f"{quyosh_oy6}", font=quyosh_razmer, fill=(255,255,255))



        draw.text((35, 85), f"{havo[3]} {temp[3]}", font=kun_qism, fill=(255, 255, 255))  # havo va temperatura
        draw.text((35, 115), f"{havo[4]} {temp[4]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 215), f"{havo[7]} {temp[7]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 245), f"{havo[8]} {temp[8]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 342), f"{havo[11]} {temp[11]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 372), f"{havo[12]} {temp[12]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 470), f"{havo[15]} {temp[15]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 497), f"{havo[16]} {temp[16]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 592), f"{havo[19]} {temp[19]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 622), f"{havo[20]} {temp[20]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 721), f"{havo[23]} {temp[23]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 751), f"{havo[24]} {temp[24]}", font=kun_qism, fill=(255, 255, 255))


        shamol_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)
        draw.text((90, 140), f"Shamol {shamol[4]}", font=shamol_razmer, fill=(255, 255, 255))  #   shamol tezligi
        draw.text((90, 270), f"Shamol {shamol[8]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 395), f"Shamol {shamol[12]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 517), f"Shamol {shamol[16]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 640), f"Shamol {shamol[20]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 775), f"Shamol {shamol[24]}", font=shamol_razmer, fill=(255, 255, 255))

        image.save(f'rasmlar/{id}.jpg')

    if len(kun_qismlari) == 27:

        image = Image.open('rasmlar/foto.jpg')

        draw = ImageDraw.Draw(image)
        haftaliklar = ImageFont.truetype("rasmlar/arial2.TTF", 23)
        draw.text((230, 4), id, font=haftaliklar, fill=(255, 255, 255)) # bu callback data <Misol Nukus Haftalik tugamasi> yoki boshqa tugma.

        kunlar = ImageFont.truetype(("rasmlar/arial2.TTF"), 18)
        draw.text((70, 41), kunlar_haftalik[1], font=kunlar, fill=(255, 255, 0))  #  haftaning kunlari
        draw.text((70, 169), kunlar_haftalik[2], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 296), kunlar_haftalik[3], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 421), kunlar_haftalik[4], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 550), kunlar_haftalik[5], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 669), kunlar_haftalik[6], font=kunlar, fill=(255, 255, 0))


        kun_qism = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((35, 70), f"{kun_qismlari[4].title()}", font=kun_qism, fill=(255,255,255))   #  kunning qismlari yani ertalab kunduzi kechga
        draw.text((35, 100), f"{kun_qismlari[5].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 200), f"{kun_qismlari[8].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 230), f"{kun_qismlari[9].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 327), f"{kun_qismlari[12].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 357), f"{kun_qismlari[13].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 455), f"{kun_qismlari[16].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 485), f"{kun_qismlari[17].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 576), f"{kun_qismlari[20].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 606), f"{kun_qismlari[21].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 704), f"{kun_qismlari[24].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 735), f"{kun_qismlari[25].title()}", font=kun_qism, fill=(255,255,255))


        quyosh_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((425, 71), f"{quyosh_oy1}", font=quyosh_razmer, fill=(255,255,255))  #   quyosh va oy
        draw.text((425, 200), f"{quyosh_oy2}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 327), f"{quyosh_oy3}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 452), f"{quyosh_oy4}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 576), f"{quyosh_oy5}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 703), f"{quyosh_oy6}", font=quyosh_razmer, fill=(255,255,255))



        draw.text((35, 85), f"{havo[4]} {temp[4]}", font=kun_qism, fill=(255, 255, 255))  # havo va temperatura
        draw.text((35, 115), f"{havo[5]} {temp[5]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 215), f"{havo[8]} {temp[8]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 245), f"{havo[9]} {temp[9]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 342), f"{havo[12]} {temp[12]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 372), f"{havo[13]} {temp[13]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 470), f"{havo[16]} {temp[16]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 497), f"{havo[17]} {temp[17]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 592), f"{havo[20]} {temp[20]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 622), f"{havo[21]} {temp[21]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 721), f"{havo[24]} {temp[24]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 751), f"{havo[25]} {temp[25]}", font=kun_qism, fill=(255, 255, 255))


        shamol_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)
        draw.text((90, 140), f"Shamol {shamol[5]}", font=shamol_razmer, fill=(255, 255, 255))  #   shamol tezligi
        draw.text((90, 270), f"Shamol {shamol[9]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 395), f"Shamol {shamol[13]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 517), f"Shamol {shamol[17]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 640), f"Shamol {shamol[21]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 775), f"Shamol {shamol[25]}", font=shamol_razmer, fill=(255, 255, 255))

        image.save(f'rasmlar/{id}.jpg')

    if len(kun_qismlari) == 28:

        image = Image.open('rasmlar/foto.jpg')

        draw = ImageDraw.Draw(image)
        haftaliklar = ImageFont.truetype("rasmlar/arial2.TTF", 23)
        draw.text((230, 4), id, font=haftaliklar, fill=(255, 255, 255)) # bu callback data <Misol Nukus Haftalik tugamasi> yoki boshqa tugma.

        kunlar = ImageFont.truetype(("rasmlar/arial2.TTF"), 18)
        draw.text((70, 41), kunlar_haftalik[1], font=kunlar, fill=(255, 255, 0))  #  haftaning kunlari
        draw.text((70, 169), kunlar_haftalik[2], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 296), kunlar_haftalik[3], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 421), kunlar_haftalik[4], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 550), kunlar_haftalik[5], font=kunlar, fill=(255, 255, 0))
        draw.text((70, 669), kunlar_haftalik[6], font=kunlar, fill=(255, 255, 0))


        kun_qism = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((35, 70), f"{kun_qismlari[5].title()}", font=kun_qism, fill=(255,255,255))   #  kunning qismlari yani ertalab kunduzi kechga
        draw.text((35, 100), f"{kun_qismlari[6].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 200), f"{kun_qismlari[9].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 230), f"{kun_qismlari[10].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 327), f"{kun_qismlari[13].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 357), f"{kun_qismlari[14].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 455), f"{kun_qismlari[17].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 485), f"{kun_qismlari[18].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 576), f"{kun_qismlari[21].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 606), f"{kun_qismlari[22].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 704), f"{kun_qismlari[25].title()}", font=kun_qism, fill=(255,255,255))
        draw.text((35, 735), f"{kun_qismlari[26].title()}", font=kun_qism, fill=(255,255,255))


        quyosh_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)

        draw.text((425, 71), f"{quyosh_oy1}", font=quyosh_razmer, fill=(255,255,255))  #   quyosh va oy
        draw.text((425, 200), f"{quyosh_oy2}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 327), f"{quyosh_oy3}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 452), f"{quyosh_oy4}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 576), f"{quyosh_oy5}", font=quyosh_razmer, fill=(255,255,255))
        draw.text((425, 703), f"{quyosh_oy6}", font=quyosh_razmer, fill=(255,255,255))



        draw.text((35, 85), f"{havo[5]} {temp[5]}", font=kun_qism, fill=(255, 255, 255))  # havo va temperatura
        draw.text((35, 115), f"{havo[6]} {temp[6]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 215), f"{havo[9]} {temp[9]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 245), f"{havo[10]} {temp[10]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 342), f"{havo[13]} {temp[13]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 372), f"{havo[14]} {temp[14]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 470), f"{havo[17]} {temp[17]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 497), f"{havo[18]} {temp[18]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 592), f"{havo[21]} {temp[21]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 622), f"{havo[22]} {temp[22]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 721), f"{havo[25]} {temp[25]}", font=kun_qism, fill=(255, 255, 255))
        draw.text((35, 751), f"{havo[26]} {temp[26]}", font=kun_qism, fill=(255, 255, 255))


        shamol_razmer = ImageFont.truetype(("rasmlar/arial2.TTF"), 15)
        draw.text((90, 140), f"Shamol {shamol[6]}", font=shamol_razmer, fill=(255, 255, 255))  #   shamol tezligi
        draw.text((90, 270), f"Shamol {shamol[10]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 395), f"Shamol {shamol[14]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 517), f"Shamol {shamol[18]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 640), f"Shamol {shamol[22]}", font=shamol_razmer, fill=(255, 255, 255))
        draw.text((90, 775), f"Shamol {shamol[26]}", font=shamol_razmer, fill=(255, 255, 255))

        image.save(f'rasmlar/{id}.jpg')

