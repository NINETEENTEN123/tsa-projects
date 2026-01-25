# Libraries

import pygame
import sys
import json
import io
import urllib.request

# Other files / classes

from textures import mainScreen
from textures import brutusName as testVars
from textures import metaName as testVars2
from textures import zippyName as testVars3
from textures import vigneshName as testVars4
import functions

# Variables

image1_url = "https://codehs.com/uploads/8cb18d6cb1b15e64ecab69317625acde"

# import later (scene 1)

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((450, 350))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get(): # stops running function
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    # Set screen to 60 FPS
    
    clock.tick(60)
    
    screen.fill("lightblue")
    
    # Load "Characters title"
    
    screen.blit(mainScreen.text_surface, mainScreen.text_rect)
    
    # Load the character names
    
    screen.blit(testVars.text_surface, testVars.text_rect)
    screen.blit(testVars2.text_surface, testVars2.text_rect)
    screen.blit(testVars3.text_surface, testVars3.text_rect)
    screen.blit(testVars4.text_surface, testVars4.text_rect)
    
    # Load the character images
    
        # Load image 1
        
    online_image = functions.loadImage(image1_url)
    sized_image = pygame.transform.scale(online_image, (50, 180))
    screen.blit(sized_image, (30, 150))
    
    # Flip display
    
    pygame.display.flip()

pygame.quit()
