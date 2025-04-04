import pygame
from pygame.locals import *

class Jugador(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, image_file,  x, y):
        super().__init__()
        self.limitePantallaX, self.limitePantallaY = x, y
        x, y = x // 2, y // 1.1 # Posicion inicial del jugador
        self.velocidad = [7, -7]
        self.teletrans = [5, -5]
        image_file = pygame.image.load(image_file).convert_alpha()
        original_width, original_height = image_file.get_size()
        scale_factor = 0.1

        # Calcular el nuevo tamaño manteniendo las proporciones
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        self.image = pygame.transform.scale(image_file, (new_width, new_height))
        self.rect = self.image.get_rect(center=(x, y))
        
    def getPosicion(self):
        return self.rect.x, self.rect.y
    
    def limitePantalla(self):
        self.maxArriba, self.maxAbajo, self.maxIzquierda, self.maxDerecha = 370, self.limitePantallaY, 0, self.limitePantallaX # Limite superior
        if self.rect.top < self.maxArriba:  # Limitar para que no salga por arriba
                self.rect.top = self.maxArriba
        
        if self.rect.bottom > self.maxAbajo:  # Limitar para que no salga por abajo
                self.rect.bottom = self.maxAbajo
        
        if self.rect.left < self.maxIzquierda:  # Limitar para que no salga por la izquierda
                self.rect.left = self.maxIzquierda
        
        if self.rect.right > self.maxDerecha:  # Limitar para que no salga por la derecha
                self.rect.right = self.maxDerecha
        
        
    def teletransporte(self, salto):
        if salto == "izquierda":
            self.rect.x -= self.teletrans[0] * 40
        elif salto == "derecha":
            self.rect.x += self.teletrans[0] * 40
        
        self.limitePantalla()  # Limitar el movimiento del jugador a la pantalla

    def mover(self, donde, NumMovimiento=1):
        NumMovimiento = NumMovimiento * -1 if NumMovimiento < 0 else NumMovimiento

        if donde == "arriba":
            self.rect.y += self.velocidad[1] * NumMovimiento

        elif donde == "abajo":
            self.rect.y -= self.velocidad[1] * NumMovimiento

        elif donde == "izquierda":
            self.rect.x -= self.velocidad[0] * NumMovimiento

        elif donde == "derecha":
            self.rect.x += self.velocidad[0] * NumMovimiento
        
        self.limitePantalla()  # Limitar el movimiento del jugador a la pantalla
        
        # print("Posicion Jugador: X: ", self.rect.x, " Y: ", self.rect.y)


    def update(self):
        # Los botones del teclado
        teclado = pygame.key.get_pressed()

        if teclado[K_LEFT] or teclado[K_a]:  # Si se presiona la tecla izquierda o el boton 13 del joystick
            self.mover("izquierda")

        if teclado[K_RIGHT] or teclado[K_d]:  # Si se presiona la tecla derecha o el boton 14 del joystick
            self.mover("derecha")

        if teclado[K_UP] or teclado[K_w]:  # Si se presiona la tecla arriba o el boton 11 del joystick
            self.mover("arriba")

        if teclado[K_DOWN] or teclado[K_s]:  # Si se presiona la tecla abajo o el boton 12 del joystick
            self.mover("abajo")

        # Los botones del joystick
        if pygame.joystick.get_count() > 0:
            buttonJoy = pygame.joystick.Joystick(0)
            ejeXL3 = float(buttonJoy.get_axis(0))  # Eje X L3
            ejeYL3 = float(buttonJoy.get_axis(1))  # Eje Y L3

            ejeXR3 = float(buttonJoy.get_axis(2))  # Eje X R3
            ejeYR3 = float(buttonJoy.get_axis(3))  # Eje Y R3

            if ejeXL3 < -0.2:
                self.mover("izquierda", ejeXL3 * 1.5)

            if ejeXL3 > 0.2:
                self.mover("derecha", ejeXL3 * 1.5)

            if ejeYL3 < -0.2:
                self.mover("arriba", ejeYL3 * 1.5)

            if ejeYL3 > 0.2:
                self.mover("abajo", ejeYL3 * 1.5)

            # empujarL2 = buttonJoy.get_axis(4)  # Empujar L2
            # empujarR2 = buttonJoy.get_axis(5)  # Empujar R2
            # l2_normalized = empujarL2 / 0.9 if empujarL2 > 0 else 0
            # r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0

            # l2_normalized = float(min(max(l2_normalized, 0), 1))
            # r2_normalized = float(min(max(r2_normalized, 0), 1))

            # print("Empujar L2: ", l2_normalized , ", Empujar R2: ", r2_normalized)

            # Si se presiona la tecla izquierda o el boton 13 del joystick
            if buttonJoy.get_button(13):
                self.mover("izquierda")

            # Si se presiona la tecla derecha o el boton 14 del joystick
            if buttonJoy.get_button(14):
                self.mover("derecha")

            # Si se presiona la tecla arriba o el boton 11 del joystick
            if buttonJoy.get_button(11):
                self.mover("arriba")

            # Si se presiona la tecla abajo o el boton 12 del joystick
            if buttonJoy.get_button(12):
                self.mover("abajo")
