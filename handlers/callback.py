# (C) KennedyProject github.com/KennedyProject

from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME as bn, BOT_IMG, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


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


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π **Hello {message.from_user.mention}** β \n
**[{ππ½π΄π·π°π±π·πΈ πΌπππΈπ²](https://t.me/SNEHABHI_MUSICxBOT) Is a bot designed to play music in your voice chat groups!**
**To see some commands for using this bot, click Β» /help**
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


@Client.on_callback_query(filters.regex("cbabout"))
async def cbabout(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>β **About  [{bn}](https://t.me/{BOT_USERNAME})**</b> 

β  **A powerfull bot for playing music for groups!

β  Working with pyrogram

β  Using Python 3.9.7

β  Can play and download music or videos from YouTube

β  I can make you happy

β  For more info click /help

__{bn} licensed under the GNU General Public License v.3.0__

β’ Updates channel @{UPDATES_CHANNEL}
β’ Group Support @{GROUP_SUPPORT}
β’ Assistant @{ASSISTANT_NAME}
β’ Here is my [Owner](https://t.me/{OWNER_NAME})**

β Wanna make your own bot music? try click Source button!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sα΄α΄Κα΄α΄ββ", url="https://t.me/ABHI_NETWORK"
                    ),
                    InlineKeyboardButton(
                        "Κα΄α΄α΄β", callback_data="cbadvanced"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ποΈ Here is the help menu !</b>

**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

π‘ Bot by @SNEHU_IS_MINE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Basic Cmd", callback_data="cbbasic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "π Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ποΈ basic commands for bots

[GROUP SETTINGS]
/play (title) - play music via youtube
/ytp (title) - play music live
/stream (reply to audio) - play music via reply to audio
/playlist - view queue list
/song (title) - download music from youtube
/search (title) - search for music from youtube in detail
/video (title) - download music from youtube in detail
/lyrics (title) - search for lyrics
/shazam (reply audio) - for identifying song name
/q (reply text) - to make a quotes sticker
/id - to show your id or chat id
[ MORE ]
/alive - check alive bot
/start - starting bot
/ping - show current ping

π‘ Bot by @SNEHU_IS_MINE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await query.edit_message_text(
        f"""**ΰΌ Holla I'm [{ππ½π΄π·π°π±π·πΈ πΌπππΈπ²](https://t.me/SNEHABHI_MUSICxBOT)**

ΰΌ **I'm Working Properly**

ΰΌ **Bot : 6.0 LATEST**

ΰΌ **My Master : [ABHISHEK](https://t.me/SNEHU_IS_MINE)**

ΰΌ **Service Uptime : `{uptime}`**

**Thanks For Using Me β₯οΈ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "α΄Κα΄α΄α΄", callback_data="cbabout"
                    ),
                    InlineKeyboardButton(
                        "α΄Κα΄Ι΄Ι΄α΄Κ", url=f"https://t.me/ABHI_NETWORK1"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ποΈ command for group admin

/player - view playback status
/pause - pauses playing music
/resume - resume paused music
/skip - skip to next song
/end - mute the music
/userbotjoin - invite assistant to join the group
/musicplayer (on / off) - turn on / off the music player in your group

π‘ Bot by @SNEHU_IS_MINE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ποΈ **command for sudo**

**/userbotleaveall - remove assistant from all groups
/gcast - send global messages via assistant
/rmd - delete downloaded files

π‘ Bot by @SNEHU_IS_MINE**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ποΈ **Command fun**

**/chika - check it yourself
/wibu - check it yourself
/asupan - check yourself
/truth - check yourself
/dare - check it yourself
/q - to make quotes text

π‘ Bot by @SNEHU_IS_MINE**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**HOW TO USE THIS BOTT :**

**1.) First, add to your group.
2.) Then make admin with all permissions except anonymous admin.
3.) Add @SNEHABHI_MUSIC to your group or type `/userbotjoin` to invite assistant.
4.) Turn on voice chat first before playing music.

π‘ Bot by @SNEHU_IS_MINE**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
