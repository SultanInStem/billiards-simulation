import pygame 
from globals import to_screen_coords, to_math_coords

class Arc: 
    def __init__(self, pos, radius):
        self.pos = pos 
        self.radius = radius 


    def draw(self, screen):
        pygame.draw.arc()
        