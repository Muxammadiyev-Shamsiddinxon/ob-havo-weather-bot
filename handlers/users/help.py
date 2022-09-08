from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.Viloyatlar_menu import viloyatlarmenu
from loader import dp



@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Botdan foydalanish uchun /start tugmasini bosing"
    await message.answer(text)



#   Maydon tavsiflari:
#   lat:Kenglik (daraja).
#   lon:Uzunlik (daraja).
#   timezone:Mahalliy IANA vaqt zonasi.
#   city_name:Shahar nomi.
#   city_id:Shahar identifikatori.
#   station_id:[QO'SHILGAN] Eng yaqin stantsiya.
#   country_code:Mamlakat qisqartmasi.
#   state_code:Davlat qisqartmasi/kodi.
#   sources:Javob sifatida foydalanilgan ma'lumotlar manbalari ro'yxati.
#   data: [
#   datetime:Sana (YYYY-AA-DD).
#   ts:Vaqt tamg'asi UTC (Unix vaqt tamg'asi).
#   pres:O'rtacha bosim (mb).
#   slp:Dengiz sathining o'rtacha bosimi (mb).
#   wind_spd:Shamolning o'rtacha tezligi (Standart m/s).
#   wind_gust_spd:Shamol tezligi (m/s).
#   max_wind_spd:Maksimal 2 minutlik shamol tezligi (m/s).
#   wind_dir:O'rtacha shamol yo'nalishi (daraja).
#   max_wind_dir:Maksimal 2 daqiqalik shamolning yo'nalishi (daraja).
#   max_wind_ts:Shamolning maksimal tezligi vaqti UTC (Unix Timestamp).
#   temp:O'rtacha harorat (standart Selsiy).
#   max_temp:Maksimal harorat (standart Selsiy).
#   min_temp:Minimal harorat (standart Selsiy).
#   max_temp_ts:Kunlik maksimal harorat vaqti UTC (Unix Timestamp).
#   min_temp_ts:Kunlik minimal harorat vaqti UTC (Unix Timestamp).
#   rh:O'rtacha nisbiy namlik (%).
#   dewpt:O'rtacha shudring nuqtasi (standart Selsiy).
#   clouds: [Sun'iy yo'ldoshga asoslangan] o'rtacha bulut qoplami (%).
#   precip:Yig'ilgan yog'ingarchilik (standart mm).
#   precip_gpm:Yig'ilgan yog'ingarchilik [sun'iy yo'ldosh/radar hisobi] (standart mm).
#   snow:Yig'ilgan qor yog'ishi (standart mm).
#   snow_depth:Qor chuqurligi (standart mm).
#   solar_rad:Oʻrtacha quyosh nurlanishi (Vt/M^2)
#   t_solar_rad:Umumiy quyosh nurlanishi (Vt/M^2)
#   ghi:Oʻrtacha global gorizontal quyosh nurlanishi (Vt/m^2).
#   t_ghi:Kundalik umumiy gorizontal quyosh nurlanishi (Vt/m^2) [Osmon musaffoligi]
#   max_ghi:Kundalik global gorizontal quyosh nurlanishining maksimal qiymati (Vt/m^2) [Clear Sky]
#   dni:Oʻrtacha toʻgʻridan-toʻgʻri normal quyosh nurlanishi (Vt/m^2) [Clear Sky]
#   t_dni:Kundalik toʻgʻridan-toʻgʻri normal quyosh nurlanishi (Vt/m^2) [Osmon musaffoligi]
#   max_dni:Kunda to'g'ridan-to'g'ri normal quyosh nurlanishining maksimal qiymati (Vt/m^2) [Clear Sky]
#   dhi:Oʻrtacha diffuz gorizontal quyosh nurlanishi (Vt/m^2) [Osmon musaffoligi]
#   t_dhi:Kunlik umumiy diffuz gorizontal quyosh nurlanishi (Vt/m^2) [Osmon musaffoligi]
#   max_dhi:Kunda diffuz gorizontal quyosh nurlanishining maksimal qiymati (Vt/m^2) [Osmon musaffoligi]
#   max_uv:Maksimal UV indeksi (0-11+)
#
#
#     birliklar = [birliklar](ixtiyoriy) M - [DEFAULT]

#     Metrik(Selsiy, m / s, mm)
#     S - Ilmiy(Kelvin, m / s, mm)
#     I - Farengeyt(F, milya, dyuym)

#     soat = [integer](ixtiyoriy: prognoz soatlarining aniq sonini qaytaring)
#     1 - 240 hours - [DEFULT] 48 soat