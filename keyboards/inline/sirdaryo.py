from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sirdaryo_tumanlari = InlineKeyboardMarkup (

    inline_keyboard=[
    [
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryoshahri"),
            InlineKeyboardButton(text="Boyovut", callback_data="Boyovut"),
    ],

    [
        InlineKeyboardButton(text="Guliston", callback_data="Guliston"),
        InlineKeyboardButton(text="Oqoltin", callback_data="Oqoltin")

    ],
    [
        InlineKeyboardButton(text="Sardoba", callback_data="Sardoba"),
        InlineKeyboardButton(text="Sayxunobod", callback_data="Sayxunobod")
    ],
    [
        InlineKeyboardButton(text="Xavos",  callback_data="Xavos"),
        InlineKeyboardButton(text="Yangiyer", callback_data="Yangiyer")
    ],

    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="🔙Ortga"),
    ],
    [
        InlineKeyboardButton(text="📤 Ulashish", switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Sirdaryomenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Sirdaryo Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Sirdaryo Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Sirdaryodan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Sirdaryodan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Boyovutmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Boyovut Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Boyovut Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Boyovutdan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Boyovutdan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Gulistonmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Guliston Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Guliston Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Gulistondan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Gulistondan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )

Oqoltinmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Oqoltin Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Oqoltin Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Oqoltindan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Oqoltindan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Sardobamenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Sardoba Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Sardoba Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Sardobadan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Sardobadan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Sayxunobodmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Sayxunobod Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Sayxunobod Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Sayxunoboddan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Sayxunoboddan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )


Xavosmenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Xavos Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Xavos Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Xavosdan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Xavosdan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )



Yangiyermenu= InlineKeyboardMarkup (

    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bugun ob havo", callback_data="Yangiyer Bugun"),
        InlineKeyboardButton(text="Haftalik", callback_data="Yangiyer Haftalik"),
    ],
    [
        InlineKeyboardButton(text="🔙Ortga", callback_data="Yangiyerdan tumanlarga qayt"),
        InlineKeyboardButton(text="🏠Menu", callback_data="Yangiyerdan viloyatlarga qayt")

    ],
    [
        InlineKeyboardButton(text="📤 Ulashish",switch_inline_query="ob-havo bot 🌤🌤 ")
    ]

] )

