import pygame
from pygame.locals import *

import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables
saltando = False

cuadrado = pygame.Rect(0, HEIGHT//2, 60, 60)
velocidad = [3, -14]
saltar_HEIGHT = 20
gravedad = 0.4

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

    teclado = pygame.key.get_pressed()
    
    if teclado[K_SPACE]:
        saltando = True
        print("A key has been pressed")
               
    # code here
    
    if saltando:
        if cuadrado.y < -saltar_HEIGHT:
            cuadrado.y -= velocidad[1]
            saltando = False
            # cuadrado.y = saltar_HEIGHT
        elif cuadrado.y > -saltar_HEIGHT:
            cuadrado.y += velocidad[1]
            saltando = False
        velocidad[1] += gravedad
    
    
    cuadrado.x += velocidad[0]
    # cuadrado.y += velocidad[1]
    # velocidad[1] += gravedad
    pygame.draw.rect(screen, (255, 255, 255), cuadrado)
    
    if cuadrado.y > HEIGHT-60:
        velocidad[1] = 0
        gravedad = 0

    pygame.display.update()
    screen.fill((0, 0, 0))
    
    #Ese es para calidad de imagen FPS o HZ (30 es poco duro y 60 es suave)
    clock.tick(60)