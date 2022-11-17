import random

from telethon import events

from NekoRobot import tbot as neko

GIF = (
    "CAACAgUAAxkBAAIIW2NL5v9F9hUom4xmsgNYb63SEfZZAAIZBgACYAF5VIerYoMcSln8KgQ",
    "CAACAgUAAxkBAAIIT2NL5tVmdAO3n1o3cp9Jic9LkqJvAAK7AgACoU3RVLpdwYfQPmS9KgQ",
    "CAACAgUAAxkBAAIIUGNL5tVNd0rwdoMv-uDVcZ3hHgwlAAIwAwACP9jQVMv2AfU-DvBfKgQ",
    "CAACAgUAAxkBAAIIUmNL5tUzCtvS5E-XR8h3tFMSqVu7AAIGAwACNZnYVOTUhlBiHTQGKgQ",
    "CAACAgUAAxkBAAIIUWNL5tVBEQAB2gWLSq0ymEPeAj5kmQAC3QEAAuu92VSPj3UkCiNvfioE",
)


@neko.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://telegra.ph/file/cae00f6c0729da2a93315.mp4"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__chance of success {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = random.choice(GIF)
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
