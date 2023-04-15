import os
import io
import base64
import requests
from datetime import datetime
from PIL import Image, PngImagePlugin
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

from config import ALLOWED_CHATS, SD_URL, PAYLOAD

# Initialize the Pyrogram client
app = Client("my_bot")


def log_request(chat_id, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("requests.log", "a") as f:
        f.write(f"[{timestamp}] Chat ID: {chat_id} - Message: {message}\n")


# Define a handler function for the "/start" command
@app.on_message(filters.command("start"))
async def start_handler(_, message: Message) -> None:
    await message.reply_text("Hello! Send me a message with the /imagine command and I'll create an image of it for you.")


# Define a handler function for valid requests
@app.on_message(filters.chat(ALLOWED_CHATS) & filters.command("imagine") & filters.text)
async def callback(_, message: Message) -> None:
    chat_id = message.chat.id
    prompt = message.text.strip()

    if not prompt:
        await message.reply_text("Please enter some text.")
        return

    log_request(chat_id, prompt)

    payload = PAYLOAD.copy()
    payload["prompt"] = prompt

    response = requests.post(url=f"{SD_URL}/sdapi/v1/txt2img", json=payload)

    if not response.ok:
        await message.reply_text("An error occurred while processing the image.")
        return

    r = response.json()

    if not r.get("images"):
        await message.reply_text("An error occurred while processing the image.")
        return

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{SD_URL}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('output.png', pnginfo=pnginfo)

        image_buffer = io.BytesIO()
        image.save(image_buffer, format="PNG")
        image_buffer.seek(0)

        await message.reply_photo(photo=image_buffer)


# Define a handler function for illegal requests
@app.on_message(~filters.chat(ALLOWED_CHATS) & filters.command("imagine") & filters.text)
async def illegal_callback(_, message: Message) -> None:
    chat_id = message.chat.id
    log_request(chat_id, message.text.strip())
    await message.reply_text("Sorry, you're not authorized to use this command.")
