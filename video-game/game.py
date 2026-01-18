import sys
import os
import pygame
import asyncio
import random

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Async Game Loop Example")

    clock = pygame.time.Clock()
    running = True

    player_pos = [400, 300]
    player_speed = 5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (*player_pos, 50, 50))
        pygame.display.flip()

        await asyncio.sleep(0)  # Yield control to the event loop
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())