import pygame 
import sys
import numpy as np
from ball import Ball
from table import Table
from globals import to_screen_coords
class Canvas: 
    def __init__(self,size):
        pygame.init()
        self.running = True 
        pygame.display.set_caption("Bunimovich Stadium")
        self.screen = pygame.display.set_mode(size) 
        self.clock = pygame.time.Clock()
        self.balls = [Ball((-220,0), 10, np.array([0,2]))]
        self.table = Table(250, (255,0,0))
        self.is_paused = False
        self.steps = 100

    def update(self): 
        for i in range(0, len(self.balls)): 
            obstacles = self.table.get_obstacles()
            self.balls[i].move(self.steps, obstacles, self)

    def render(self): 
        self.screen.fill((0,0,0))

        for ball in self.balls: 
            ball.draw(self.screen)

        self.table.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(90)
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False 

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    self.is_paused = not self.is_paused

    def run(self): 
        while(self.running):
            self.handle_events() 
            if self.is_paused == False: self.update()
            self.render()
        pygame.quit()
        sys.exit()