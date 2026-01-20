import pygame
import sys
import random
import os
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        text = font.render("Hello, Game!", True, (255, 255, 255))
        screen.blit(text, (250, 250))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # Yield control to the event loop

asyncio.run(main())