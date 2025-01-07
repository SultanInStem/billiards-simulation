import pygame 
from globals import to_screen_coords, to_math_coords

class Ball: 
    def __init__(self, pos, radius, velocity_v): 
        self.current_pos = pos 
        self.radius = radius 
        self.vel_v = velocity_v 


    def draw(self, screen): 
        screen_pos = to_screen_coords(self.current_pos, screen.get_size())
        pygame.draw.circle(screen, (255,255,255), screen_pos, self.radius, 0)

    def move(self, steps, obstacles, canvas): 
        step_dx = (self.vel_v[0] / steps)
        step_dy = (self.vel_v[1] / steps) 
        x = self.current_pos[0]
        y = self.current_pos[1]
        for _ in range(steps):  
            new_x = x + step_dx 
            new_y = y + step_dy
            collision_detected = False
            for obstacle in obstacles:
                if obstacle.is_collision(self):
                    collision_detected = True
                    break

            # If a collision is detected, stop the movement at the previous position
            if collision_detected:
                break
            else:
                x = new_x
                y = new_y
        self.current_pos = (x, y)
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
