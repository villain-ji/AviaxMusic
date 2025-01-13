from pyrogram.types import ChatMemberUpdated
from AviaxMusic import app

@app.on_chat_member_updated()
async def vc_notification(client: Client, chat_member_updated: ChatMemberUpdated):
    # Check if this update is for joining a voice chat
    if chat_member_updated.new_chat_member and chat_member_updated.new_chat_member.is_member:
        user = chat_member_updated.new_chat_member.user
        chat_id = chat_member_updated.chat.id
        
        # Extract user details
        user_id = user.id
        username = f"@{user.username}" if user.username else "No username"
        full_name = user.first_name if user.first_name else "Unknown"
        
        # Create the notification message
        notification_text = (
            f"{full_name} ɪs ᴊᴏɪɴᴇᴅ!\n\n"
            f"ɪᴅ: {user_id}\n"
            f"ɴᴀᴍᴇ: {full_name}\n"
            f"ᴜsᴇʀɴᴀᴍᴇ: {username}"
        )

        # Send the notification to the chat
        await client.send_message(chat_id, notification_text)
