import numpy as np 
import pygame
from globals import to_screen_coords, normalize_vector 
class Line: 
    def __init__(self, start_pos, end_pos,color): 
        self.start_pos = start_pos 
        self.end_pos = end_pos
        self.color = color
        if start_pos[1] > 0: 
            self.normal = np.array([0,1])
        else: 
            self.normal = np.array([0,-1])

    def draw(self, screen):
        start_pos = to_screen_coords(self.start_pos, screen.get_size())
        end_pos = to_screen_coords(self.end_pos, screen.get_size())
        pygame.draw.line(screen, self.color, start_pos, end_pos)
    def is_collision(self, pos, radius):
        error_tolerance = 0
        if (pos[0] - radius >= self.start_pos[0] and pos[0] + radius <= self.end_pos[0] and abs(pos[1]) + radius + error_tolerance  >= abs(self.start_pos[1])): 
            return True
        return False
        
    def get_normal(self, point): 
        return self.normal
