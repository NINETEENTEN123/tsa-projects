import pygame
import urllib.request
import io

def loadImage(url):
    # 1. Open the URL and read the raw data
    
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
        
    # 2. Convert data into a file-like object Pygame can read
    
    image_file = io.BytesIO(raw_data)
    
    # 3. Load and optimize (use .convert_alpha() for transparency)
    
    return pygame.image.load(image_file).convert_alpha()
