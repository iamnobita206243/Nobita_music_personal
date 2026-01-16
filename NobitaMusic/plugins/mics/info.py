import os
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont

from pyrogram import filters, enums
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from NobitaMusic import app

# ================= BUTTON ================= #

EVAA = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url="https://t.me/NobitaMusicsRobot?startgroup=true"
        ),
    ],
]

# ================= IMAGE MAKER ================= #

async def get_userinfo_img(
    bg_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path).convert("RGBA")

    if profile_path:
        img = Image.open(profile_path).convert("RGBA")
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

        img.putalpha(mask)
        img = img.resize((534, 534))
        bg.paste(img, (607, 86), img)

    path = f"./userinfo_{user_id}.png"
    bg.save(path)
    return path


# ================= CONFIG ================= #

bg_path = "NobitaMusic/assets/RISHUINFO.png"

INFO_TEXT = """
ㅤ◦•●◉✿ **USER INFORMATION** ✿◉●•◦
▬▭▬▭▬▭▬▭▬▭▬▭▬▭

❍ **ᴜsᴇʀ ɪᴅ** ▷ `{}`  
❍ **ᴜsᴇʀɴᴀᴍᴇ** ▷ `{}` 
❍ **ᴍᴇɴᴛɪᴏɴ** ▷ `{}` 
❍ **sᴛᴀᴛᴜs** ▷ `{}`  
❍ **ᴅᴄ ɪᴅ** ▷ `{}`  
❍ **ʙɪᴏ** ▷ `{}`  

❖ **ᴍᴀᴅᴇ ʙʏ** ➛ [𝚴 𝐎 𝐁 𝚰 𝐓 𝚲](https://t.me/II_YOUR_NOBITA_II)
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
            return "Last week"
        elif x == enums.UserStatus.LONG_AGO:
            return "Long ago"
    except:
        return "Unknown"


# ================= COMMAND ================= #

@app.on_message(filters.command(["info", "userinfo", "information"]))
async def userinfo(_, message):

    chat_id = message.chat.id
    is_group = message.chat.type in ["group", "supergroup"]

    # -------- TARGET USER -------- #
    if message.reply_to_message:
        target = message.reply_to_message.from_user
    elif len(message.command) > 1:
        target = await app.get_users(message.command[1])
    else:
        target = message.from_user

    user = await app.get_users(target.id)
    chat = await app.get_chat(target.id)

    status = await userstatus(user.id)

    user_id = chat.id
    username = f"@{chat.username}" if chat.username else "None"
    mention = user.mention
    dc_id = user.dc_id or "N/A"
    bio = chat.bio or "No bio"

    caption = INFO_TEXT.format(
        user_id,
        username,
        mention,
        status,
        dc_id,
        bio
    )

    # ================= GROUP = TEXT ONLY ================= #
    if is_group:
        await message.reply_text(
            caption,
            reply_markup=InlineKeyboardMarkup(EVAA),
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # ================= PRIVATE = IMAGE + TEXT ================= #
    photo = None
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)

    img = await get_userinfo_img(
        bg_path=bg_path,
        user_id=user_id,
        profile_path=photo
    )

    await app.send_photo(
        chat_id,
        photo=img,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(EVAA),
        parse_mode=ParseMode.MARKDOWN
    )

    if os.path.exists(img):
        os.remove(img)
