"""
GNU General Public License v3.0

Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2021-2022, Awesome-RJ, [ https://github.com/Awesome-RJ ]
Copyright (c) 2021-2022, Yūki • Black Knights Union, [ https://github.com/Awesome-RJ/CutiepiiRobot ]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random

from NekoRobot import DEV_USERS, OWNER_ID, tbot as telethn

from telethon import events, Button
from telegram import ParseMode

GIF = (
    "https://telegra.ph/file/ef94f2f61aa4d9394ef23.mp4",
    "https://telegra.ph/file/b82442bf9ebc32534f7a2.mp4",
    "https://telegra.ph/file/70d43e136125f9c120d2e.mp4",
    "https://telegra.ph/file/45354d3e42982f8de78f4.mp4",
    "https://telegra.ph/file/a22a0930f069686a0c4ef.mp4",
)

BUTTON = [[Button.url("❓ What Is This", "https://t.me/WOFBotsUpdates/4")]]
COMET = "https://telegra.ph/file/713fbfbdde25cc1726866.mp4"
STAR = "https://telegra.ph/file/ad90b44c551cec31df76b.mp4"
WISH = """
**You can use** `/wish` **as a general Wishing Well of sorts**
**For example:**
`/wish I could date you 😍,` **or**
`/wish that sushi was 🍣 in /emojify, or
/wish I had someone to /cuddle at night...`
"""

@telethn.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):
 quew = e.pattern_match.group(1)
 if e.sender_id != DEV_USERS and not quew:
  (await e.reply(WISH, parse_mode=ParseMode.MARKDOWN, buttons=BUTTON, file=STAR),) 
  return   
 if not e.is_reply:
         mm = random.randint(1,100)
         DREAM = f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__"
         await e.reply(DREAM, buttons=BUTTON, file=(random.choice(GIF) )
