import io
import base64
import requests
from datetime import datetime
from PIL import Image, PngImagePlugin
from pyrogram import Client, filters
from pyrogram.types import Message

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    SD_URL,
    ALLOWED_CHATS,
    PAYLOAD,
)
from handlers import start_handler, callback, illegal_callback, log_request

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define a handler function for the "/start" command
app.on_message(filters.command("start"))(start_handler)

# Define a handler function for valid requests
app.on_message(
    filters.chat(ALLOWED_CHATS) & filters.command("imagine") & filters.text
)(callback)

# Define a handler function for illegal requests
app.on_message(
    ~filters.chat(ALLOWED_CHATS) & filters.command("imagine") & filters.text
)(illegal_callback)

# Run the bot
app.run()
