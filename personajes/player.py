import pygame
from pygame.locals import *


class Jugador(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, image_file,  x, y):
        super().__init__()
        self.aceleracion = 0.1
        self.velocidad = [3, -3]
        self.image = pygame.transform.scale(
            pygame.image.load(image_file).convert_alpha(), (95, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.topleft = (x, y)

    def update(self):
        teclado = pygame.key.get_pressed()
        if teclado[K_LEFT]:
            self.rect.x -= self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_RIGHT]:
            self.rect.x += self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_UP]:
            self.rect.y += self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if teclado[K_DOWN]:
            self.rect.y -= self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if not teclado[K_LEFT] and not teclado[K_RIGHT]:
            self.velocidad[0] = 3

        if not teclado[K_UP] and not teclado[K_DOWN]:
            self.velocidad[1] = -3
