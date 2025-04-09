import pygame
from pygame.locals import *

class Laser(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, col, jugador_rect, timeRun=7):
        super().__init__()
        self.tiempoVelocidad = timeRun
        # screen = pygame.display.set_mode((x, y))
        self.image = pygame.Surface((5, 45))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = jugador_rect[0]
        self.rect.y = jugador_rect[1] * 0.9  # Ajustar la posición del láser
    
    def getPosicion(self):
        return self.rect.x, self.rect.y
    
    def update(self):
        self.rect.y -= self.tiempoVelocidad