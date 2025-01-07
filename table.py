import pygame 
import math
from globals import to_math_coords, to_screen_coords
from arc import Arc 
from line import Line
class Table: 
    def __init__(self, radius, color): 
        self.type = type
        self.line_top = Line((-radius, radius), (radius, radius), color)
        self.line_bottom = Line((-radius, -radius), (radius, -radius), color)

        self.arc_right = Arc((radius, 0), 2*radius, 3 *math.pi / 2, math.pi / 2, color)
        self.arc_left = Arc((-radius, 0), 2*radius, math.pi / 2, 3*math.pi / 2, color)

        self.shapes = [self.line_top, self.line_bottom, self.arc_right, self.arc_left]
    def draw(self, screen):
        for shape in self.shapes: 
            shape.draw(screen)

    def handle_collisions(self, ball, c): 
        for shape in self.shapes: 
            if shape.is_collision(ball): 
                print("Collision Detected")
                c.is_paused = True
                break