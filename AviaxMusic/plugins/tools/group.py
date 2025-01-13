from pyrogram import Client, filters
from pyrogram.types import Message
from AviaxMusic import app
from config import OWNER_ID

# Invite members on voice chat
@app.on_message(filters.video_chat_members_invited)
async def handle_invite(app: Client, message: Message):
    try:
        inviter = message.from_user.mention if message.from_user else "Unknown User"
        text = f"♻️ ❛{inviter}❜ 💞™🌙 ɪɴᴠɪᴛᴇᴅ "
        invited_users = message.video_chat_members_invited.users
        
        if not invited_users:
            await message.reply("No users were invited.")
            return

        for user in invited_users:
            try:
                text += f"🖤[{user.first_name}](tg://user?id={user.id})🖤 "
            except Exception:
                text += "🖤[Unknown User]🖤 "

        await message.reply(text)
    except Exception as e:
        print(f"Error in handle_invite: {e}")


# Math calculation command
@app.on_message(filters.command("math", prefixes="/"))
async def calculate_math(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply("Please provide an expression to evaluate.")
            return

        expression = message.text.split("/math ", 1)[1]
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except Exception:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    await message.reply(response)


# Leave group command
@app.on_message(filters.command("leavegroup") & filters.user(OWNER_ID))
async def bot_leave(app: Client, message: Message):
    try:
        chat_id = message.chat.id
        await app.leave_chat(chat_id=chat_id, delete=True)
        await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ !!.")
    except Exception as e:
        await message.reply(f"Failed to leave the group: {e}")
