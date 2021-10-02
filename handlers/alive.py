# © KennedyProject 2021
# Sena (@xgothboi)
# Kalo ngedit jangan hapus credit ya meki
# YAHAHA WAHYOE

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import DEV_NAME as dn
from config import BOT_NAME as bn, BOT_USERNAME, BOT_IMG, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@SNEHABHI_MUSICxBOT"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e2985056a4f04fa0cc649.jpg",
        caption=f"""**༄ Holla I'm [𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝙼𝚄𝚂𝙸𝙲](https://t.me/SNEHABHI_MUSICxBOT)**

༄ **I'm Working Properly**

༄ **Bot : 6.0 LATEST**

༄ **My Master : [ABHISHEK](https://t.me/SNEHU_IS_MINE)**

༄ **Service Uptime : `{uptime}`**

**Thanks For Using Me ♥️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀʙᴏᴜᴛ", callback_data="cbabout"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ABHI_NETWORK1"
                    )
                ]
            ]
        )
    )
