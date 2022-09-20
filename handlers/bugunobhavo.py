# import requests
# from bs4 import BeautifulSoup
# import  re
# sonlar = "[0-9]+.?[0-9]*"


def bugun_obhavo(url):

    # headers = {
    #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    #     "referer": "https://www.google.com/"
    # }
    #
    #
    # site = requests.get(url=url, headers=headers)
    # htmldom = BeautifulSoup(site.text, "lxml")
    #
    #
    # hudud = htmldom.find("h1").text.strip()

    # kun = htmldom.find("div", class_="content-module subnav-pagination").text.strip()
    # bugun = f"Bugun {kun}."  # javob
    #
    # hozir_temp = htmldom.find("div", class_="display-temp").text.strip()
    # hozir_havo = htmldom.find("div", class_="phrase").text.strip()
    # temp = f"{hozir_havo} havo {hozir_temp}  \n"  # javob
    #
    # umumiy_temp = htmldom.findAll("div", class_="row first")[0].text
    # umumiy_temp = re.findall(sonlar, umumiy_temp)
    # max_temp = umumiy_temp[0]
    # min_temp = umumiy_temp[1]
    #
    # max_min = f"🌡Yuqori temperatura --> {max_temp}C\n🌡Past temperatura -----> {min_temp}C"  # javob
    #
    # umumiy = htmldom.find("div", class_="left").text.strip()
    # umumiy1 = re.findall(sonlar, umumiy)
    # if len(umumiy1) == 5:
    #     shamol = f"🌬Shamol -------------------> {re.findall(sonlar, umumiy)[1]}km/soat"
    #     namlik = f"💧Namlik -------------------> {re.findall(sonlar, umumiy)[3]} "
    # else:
    #     shamol = f"🌬Shamol -----------------> {re.findall(sonlar, umumiy)[0]}km/soat"
    #     namlik = f"💧Namlik ------------------> {re.findall(sonlar, umumiy)[2]} "
    # shamol_namlik = f"<b>{shamol} \n{namlik}</b>"  # javob
    #
    # umumiy2 = htmldom.find("div", class_="right").text.strip()
    # bosim = f"⛈Bosim -------------------> ↓ {re.findall(sonlar, umumiy2)[0]}mb"
    # tuman = f"☁️Tumanli -----------------> {re.findall(sonlar, umumiy2)[1]}"
    # bulut = f"\nEng pastgi bulut {re.findall(sonlar, umumiy2)[3]}metr masofada"
    # b_t_b = f"<b>{bosim}\n{tuman}\n{bulut}</b>"  # javob
    #
    # quyosh1 = htmldom.findAll("span", class_="text-value")[0].text.strip()
    # quyosh2 = htmldom.findAll("span", class_="text-value")[1].text.strip()
    # quyosh = f"🌤 Quyosh chiqishi ___{quyosh1}___\n🌥 Quyosh botishi ___{quyosh2}___"  # javob
    #
    # javob = f"<b>{hudud}\n\n{bugun}\n{temp}\n{max_min}\n{shamol_namlik}\n{b_t_b}\n\n\n{quyosh}</b>"
    javob = f"Assalom Alaykum hurmatli <b>foydalanuvchi</b>.\nBu bo'lim ham yaqinda ishga tushadi.\n\nMurojat uchun Dasturchi:\n<b>Shamsiddin_xon.</b>\nlink 👉  @Hacker_Attacks1"
    return javob