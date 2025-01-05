import pygame 
import sys
class Canvas: 
    def __init__(self,size):
        pygame.init()
        self.running = True 
        pygame.display.set_caption("Billiards bitches")
        self.screen = pygame.display.set_mode(size) 
        self.clock = pygame.time.Clock()

    def update(self): 
        pass 

    def render(self): 
        self.screen.fill((0,0,0))


        pygame.display.flip()
        self.clock.tick(60)
    def handle_events(self): 
        for event in pygame.event.get():
            if event == pygame.QUIT: 
                self.running = False 

    def run(self): 
        while(self.running):
            self.handle_events() 
            self.update()
            self.render()
        pygame.quit()
        sys.exit()