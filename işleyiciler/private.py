from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/7016b36478a0b3680a0cc.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\nᴄʀᴇᴀᴛᴏʀ🇦🇿  [ᴜ̈ʟᴠɪ ʜᴜ̈sᴇʏɴᴏᴠ](https://t.me/BrendUIvi)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴍᴇɴɪ ǫʀᴜᴘᴀ ᴇʟᴀᴠᴇ ᴇᴛ ❱ ➕", url=f"https://t.me/JasmineMusicXBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ᴀsɪsᴛᴀɴ", url="https://t.me/JasmineAsistan"
                    ),
                    InlineKeyboardButton(
                        "📚  sᴜᴘᴘᴏʀᴛ", url="https://t.me/JasmineSup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 ᴇᴍʀʟᴇʀ" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📚 ᴋᴀɴᴀʟ", url=f"https://t.me/Alay57Chat"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\n Botun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 ɪsᴛɪғᴀᴅᴇᴄɪ ᴇᴍʀʟᴇʀɪ", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ ᴀᴅᴍɪɴ ʀᴍʀʟᴇʀɪ", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "ɢᴇʀɪ 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "ᴄʀᴇᴀᴛᴏʀ🇦🇿", url="https://t.me/Jasmine0wner")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️\n- Mesaj silmə yetkisi.\n- Bağlantı ilə dəvət etmə yetkisi.\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨ ʜᴇʀ ᴋᴇs ᴜᴄᴜɴ ᴇᴍʀʟᴇʀ", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑 ᴀᴅᴍɪɴ ᴇᴍʀʟᴇʀɪ",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 ɢᴇʀɪ", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "ᴄʀᴇᴀᴛᴏʀ🇦🇿", url="https://t.me/Jasmine0wner")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nBu botun hərkəs üçün əmr menyusu . 
    » /vplay =>  İstədiyiniz Videoları Sürətli Bir Şəkildə Axtarın. \n» /song => İstədiyiniz Musiqi Sürətli Bir Şəkildə Axtarın. \n» /play => Musiqi Oxutmaq Üçün Youtube Url'sinə Və Ya Musiqi Dosyasına Yanıt Verin. """,
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "ᴄʀᴇᴀᴛᴏʀ🇦🇿", url="https://t.me/Jasmine0wner")
                 ],
                 [
                     InlineKeyboardButton(
                         "🔄 ɢᴇʀɪ", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n 🔄 /skip - Sıraya alınmış musiqiyə keç\n ⏹ /end - Musiqi oxumanı dayandır\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "ᴄʀᴇᴀᴛᴏʀ🇦🇿", url="https://t.me/Jasmine0wner")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 ɢᴇʀɪ", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nᴄʀᴇᴀᴛᴏʀ🇦🇿  [ᴜ̈ʟᴠɪ ʜᴜ̈sᴇʏɴᴏᴠ](https://t.me/BrendUIvi)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴍᴇɴɪ ǫʀᴜᴘᴀ ᴇʟᴀᴠᴇ ᴇʀ ❱ ➕", url=f"https://t.me/JasmineMusicXBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ᴀsɪsᴛᴀɴ", url="https://t.me/JasmineAsistan"
                    ),
                    InlineKeyboardButton(
                        "📚 sᴜᴘᴘᴏʀᴛ", url="https://t.me/JasmineSup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 ᴇᴍʀʟᴇʀ" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📚 ᴋᴀɴᴀʟ", url=f"https://t.me/Alay57Chat"
                    )
                ]
                
           ]
        ),
    )
