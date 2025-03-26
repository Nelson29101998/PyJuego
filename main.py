import pygame
from pygame.locals import *

from personajes import player

import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()

jugador = player.Jugador(WIDTH // 2, HEIGHT // 1.1)
player_group.add(jugador)

# constants


# variables

# fondoPantalla = pygame.image.load("assets/img/fondo/galaxia.jpg")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

    # code here

    # screen.blit(fondoPantalla, (0, 0))
    # screen.blit(imagen, cuadrado)

    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()
    screen.fill((0, 0, 0))

    # Ese es para calidad de imagen FPS o HZ (30 es poco duro y 60 es suave)
    clock.tick(60)
