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
        self.balls = [Ball((0,0), 10, np.array([3,1]))]
        self.table = Table(250, (255,0,0))

    def update(self): 
        for i in range(0, len(self.balls)): 
            self.table.handle_collisions(self.balls[i])
            self.balls[i].move()

    def render(self): 
        self.screen.fill((0,0,0))

        for ball in self.balls: 
            ball.draw(self.screen)

        self.table.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
    def handle_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False 

    def run(self): 
        while(self.running):
            self.handle_events() 
            self.update()
            self.render()
        pygame.quit()
        sys.exit()