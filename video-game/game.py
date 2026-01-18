import sys
import os
import pygame
import asyncio
import random

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Async Pygame Example")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Draw a random rectangle
        rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rect_position = (random.randint(0, 700), random.randint(0, 500), 100, 100)
        pygame.draw.rect(screen, rect_color, rect_position)

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)  # Yield control to the event loop

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    asyncio.run(main())
    # End of file