import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from NobitaMusic import app
from config import BOT_USERNAME

SACHIN = [
    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✙", url=f"https://t.me/NobitaMusicsRobot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/NOBITA_SUPP0RT"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ ˹ 𝐍ᴏʙɪᴛᴀ ꭙ 𝐌ᴜsɪᴄ ˼", reply_markup=InlineKeyboardMarkup(SACHIN),)
