#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, APPROVE_TXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import time
from pyrogram.enums import ParseMode

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "approve":
        hash = int(time.time())
        await query.message.edit_text(text=APPROVE_TXT.format(client.username, hash), parse_mode=ParseMode.HTML)
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass