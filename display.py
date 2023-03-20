import re
import pygame

def check_pixel_message_format(message):
    pattern = r'^#[0-9A-Fa-f]{{6}};([1-9]|[1-5]\d|6[0-4]\d|65[0-4]);([1-9]|[1-2]\d|3[0-5]\d|{height})$'.format(
        height=height-1, length=length-1)
    return re.match(pattern, message)

async def display_pixel(pixel, screen):
    screen.set_at((pixel.x, pixel.y), (pixel.red, pixel.green, pixel.blue))
    pygame.display.update()
    await asyncio.sleep(0)

def process_events(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), censor_radius)
            pygame.display.update()
    return False
