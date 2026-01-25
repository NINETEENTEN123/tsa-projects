import pygame, sys, json

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# MAIN SCREEN

class mainScreen:
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render("Choose your character", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (400 / 2, (350 / 2) - 80)
    
class brutusName:
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Brutus", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = ((400 / 2) - 140, (350 / 2) - 40)
    
class metaName:
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Meta", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = ((400 / 2) + 140, (350 / 2) - 40)
    
class zippyName:
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Zippy", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = ((400 / 2) -50, (350 / 2) - 40)
    
class vigneshName:
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Vignesh", True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = ((400 / 2) +50, (350 / 2) - 40) 
