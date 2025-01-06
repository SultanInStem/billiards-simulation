import pygame 
import sys
import numpy as np
from ball import Ball
from table import Table
class Canvas: 
    def __init__(self,size):
        pygame.init()
        self.running = True 
        pygame.display.set_caption("Billiards bitches")
        self.screen = pygame.display.set_mode(size) 
        self.clock = pygame.time.Clock()
        self.ball = Ball((0,0), 10, np.array([-3,1]))
        self.table = Table()

    def update(self): 
        self.ball.move()

    def render(self): 
        self.screen.fill((0,0,0))

        self.ball.draw(self.screen)
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