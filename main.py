import pygame
from pygame.locals import *

import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables
saltando = False

imagen = pygame.transform.scale(pygame.image.load("assets/img/player/naveJ1.png"), (65, 60))



cuadrado = imagen.get_rect(center=(WIDTH // 2, HEIGHT // 1.1))
velocidad = [3, -3]
aceleracion = 0.1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

    teclado = pygame.key.get_pressed()
               
    # code here
    
    if teclado[K_LEFT]:
        cuadrado.x -= velocidad[0]
        velocidad[0] += aceleracion
        
    if teclado[K_RIGHT]:
        cuadrado.x += velocidad[0]
        velocidad[0] += aceleracion
    
    if teclado[K_UP]:
        cuadrado.y += velocidad[1]
        velocidad[1] -= aceleracion
        
    if teclado[K_DOWN]:
        cuadrado.y -= velocidad[1]
        velocidad[1] -= aceleracion
        
    if not teclado[K_LEFT] and not teclado[K_RIGHT]:
        velocidad[0] = 3
    
    if not teclado[K_UP] and not teclado[K_DOWN]:
        velocidad[1] = -3
    

    
    # pygame.draw.rect(screen, (255, 255, 255), cuadrado)
    
    screen.blit(imagen, cuadrado)
    
    
    
    pygame.display.update()
    screen.fill((0, 0, 0))
    
    #Ese es para calidad de imagen FPS o HZ (30 es poco duro y 60 es suave)
    clock.tick(60)