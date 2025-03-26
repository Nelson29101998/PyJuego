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
        #Los botones del teclado
        teclado = pygame.key.get_pressed()
        
        #Los botones del joystick
        arriba = pygame.joystick.Joystick(0).get_button(11)
        abajo = pygame.joystick.Joystick(0).get_button(12)
        izquierda = pygame.joystick.Joystick(0).get_button(13)
        derecha = pygame.joystick.Joystick(0).get_button(14)
            
        if teclado[K_LEFT] or izquierda:
            self.rect.x -= self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_RIGHT] or derecha:
            self.rect.x += self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_UP] or arriba:
            self.rect.y += self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if teclado[K_DOWN] or abajo:
            self.rect.y -= self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if not (teclado[K_LEFT] or izquierda) and not (teclado[K_RIGHT] or derecha):
            self.velocidad[0] = 3

        if not (teclado[K_UP] or arriba) and not (teclado[K_DOWN] or abajo):
            self.velocidad[1] = -3
        