import pygame 
from globals import to_screen_coords, to_math_coords
import numpy as np
class Ball: 
    def __init__(self, pos, radius, velocity_v): 
        self.current_pos = pos 
        self.radius = radius 
        self.vel_v = velocity_v 
        self.tail = [self.current_pos]
        self.tail_max_length = 50

    def draw(self, screen): 
        screen_pos = to_screen_coords(self.current_pos, screen.get_size())
        pygame.draw.circle(screen, (255,255,255), screen_pos, self.radius, 0)
        for dot in self.tail:
            pygame.draw.circle(screen, (55,25,255), to_screen_coords(dot, screen.get_size()), 1, 0)

    def move(self, steps, obstacles, dt): 
        step_dx = (self.vel_v[0] / steps)
        step_dy = (self.vel_v[1] / steps) 
        x = self.current_pos[0]
        y = self.current_pos[1]
        for _ in range(steps):  
            x += step_dx 
            y += step_dy
            collision_detected = False
            for obstacle in obstacles:
                if obstacle.is_collision((x,y), self.radius):
                    collision_detected = True
                    ### Reflect velocity 
                    x -= step_dx 
                    y -= step_dy
                    normal = obstacle.get_normal((x, y))
                    new_vel = self.vel_v - 2 * (np.dot(normal, self.vel_v)) * normal
                    self.vel_v = new_vel
                    break
            # If a collision is detected, stop the movement at the previous position
            if collision_detected: break
        self.current_pos = (x, y)
        if len(self.tail) < self.tail_max_length: 
            self.tail.append((x,y))
        else: 
            self.tail.pop()
            self.tail.insert(0,(x,y))
    def get_current_pos(self): 
        return self.current_pos 
    def get_velocity(self):
        return self.vel_v
    def get_radius(self): 
        return self.radius
    def set_velocity(self, vel): 
        self.vel_v = vel
    def set_pos(self, point): 
        self.current_pos = point
