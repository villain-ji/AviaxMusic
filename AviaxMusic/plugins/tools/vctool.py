from pyrogram import Client, filters
from pyrogram.types import Message
from AviaxMusic import app
from pyrogram import *
from pyrogram.types import *
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogpyrogramram.raw.types import InputGroupCall
from AviaxMusic.utils.database import get_assistant
from telethon.tl.functions.phone import (
    CreateGroupCallRequest,
    DiscardGroupCallRequest,
    GetGroupCallRequest,
    InviteToGroupCallRequest,
)


# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    await msg.reply("**😍ᴠɪᴅᴇᴏ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ🥳**")


# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    await msg.reply("**😕ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ💔**")


# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"➻ {message.from_user.mention}\n\n**๏ ɪɴᴠɪᴛɪɴɢ ɪɴ ᴠᴄ ᴛᴏ :**\n\n**➻ **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        reply_text = f"{text} 🤭🤭"

        await message.reply(
            reply_text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="๏ ᴊᴏɪɴ ᴠᴄ ๏", url=add_link)],
                ]
            ),
        )
    except Exception as e:
        print(f"Error: {e}")


###
