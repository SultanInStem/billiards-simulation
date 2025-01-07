import pygame
from globals import to_screen_coords 
class Line: 
    def __init__(self, start_pos, end_pos,color): 
        self.start_pos = start_pos 
        self.end_pos = end_pos
        self.color = color

    def draw(self, screen):
        start_pos = to_screen_coords(self.start_pos, screen.get_size())
        end_pos = to_screen_coords(self.end_pos, screen.get_size())
        pygame.draw.line(screen, self.color, start_pos, end_pos)
    def is_collision(self, ball):
        ball_pos = ball.get_current_pos()
        ball_radius = ball.get_radius()
        error_tolerance = 2
        return (ball_pos[0] - ball_radius >= self.start_pos[0] and ball_pos[0] + ball_radius <= self.end_pos[0] and abs(ball_pos[1] + ball_radius + error_tolerance) >= abs(self.start_pos[1]))