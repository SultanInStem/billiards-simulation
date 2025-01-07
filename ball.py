import pygame 
from globals import to_screen_coords, to_math_coords

class Ball: 
    def __init__(self, pos, radius, velocity_v): 
        self.pos = pos 
        self.radius = radius 
        self.vel_v = velocity_v 


    def draw(self, screen): 
        screen_pos = to_screen_coords(self.pos, screen.get_size())
        pygame.draw.circle(screen, (255,255,255), screen_pos, self.radius, 0)

    def move(self): 
        x = self.pos[0] + self.vel_v[0]
        y = self.pos[1] + self.vel_v[1] 
        self.pos = (x, y)
    def get_math_pos(self): 
        return self.pos 
    def get_velocity(self):
        return self.vel_v
    def get_radius(self): 
        return self.radius
