from audio import play_sound, freq_from_pixel
from pixel import Pixel
from display import display_pixel
from config import height, length, no_sound
import asyncio
import re


# Check if message text follows pixel format
def check_pixel_message_format(message):
    pattern = fr'^#[0-9A-Fa-f]{{6}};([0-9]\d{{0,{height-1}}});([0-9]\d{{0,{length-1}}})$'
    return re.match(pattern, message)


async def pixel_from_message(match):
    color, x, y = match.group(0).split(';')
    red, green, blue = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    x, y = int(x), int(y)
    return Pixel(red, green, blue, x, y)


async def process_messages(message, screen):
    match = check_pixel_message_format(message)
    if match is not None:
        pixel = await pixel_from_message(match)
        if not no_sound:
            asyncio.create_task(play_sound(pixel))
        await display_pixel(pixel, screen)
