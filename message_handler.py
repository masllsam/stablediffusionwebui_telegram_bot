from typing import List
from pyrogram.types import Message, InputMediaPhoto


async def send_images_as_album(message: Message, images: List[bytes], caption: str = "") -> None:
    media = [InputMediaPhoto(i) for i in images]
    await message.reply_media_group(media, caption=caption)
