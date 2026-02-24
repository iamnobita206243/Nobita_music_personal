from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NobitaMusic import app
from config import BOT_USERNAME
from NobitaMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - 𝚴 𝐎 𝐁 𝚰 𝐓 𝚲
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴍᴀᴛ ᴊᴀᴀɴᴏ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @NOBITA_SUPP0RT
├┤~ @DEFAULTERS_ERA
├┤~ @NobitaMusicsRobot
├┤~ @VanshikaaMusicBot
├┤~ @SigmaMusicsBot
├┤~ @AppleMusicRobot
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @II_YOUR_NOBITA_II
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝚴 𝐎 𝐁 𝚰 𝐓 𝚲 ", url=f"https://t.me/II_YOUR_NOBITA_II")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/+MytF4Bvu4z8xNDU1"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/NOBITA_SUPP0RT"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/DEFAULTERS_ERA"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/NobitaMusicsRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
