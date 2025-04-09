import pygame
from pygame.locals import *

class Laser(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, col, jugador_rect, timeRun=7, maxLargo=45):
        super().__init__()
        self.maxLargo = maxLargo
        if maxLargo <= 45:
            self.tiempoVelocidad = timeRun
        else:
            self.tiempoVelocidad = 0
        # screen = pygame.display.set_mode((x, y))
        self.image = pygame.Surface((5, maxLargo))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = jugador_rect[0]
        self.rect.y = jugador_rect[1] * 0.9  # Ajustar la posición del láser
    
    def getPosicion(self):
        return self.rect.x, self.rect.y
    
    def update(self):
        if self.maxLargo <= 45:
            self.rect.y -= self.tiempoVelocidad
        else:
            self.rect.y -= self.tiempoVelocidad