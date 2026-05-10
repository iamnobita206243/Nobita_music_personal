from NobitaMusic import app
from pyrogram import filters, enums
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= BUTTON ================= #

EVAA = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url="https://t.me/AuraMusiccRobot?startgroup=true"
        ),
    ],
]

# ================= INFO TEXT ================= #

INFO_TEXT = """
ㅤ◦•●◉✿ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✿◉●•◦
▬▭▬▭▬▭▬▭▬▭▬▭▬▭

❍ ᴜsᴇʀ ɪᴅ ɴᴏ. ▷ `{}`  
❍ ᴜsᴇʀɴᴇᴍᴇ ▷ {}  
❍ ᴍᴇɴᴛɪᴏɴ ▷ {}  
❍ sᴛᴀᴛᴜs ▷ `{}`  
❍ ᴅᴄ ɪᴅ ▷ `{}`  
❍ ʙɪᴏ ▷ `{}`  

❖ ᴍᴀᴅᴇ ʙʏ ➛ [𝚴 𝐎 𝐁 𝚰 𝐓 𝚲](https://t.me/II_NOBITA_DEFAULTERS_II)
▬▭▬▭▬▭▬▭▬▭▬▭▬▭
"""

# ================= STATUS ================= #

async def userstatus(user_id):
    try:
        user = await app.get_users(user_id)
        x = user.status
        if x == enums.UserStatus.ONLINE:
            return "Online"
        elif x == enums.UserStatus.OFFLINE:
            return "Offline"
        elif x == enums.UserStatus.RECENTLY:
            return "Recently"
        elif x == enums.UserStatus.LAST_WEEK:
            return "Last Week"
        elif x == enums.UserStatus.LONG_AGO:
            return "Long Ago"
    except:
        return "Unknown"

# ================= COMMAND ================= #

@app.on_message(filters.command(
    ["info", "information", "userinfo"],
    prefixes=["/", "!", "%", ",", ".", "@", "#"]
))
async def userinfo(_, message):

    # -------- TARGET USER -------- #
    if message.reply_to_message:
        target = message.reply_to_message.from_user
    elif len(message.command) == 2:
        target = await app.get_users(message.command[1])
    else:
        target = message.from_user

    user = await app.get_users(target.id)
    chat = await app.get_chat(target.id)

    status = await userstatus(user.id)

    user_id = chat.id
    username = f"@{chat.username}" if chat.username else "None"
    mention = f"[{user.first_name}](tg://user?id={user.id})"
    dc_id = user.dc_id or "N/A"
    bio = chat.bio or "No bio"

    text = INFO_TEXT.format(
        user_id,
        username,
        mention,
        status,
        dc_id,
        bio
    )

    # ===== ONLY TEXT OUTPUT ===== #
    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(EVAA),
        parse_mode=ParseMode.MARKDOWN
    )
