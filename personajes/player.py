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

    def mover(self, donde, NumMovimiento=1):
        if donde == "arriba":
            self.rect.y += self.velocidad[1] 
            self.velocidad[1] -= self.aceleracion
        elif donde == "abajo":
            self.rect.y -= self.velocidad[1]
            self.velocidad[1] -= self.aceleracion
        elif donde == "izquierda":
            self.rect.x -= self.velocidad[0]
            self.velocidad[0] += self.aceleracion
        elif donde == "derecha":
            self.rect.x += self.velocidad[0]
            self.velocidad[0] += self.aceleracion
    
    def update(self):
        #Los botones del teclado
        teclado = pygame.key.get_pressed()
        
        if teclado[K_LEFT]: #Si se presiona la tecla izquierda o el boton 13 del joystick
            self.mover("izquierda")

        if teclado[K_RIGHT]: #Si se presiona la tecla derecha o el boton 14 del joystick
            self.mover("derecha")

        if teclado[K_UP]: #Si se presiona la tecla arriba o el boton 11 del joystick
            self.mover("arriba")

        if teclado[K_DOWN]: #Si se presiona la tecla abajo o el boton 12 del joystick
            self.mover("abajo")
        
        #Los botones del joystick
        if pygame.joystick.get_count() > 0:      
            buttonJoy = pygame.joystick.Joystick(0)
            ejeXL3 = float(buttonJoy.get_axis(0)) #Eje X L3
            ejeYL3 = float(buttonJoy.get_axis(1))#Eje Y L3
            # print("Eje X L3: ", ejeXL3 , ", Eje Y L3: ", ejeYL3)
            
            ejeXR3 = float(buttonJoy.get_axis(2))  #Eje X R3
            ejeYR3 = float(buttonJoy.get_axis(3)) #Eje Y R3
            print(f"L3: X={ejeXL3:.2f}, Y={ejeYL3:.2f} | R3: X={ejeXR3:.2f}, Y={ejeYR3:.2f}")
            
            if ejeXL3 < -0.5:
                self.mover("izquierda", ejeXL3)
                
            if ejeXL3 > 0.5:
                self.mover("derecha", ejeXL3)
                
            if ejeYL3 < -0.5:
                self.mover("arriba", ejeYL3)
                
            if ejeYL3 > 0.5:
                self.mover("abajo", ejeYL3)

            empujarL2 = buttonJoy.get_axis(4) #Empujar L2
            empujarR2 = buttonJoy.get_axis(5) #Empujar R2
            l2_normalized = empujarL2 / 0.9 if empujarL2 > 0 else 0
            r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0
            
            l2_normalized = float(min(max(l2_normalized, 0), 1))
            r2_normalized = float(min(max(r2_normalized, 0), 1))
            
            # print("Empujar L2: ", l2_normalized , ", Empujar R2: ", r2_normalized)
            
            if buttonJoy.get_button(13): #Si se presiona la tecla izquierda o el boton 13 del joystick
                self.mover("izquierda")
            
            if buttonJoy.get_button(14): #Si se presiona la tecla derecha o el boton 14 del joystick
                self.mover("derecha")
            
            if buttonJoy.get_button(11): #Si se presiona la tecla arriba o el boton 11 del joystick
                self.mover("arriba")
            
            if buttonJoy.get_button(12): #Si se presiona la tecla abajo o el boton 12 del joystick
                self.mover("abajo")
            
            if not (teclado[K_LEFT] or buttonJoy.get_button(13)) and not (teclado[K_RIGHT] or buttonJoy.get_button(14)):
                self.velocidad[0] = 3

            if not (teclado[K_UP] or buttonJoy.get_button(11)) and not (teclado[K_DOWN] or buttonJoy.get_button(12)):
                self.velocidad[1] = -3
        else:
            if not teclado[K_LEFT] and not teclado[K_RIGHT]:
                self.velocidad[0] = 3

            if not teclado[K_UP] and not teclado[K_DOWN]:
                self.velocidad[1] = -3
        
        