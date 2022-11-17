import random

from telethon import events

from NekoRobot import DEV_USERS, OWNER_ID, tbot as neko

from tbot import events, Button
from telegram import ParseMode

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

GIF = (
    "https://telegra.ph/file/ef94f2f61aa4d9394ef23.mp4",
    "https://telegra.ph/file/b82442bf9ebc32534f7a2.mp4",
    "https://telegra.ph/file/70d43e136125f9c120d2e.mp4",
    "https://telegra.ph/file/45354d3e42982f8de78f4.mp4",
    "https://telegra.ph/file/a22a0930f069686a0c4ef.mp4",
)


@neko.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):
 quew = e.pattern_match.group(1)
 if e.sender_id != DEV_USERS and not quew:
  (await e.reply(WISH, parse_mode=ParseMode.MARKDOWN, buttons=BUTTON, file=STAR),) 
  return
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = random.choice(GIF)
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
