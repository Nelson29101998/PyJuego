import pygame, sys
from pygame.locals import *

from personajes import player
from fondos import fondoPantalla

pygame.init()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())] #! No ponga el comentario en la linea 11 ni borrar
for joystick in joysticks:
    joystick.init()    

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()

fondo_group = pygame.sprite.Group()

jugador = player.Jugador("assets/img/player/naveJ1.png", WIDTH // 2, HEIGHT // 1.1)
fondo = fondoPantalla.Pantalla("assets/img/fondo/galaxia.jpg", [0,0])
player_group.add(jugador)
fondo_group.add(fondo)

# La maquina de Update con While
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            for joystick in joysticks:
                joystick.quit()
            pygame.joystick.quit()
            pygame.quit()
            quit()
            sys.exit()
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 9:
                jugador.teletransporte("izquierda")
            if event.button == 10:
                jugador.teletransporte("derecha")
        
    # code here
    
    fondo_group.draw(screen)
    fondo_group.update()

    player_group.draw(screen)
    player_group.update()
    
    pygame.display.flip()
    screen.fill((0, 0, 0))

    # Ese es para calidad de imagen FPS o HZ (30 es poco duro y 60 es suave)
    clock.tick(60)
