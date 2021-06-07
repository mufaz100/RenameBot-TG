import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},

💡 ** I am Stylish Font Bot**

`I can help you to get stylish fonts. Just send me some text and see magic.`

**👲 Maintained By:** [ᴍʜᴅ ᴍᴜꜰᴀᴢ](https://t.me/mufaz123)
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('🤖 Bot Updates', url=f"https://t.me/Bx_Botz")
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



    RENAME_403_ERR = "What Are You Doing? You are Banned"
    UPGRADE_TEXT = "CONTACT @mufaz123"
    DOWNLOAD_START = "Give Me Some Time..."
    UPLOAD_START = "Starting to upload..."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me > ©  @Mallu_Cartoonzz **"
    SAVED_THUMB = "Thumbnail Saved ✅ This Is Permanent"
    DEL_THUMB = "Thumbnail cleared succesfully!"
    NO_THUMB = "No thumbnails found!"
    SAVED_RECVD_DOC_FILE = "File Downloaded Successfully 😎"
    CUSTOM_CAPTION_UL_FILE = " "
    HELP_USER = """It's not that complicated😅
    
1. Send me any Telegram File.
2. Choose appropriate option."""

