import pygame, sys
from pygame.locals import *

class mainApp(self):
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set.caption("Termometro")
        self.__screen.fill((244, 236, 203))
        
    def __on_close(self):
        pygame.quit()
        sys.quit()
        sys.exit()
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    slef.__on_close()
            
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
    
        
        