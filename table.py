import pygame 
import math
from globals import to_math_coords, to_screen_coords
class Table: 
    def __init__(self): 
        self.type = type
    def draw(self, screen): 
        color = (255, 0, 0)
        pygame.draw.line(
            screen, 
            color, 
            to_screen_coords((-250,250), screen.get_size()), 
            to_screen_coords((250, 250), screen.get_size())
        )
        pygame.draw.line(
            screen, 
            color, 
            to_screen_coords((-250,-250), screen.get_size()), 
            to_screen_coords((250, -250), screen.get_size())
        )
        rect_one_pos = to_screen_coords((0,250), screen.get_size())
        rect_one = pygame.Rect(rect_one_pos[0], rect_one_pos[1], 500, 500)
        pygame.draw.arc(
            screen, 
            color, 
            rect_one, 
            3 * math.pi / 2,
            math.pi / 2
        )
        rect_two_pos = to_screen_coords((-500,250), screen.get_size())
        rect_two = pygame.Rect(rect_two_pos[0], rect_two_pos[1], 500, 500)
        pygame.draw.arc(
            screen, 
            color, 
            rect_two,
            math.pi / 2, 
            3 * math.pi / 2
        )
