import random

from telethon import events

from NekoRobot import tbot as neko

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
         mm = random.randint(1,100)
         DREAM = f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__"
         await e.reply(DREAM, buttons=BUTTON, file=random.choice(GIF) )
