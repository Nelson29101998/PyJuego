import pygame
from pygame.locals import *

import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables

teclado = pygame.key.get_pressed()

cuadrado = pygame.Rect(0, HEIGHT//2, 60, 60)
velocidad = [3, -14]
gravedad = 0.4

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("A key has been pressed")
            
    # code here
    cuadrado.x += velocidad[0]
    cuadrado.y += velocidad[1]
    velocidad[1] += gravedad
    pygame.draw.rect(screen, (255, 255, 255), cuadrado)
    
    if cuadrado.y > HEIGHT-60:
        velocidad[1] = 0
        gravedad = 0

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)