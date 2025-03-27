import pygame
from pygame.locals import *

class Jugador(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, image_file,  x, y):
        self.cambiarXL3, self.cambiarYL3, self.cambiarXR3, self.cambiarYR3 = 0, 0, 0, 0
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
        
        if teclado[K_LEFT]: #Si se presiona la tecla izquierda o el boton 13 del joystick
            self.rect.x -= self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_RIGHT]: #Si se presiona la tecla derecha o el boton 14 del joystick
            self.rect.x += self.velocidad[0]
            self.velocidad[0] += self.aceleracion

        if teclado[K_UP]: #Si se presiona la tecla arriba o el boton 11 del joystick
            self.rect.y += self.velocidad[1]
            self.velocidad[1] -= self.aceleracion

        if teclado[K_DOWN]: #Si se presiona la tecla abajo o el boton 12 del joystick
            self.rect.y -= self.velocidad[1]
            self.velocidad[1] -= self.aceleracion
        
        #Los botones del joystick
        if pygame.joystick.get_count() > 0:      
            buttonJoy = pygame.joystick.Joystick(0)
            ejeXL3 = buttonJoy.get_axis(0) #Eje X L3
            ejeYL3 = buttonJoy.get_axis(1) #Eje Y L3
            self.cambiarXL3 += ejeXL3 * 2
            self.cambiarYL3 += ejeYL3 * 2
            print("Eje X L3: ", self.cambiarXL3 , ", Eje Y L3: ", self.cambiarYL3)
            
            ejeXR3 = buttonJoy.get_axis(2) #Eje X R3
            ejeYR3 = buttonJoy.get_axis(3) #Eje Y R3
            self.cambiarXR3 += ejeXR3 * 2
            self.cambiarYR3 += ejeYR3 * 2
            print("Eje X R3: ", self.cambiarXR3 , ", Eje Y R3: ", self.cambiarYR3)
            
            empujarL2 = buttonJoy.get_axis(4) #Empujar L2
            empujarR2 = buttonJoy.get_axis(5) #Empujar R2
            l2_normalized = empujarL2 / 0.9 if empujarL2 > 0 else 0
            r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0
            
            l2_normalized = float(min(max(l2_normalized, 0), 1))
            r2_normalized = float(min(max(r2_normalized, 0), 1))
            
            print("Empujar L2: ", l2_normalized , ", Empujar R2: ", r2_normalized)
            
            if buttonJoy.get_button(13): #Si se presiona la tecla izquierda o el boton 13 del joystick
                self.rect.x -= self.velocidad[0]
                self.velocidad[0] += self.aceleracion
            
            if buttonJoy.get_button(14): #Si se presiona la tecla derecha o el boton 14 del joystick
                self.rect.x += self.velocidad[0]
                self.velocidad[0] += self.aceleracion
            
            if buttonJoy.get_button(11):
                self.rect.y += self.velocidad[1] #Si se presiona la tecla arriba o el boton 11 del joystick
                self.velocidad[1] -= self.aceleracion
            
            if buttonJoy.get_button(12): #Si se presiona la tecla abajo o el boton 12 del joystick
                self.rect.y -= self.velocidad[1]
                self.velocidad[1] -= self.aceleracion
            
            if not (teclado[K_LEFT] or buttonJoy.get_button(13)) and not (teclado[K_RIGHT] or buttonJoy.get_button(14)):
                self.velocidad[0] = 3

            if not (teclado[K_UP] or buttonJoy.get_button(11)) and not (teclado[K_DOWN] or buttonJoy.get_button(12)):
                self.velocidad[1] = -3
        else:
            if not teclado[K_LEFT] and not teclado[K_RIGHT]:
                self.velocidad[0] = 3

            if not teclado[K_UP] and not teclado[K_DOWN]:
                self.velocidad[1] = -3
        
        