from datetime import datetime

from pyrogram.types import Message

from config import ALLOWED_CHATS


def log_request(chat_id: int, message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("requests.log", "a") as f:
        f.write(f"[{timestamp}] Chat ID: {chat_id} - Message: {message}\n")


async def illegal_callback(_, message: Message) -> None:
    chat_id = message.chat.id
    log_request(chat_id, message.text.strip())
    await message.reply_text("Sorry, you're not authorized to use this command.")
