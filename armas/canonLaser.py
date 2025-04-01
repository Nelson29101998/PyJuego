import pygame
from pygame.locals import *

class Laser(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, col, x, y):
        super().__init__()
        # screen = pygame.display.set_mode((x, y))
        self.image = pygame.Surface((5, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        pass