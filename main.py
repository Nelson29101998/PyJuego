import pygame, time, sys
from pygame.locals import *

from personajes import player
from armas import canonLaser
from fondos import fondoPantalla

from pydualsense import pydualsense, TriggerModes

def main():
    pygame.init()

    pygame.joystick.init()

    # ! No ponga el comentario en la linea 11 ni borrar
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        joystick.init()
        ds = pydualsense()
        ds.init()

    disparo_delay = 500 # Tiempo de espera entre disparos en milisegundos
    ultimo_disparo = pygame.time.get_ticks()
    
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player_group = pygame.sprite.Group()

    fondo_group = pygame.sprite.Group()

    jugador = player.Jugador("assets/img/player/naveJ1.png", WIDTH, HEIGHT)
    # posX, posY = jugador.getPosicion()
    # laser = canonLaser.Laser((255, 0, 0), posX, posY)
    fondo = fondoPantalla.Pantalla("assets/img/fondo/galaxia.jpg", [0, 0])
    player_group.add(jugador)
    # player_group.add(laser)
    fondo_group.add(fondo)

    trigger_forces = {}

    # Establecer las fuerzas
    trigger_forces[1] = 0  # Fuerza en el punto 1
    trigger_forces[2] = 80  # Fuerza en el punto 2
    trigger_forces[3] = 200  # Fuerza en el punto 3

    # La maquina de Update con While
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                for joystick in joysticks:
                    joystick.quit()
                    ds.close()
                pygame.joystick.quit()
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 9:
                    jugador.teletransporte("izquierda")
                    # if pygame.joystick.get_count() > 0:
                    #     ds.setLeftMotor(255)
                    #     time.sleep(2)
                    #     ds.setLeftMotor(0)

                if event.button == 10:
                    jugador.teletransporte("derecha")
                    # if pygame.joystick.get_count() > 0:
                    #     ds.setRightMotor(255)
                    #     time.sleep(2)
                    #     ds.setRightMotor(0)

        if pygame.joystick.get_count() > 0:
            buttonJoy = pygame.joystick.Joystick(0)
            if buttonJoy.get_button(0):  # Botón "X"
                ds.triggerL.setMode(TriggerModes.Rigid)
                ds.triggerL.setForce(1, 200)
                print("Gatillo izquierdo configurado en modo rígido.")
            elif buttonJoy.get_button(1):  # Botón "O"
                ds.triggerL.setForce(1, 200)
                ds.triggerL.setForce(2, 110)
                ds.triggerL.setForce(3, 30)
                ds.triggerL.setMode(TriggerModes.Pulse)
            elif buttonJoy.get_button(2):  # Botón "Cuadrado"
                ahora = pygame.time.get_ticks()
                if ahora - ultimo_disparo >= disparo_delay:
                    ds.setLeftMotor(255)
                    posX, posY = jugador.getPosicion()
                    laser = canonLaser.Laser((255, 0, 0), posX, posY)
                    player_group.add(laser)
                    ultimo_disparo = ahora
            else:
                ds.triggerL.setMode(TriggerModes.Off)
                ds.setLeftMotor(0)

        # code here

        fondo_group.draw(screen)
        fondo_group.update()

        player_group.draw(screen)
        player_group.update()

        pygame.display.flip()
        screen.fill((0, 0, 0))

        # Ese es para calidad de imagen FPS o HZ (30 es poco duro y 60 es suave)
        clock.tick(60)

if __name__ == "__main__":
    main()