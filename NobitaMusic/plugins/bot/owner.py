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
├┤~ @UNREAL_AURA
├┤~ @NobitaMusiccRobot
├┤~ @VanshikaaMusicBot
├┤~ @AuraMusiccRobot
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @II_NOBITA_DEFAULTERS_II
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝚴 𝐎 𝐁 𝚰 𝐓 𝚲 ", url=f"https://t.me/II_NOBITA_DEFAULTERS_II")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/+S0Q1-J_EQLA3YmU1"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/NOBITA_SUPP0RT/15"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/NOBITA_SUPP0RT"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/NobitaMusiccRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
