from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import sudo_users_only, authorized_users_only


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


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>π **Hello {message.from_user.mention}** β \n
**[ππ½π΄π·π°π±π·πΈ πΌπππΈπ²](https://t.me/{SNEHABHI_MUSICxBOT}) Is a bot designed to play music in your voice chat groups!**
**To see some commands for using this bot, click Β» /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "β α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄β β", url=f"https://t.me/SNEHABHI_MUSICxBOT?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Κα΄α΄α΄ββ", url="https://t.me/ABHI_NETWORK"
                    ),
                    InlineKeyboardButton(
                        "α΄α΄α΄α΄α΄α΄s", url=f"https://t.me/ABHI_NETWORK")
                ],[
                    InlineKeyboardButton(
                        "Κα΄α΄‘ α΄α΄ α΄sα΄ α΄α΄β ββ", callback_data="cbguide"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await message.reply_text(
        f"""<b>π **Hello {message.from_user.mention()}** β</b>

β **ZINDA HU BE TU SONG PLAY KAR!
β’ Start time: `{START_TIME_ISO}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π₯ Support", url=f"https://t.me/ABHI_NETWORK"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["help", f"help@SNEHABHI_MUSICxBOT"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>π **Hello** {message.from_user.mention()}</b>
**Please press the button below to read the explanation and see the list of available commands !**

π‘ Bot by @SNEHU_IS_MINE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" HOW TO USE ME", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>π **Hello {message.from_user.mention} welcome to the help menu !**</b>

**__In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command__**

π‘ Bot by @SNEHU_IS_MINE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "HELP", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command(["ping", f"ping@SNEHABHI_MUSICxBOT"]) & ~filters.edited)
@authorized_users_only
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await m_reply.edit_text(
        f"π **Pong !!** `{delta_ping * 1000:.3f} ms`\n"
        f"β‘ **uptime:** `{uptime}`"
    )


@Client.on_message(command(["uptime", f"uptime@SNEHABHI_MUSICxBOT"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ bot status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )
