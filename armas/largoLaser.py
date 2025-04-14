import pygame
from pygame.locals import *

class Largo(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, col, jugador_rect):
        super().__init__()
        self.image = pygame.Surface((5, 45))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        # self.rect.x = jugador_rect[0]
        # self.rect.y = jugador_rect[1] * 0.9
        
        self.active = False  # Estado inicial: no visible
        
    def handle_click(self):
        """Activa el dibujo del cuadrado."""
        self.active = True

    
    def update(self):
        """Actualiza el estado del sprite."""
        if self.active:
            self.image.fill((255, 0, 0))  # Mantiene el cuadrado rojo