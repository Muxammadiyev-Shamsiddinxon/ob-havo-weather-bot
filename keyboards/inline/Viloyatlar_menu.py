from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

viloyatlarmenu = InlineKeyboardMarkup (

    inline_keyboard=[  
    [
        InlineKeyboardButton(text="Qoraqalpog'iston", callback_data="Qoraqalpogiston")
    ],
    [
        InlineKeyboardButton(text="Toshkent",  callback_data="Toshkent"),
        InlineKeyboardButton(text="Surxondaryo", callback_data="Surxondaryo")
    ],
    [
        InlineKeyboardButton(text="Andijon", callback_data="Andijon"),
        InlineKeyboardButton(text="Buxoro", callback_data="Buxoro")

    ],
    [
        InlineKeyboardButton(text="Farg'ona", callback_data="Fargona"),
        InlineKeyboardButton(text="Jizzax",  callback_data="Jizzax")
    ],
    [
        InlineKeyboardButton(text="Xorazm", callback_data="Xorazm"),
        InlineKeyboardButton(text="Namangan", callback_data="Namangan")
    ],
    [
        InlineKeyboardButton(text="Navoiy",callback_data="Navoiy"),
        InlineKeyboardButton(text="Qashqadaryo", callback_data="Qashqadaryo")
    ],
    [
        InlineKeyboardButton(text="Samarqand", callback_data="Samarqand"),
        InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryo")
    ],
    [
        InlineKeyboardButton(text="📤 Ulashish", switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )
