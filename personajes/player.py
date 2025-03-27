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
        buttonJoy = pygame.joystick.Joystick(0)
            
        if teclado[K_LEFT] or buttonJoy.get_button(13): #Si se presiona la tecla izquierda o el boton 13 del joystick
            self.rect.x -= self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_RIGHT] or buttonJoy.get_button(14): #Si se presiona la tecla derecha o el boton 14 del joystick
            self.rect.x += self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_UP] or buttonJoy.get_button(11): #Si se presiona la tecla arriba o el boton 11 del joystick
            self.rect.y += self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if teclado[K_DOWN] or buttonJoy.get_button(12): #Si se presiona la tecla abajo o el boton 12 del joystick
            self.rect.y -= self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if not (teclado[K_LEFT] or buttonJoy.get_button(13)) and not (teclado[K_RIGHT] or buttonJoy.get_button(14)):
            self.velocidad[0] = 3

        if not (teclado[K_UP] or buttonJoy.get_button(11)) and not (teclado[K_DOWN] or buttonJoy.get_button(12)):
            self.velocidad[1] = -3
        