from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NobitaMusic import app
from config import BOT_USERNAME
from NobitaMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ɴᴏʙɪᴛᴀ ʀᴇᴘᴏ
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ 𝐍ᴏʙɪᴛᴀ ꭙ 𝐌ᴜsɪᴄ ˼ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● **
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/AuraMusiccRobot?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/+S0Q1-J_EQLA3YmU1"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/II_NOBITA_DEFAULTERS_II"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/NOBITA_SUPP0RT"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://t.me/NOBITA_SUPP0RT/15"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
