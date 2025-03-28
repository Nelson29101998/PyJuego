import pygame
from pygame.locals import *


class Jugador(pygame.sprite.Sprite):  # Jugador de la Nave
    def __init__(self, image_file,  x, y):
        super().__init__()
        self.aceleracion = 0.1
        self.velocidad = [7, -7]
        self.image = pygame.transform.scale(
            pygame.image.load(image_file).convert_alpha(), (95, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.topleft = (x, y)

    def mover(self, donde, NumMovimiento=1):
        # if NumMovimiento < 0:
        NumMovimiento = NumMovimiento * -1 if NumMovimiento < 0 else NumMovimiento

        print("Movimiento: ", donde, NumMovimiento)
        if donde == "arriba":
            self.rect.y += self.velocidad[1] * NumMovimiento
        elif donde == "abajo":
            self.rect.y -= self.velocidad[1] * NumMovimiento
        elif donde == "izquierda":
            self.rect.x -= self.velocidad[0] * NumMovimiento
        elif donde == "derecha":
            self.rect.x += self.velocidad[0] * NumMovimiento

    def update(self):
        # Los botones del teclado
        teclado = pygame.key.get_pressed()

        if teclado[K_LEFT]:  # Si se presiona la tecla izquierda o el boton 13 del joystick
            self.mover("izquierda")

        if teclado[K_RIGHT]:  # Si se presiona la tecla derecha o el boton 14 del joystick
            self.mover("derecha")

        if teclado[K_UP]:  # Si se presiona la tecla arriba o el boton 11 del joystick
            self.mover("arriba")

        if teclado[K_DOWN]:  # Si se presiona la tecla abajo o el boton 12 del joystick
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

            empujarL2 = buttonJoy.get_axis(4)  # Empujar L2
            empujarR2 = buttonJoy.get_axis(5)  # Empujar R2
            l2_normalized = empujarL2 / 0.9 if empujarL2 > 0 else 0
            r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0

            l2_normalized = float(min(max(l2_normalized, 0), 1))
            r2_normalized = float(min(max(r2_normalized, 0), 1))

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
