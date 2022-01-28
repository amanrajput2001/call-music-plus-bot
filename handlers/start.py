import os

from pyrogram import Client, filters # Ik this is weird as this shit is already imported in line 6! anyway ... Fuck Off!
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2
from helpers.database import db, Database
from helpers.dbthings import handle_user_status
from config import LOG_CHANNEL, BOT_USERNAME, UPDATES_CHANNEL

@Client.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/start":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **Started To Using Me! made by @itzamanrajput** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )      
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention} 🤖 !</b>
        
<b>I'm  AMAN MUSIC 2.O version  Music Bot! A Powerful Bot to Play Music in Your Group Voice Chat 😇! </b>

<b>Also I have more features! Please hit on **/help** to see them 👨‍💻 !</b>

<b>Made by❤️</b> **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙  Add Me To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛠  Help Menu 🛠", callback_data="cbhelpmenu"
                    ),
                    InlineKeyboardButton(
                        "⚒ Create your one 📦", url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4rCYCEpaDCEfmA6KQeOYGRjVFoRCTxsyuRzCxBPCf-U5WeTaoNOW0bKs&s=10"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔔  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support Group ", url="https://t.me/himu_ki_jaan"
                    )
                ]
            ]
        )
    )

    
# Help Menu

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/help":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention} 😉️!</b>

**<b>Here is the Help Menu For This Bot 😊! </b>**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ How To Use Me ⚙️", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚔️  Get Lyrics ", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "🔍 YT Search", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📥 Music Downloader ", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "🎞  YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛠 Delete Commands", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "🧰 Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/credits":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_sticker("CAACAgEAAxkBAAJ8LGD_g_8YHC71w0gzRJxhhKL23XZaAAIjCQAC43gEAAGfWaD2uhnQOSAE")        
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 🤖!</b>

Special Thanks 💝 For all of first code owners 😍</b> !

✅ Credits To,

<b>1️⃣ <a href="https://t.me/fUckEd_uP_bY_LiFE"> My bro </a></b> -  (❤️) !
<b>2️⃣ Left tg |『 @A_B_HA_Y 』</b> - (Odu bro ❤️)
<b>3️⃣ serching </b> - ( Herbroku supporter👨‍💻)
<b>4️⃣ </b>
<b>5️⃣ DevsExpo</b>
<b>6️⃣ TeamDaisyX</b>
<b>7️⃣ Vivek-Tp</b>- ( Fsub & more help ❤️❤️)

Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔔  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/slbotzone"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )   


@Client.on_message(command(["vc", f"vc@{BOT_USERNAME}"]) & other_filters)
async def vc(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/vc":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             🎧  **Voice Chat Link** 🎧
____________________------------______________________

👉️ [Here Is Your Voice Chat Link🎸 ](https://t.me/{message.chat.username}?voicechat) 👈️
____________________------------______________________

Enjoy ❤️!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎭 Share Voice Chat Invitation 🎭 ", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20😉%20%20{VC_LINK}%20❤️**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔔  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/slbotzone"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )

    
@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def search(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/search":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**📢 News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yeah", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Nope ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
