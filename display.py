import pygame
import asyncio
from config import length, height, censor_radius


# Display a pixel on the screen
async def display_pixel(pixel, screen):
    screen.set_at((pixel.x, pixel.y), (pixel.red, pixel.green, pixel.blue))
    pygame.display.update()
    await asyncio.sleep(0)


# Process events and handle mouse clicks
def process_events(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Draw a white circle to censor a portion of the screen when the mouse is clicked
            pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), censor_radius)
            pygame.display.update()
    return False
