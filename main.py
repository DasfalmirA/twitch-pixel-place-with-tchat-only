import asyncio
import time
import pygame
import os
from config import *
from twitch_bot import TwitchBot
from display import process_events


async def game_loop(bot, screen):
    frame_time = 1 / fps
    running = True
    while running:
        await asyncio.sleep(0)
        start_time = time.monotonic()
        if process_events(screen):
            running = False
        await asyncio.sleep(0)
        elapsed_time = time.monotonic() - start_time
        remaining_time = frame_time - elapsed_time
        if remaining_time > 0:
            await asyncio.sleep(remaining_time)
    await asyncio.sleep(1)
    await bot.close()


def load_save(screen):
    image_count = 0
    if os.path.exists(f"saved_image_{image_count}.png"):
        while os.path.exists(f"saved_image_{image_count}.png"):
            image_count += 1
        image_count -= 1
        saved_image = pygame.image.load(f"saved_image_{image_count}.png")
        screen.blit(saved_image, (0, 0))
        image_count += 1
        pygame.display.flip()
    else:
        screen.fill((0, 0, 0))
    return image_count


def save_and_quit(screen, image_count):
    pygame.image.save(screen, f"saved_image_{image_count}.png")
    pygame.quit()


async def main():
    pygame.init()
    screen = pygame.display.set_mode((length, height))
    image_count = load_save(screen)
    pygame.display.set_caption("Pixel Display")
    bot = TwitchBot(screen)
    tasks = [asyncio.create_task(bot.start()), asyncio.create_task(game_loop(bot, screen))]
    await asyncio.gather(*tasks)
    await asyncio.sleep(1)
    save_and_quit(screen, image_count)

asyncio.run(main())
