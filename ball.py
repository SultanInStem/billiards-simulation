import pygame 
from globals import to_screen_coords, to_math_coords

class Ball: 
    def __init__(self, pos, radius, velocity_v): 
        self.current_pos = pos 
        self.previous_pos = pos
        self.radius = radius 
        self.vel_v = velocity_v 


    def draw(self, screen): 
        screen_pos = to_screen_coords(self.current_pos, screen.get_size())
        pygame.draw.circle(screen, (255,255,255), screen_pos, self.radius, 0)

    def move(self): 
        x = self.current_pos[0] + self.vel_v[0]
        y = self.current_pos[1] + self.vel_v[1] 
        self.previous_pos = self.current_pos 
        self.current_pos = (x, y)
    def get_current_pos(self): 
        return self.current_pos 
    def get_previous_pos(self): 
        return self.previous_pos
    def get_velocity(self):
        return self.vel_v
    def get_radius(self): 
        return self.radius
