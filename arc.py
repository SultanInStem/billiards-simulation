import pygame 
from globals import to_screen_coords, to_math_coords, normalize_vector
import math
import numpy as np 

class Arc: 
    def __init__(self, center_pos, radius, start_angle, end_angle, color):
        center_x = center_pos[0] - (radius // 2)
        center_y = center_pos[1] + (radius // 2)
        self.pos = (center_x, center_y)
        self.center_pos = center_pos
        self.radius = radius 
        self.start_angle = start_angle 
        self.end_angle = end_angle 
        self.color = color


    def draw(self, screen):
        pos = to_screen_coords(self.pos, screen.get_size())
        rect = pygame.Rect(pos[0], pos[1], self.radius, self.radius) 
        pygame.draw.arc(
            screen,
            self.color,
            rect, 
            self.start_angle, 
            self.end_angle
        )

    def is_collision(self, pos, radius):
        error_tolerance = 2
        distance = math.sqrt((self.center_pos[0] - pos[0])**2 + (self.center_pos[1] - pos[1])**2)
        if self.start_angle > self.end_angle: 
            ### Right arc 
            if pos[0] > self.center_pos[0] and (distance + radius + error_tolerance) >= (self.radius / 2): 
                return True 
            return 
        else: 
            ### Left arc 
            if pos[0] < self.center_pos[0] and (distance + radius + error_tolerance) >= (self.radius / 2): 
                return True
            return False
    def get_normal(self, point): 
        return normalize_vector(np.array([point[0] - self.center_pos[0], point[1] - self.center_pos[1]]))