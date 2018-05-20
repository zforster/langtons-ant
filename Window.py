import pygame
import sys
from Logic import Logic

pygame.init()

width = 1280
height = 720

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Langton's Ant")

class Window(object):
    def __init__(self):
        self.Main()
    
    def Main(self):
        self.fps = 120
        self.clock = pygame.time.Clock()
        window.fill((0,0,0))
        self.logic = Logic(width,height,1,window)
        while True:
            self.logic.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
            self.clock.tick(self.fps)
