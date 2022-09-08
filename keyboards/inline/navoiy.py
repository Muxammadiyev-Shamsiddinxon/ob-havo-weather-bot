from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

navoiy_tumanlari = InlineKeyboardMarkup (

    inline_keyboard=[
    [
            InlineKeyboardButton(text="Navoiy", callback_data="Navoiyshahri"),
            InlineKeyboardButton(text="Zarafshon", callback_data="Zarafshon"),
    ],

    [
        InlineKeyboardButton(text="Karmana", callback_data="Karmana"),
        InlineKeyboardButton(text="Konimex", callback_data="Konimex")

    ],
    [
        InlineKeyboardButton(text="Navbahor", callback_data="Navbahor"),
        InlineKeyboardButton(text="Nurota", callback_data="Nurota")
    ],
    [
        InlineKeyboardButton(text="Qiziltepa",  callback_data="Qiziltepa"),
        InlineKeyboardButton(text="Tomdi", callback_data="Tomdi")
    ],
    [
        InlineKeyboardButton(text="Uchquduq", callback_data="Uchquduq"),
        InlineKeyboardButton(text="Xatirchi", callback_data="Xatirchi")

    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="🔙Ortga"),
    ],
    [
        InlineKeyboardButton(text="📤 Ulashish", switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Navoiymenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Navoiy Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Navoiy Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Navoiydan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Navoiydan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Zarafshonmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Zarafshon Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Zarafshon Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Zarafshondan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Zarafshondan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Karmanamenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Karmana Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Karmana Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Karmanadan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Karmanadan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )

Konimexmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Konimex Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Konimex Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Konimexdan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Konimexdan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Navbahormenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Navbahor Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Navbahor Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Navbahordan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Navbahordan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Nurotamenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Nurota Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Nurota Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Nurotadan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Nurotadan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Qiziltepamenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Qiziltepa Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Qiziltepa Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Qiziltepadan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Qiziltepadan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Tomdimenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Tomdi Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Tomdi Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Tomdidan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Tomdidan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )

Uchquduqmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Uchquduq Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Uchquduq Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Uchquduqdan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Uchquduqdan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Xatirchimenu = InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Xatirchi Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Xatirchi Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Xatirchidan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Xatirchidan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )
