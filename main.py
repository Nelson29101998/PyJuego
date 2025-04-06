import pygame, time, sys
from pygame.locals import *

from personajes import player
from armas import canonLaser
from fondos import fondoPantalla
from controles import ps5Control

def cambioArmas(numCambiar, ps5Ctl): # Cambia el modo de los gatillos según el número
    buttonJoy = pygame.joystick.Joystick(0)
    
    match numCambiar:
        case 0:
            print("Hola 0")
            ps5Control.desactivarGatillos()
        case 1:
            ps5Ctl.pistolaGatillo()
            empujarR2 = buttonJoy.get_axis(5)  # Empujar R2
            r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0
            r2_normalized = float(min(max(r2_normalized, 0), 1))
            
            if r2_normalized == 1.0:
               return "fase1R2"

        case 2:
            print("Hola 2")
        case 3:
            print("Hola 3")
        case 4:
            print("Hola 4")
        case 5:
            print("Hola 5")
        case 6:
            print("Hola 6")
        case 7:
            print("Hola 7")
        case 8:
            print("Hola 8")
        case 9:
            print("Hola 9")
        case 10:
            print("Hola 10")

def disparar_laser(jugador, player_group, lasers_temporales, ultimo_disparo, disparo_delay):
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_disparo >= disparo_delay:
        # Obtener posición del jugador
        posX, posY = jugador.getPosicion()
        # Crear el láser
        laser = canonLaser.Laser((255, 0, 0), posX, posY)
        # Añadir el láser al grupo
        player_group.add(laser)
        # Registrar tiempo de vida del láser
        lasers_temporales.append((laser, ahora + 3000))  # Tiempo de vida de 3 segundos
        # Actualizar el último disparo
        return ahora  # Devolver el tiempo actual para actualizar "ultimo_disparo"
    
    return ultimo_disparo  # Mantener el tiempo anterior si no se disparó

def main():
    pygame.init()

    pygame.joystick.init()

    # ! No ponga el comentario en la linea 11 ni borrar
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        joystick.init()

    disparo_delay = 500  # En milisegundos (medio segundo)
    ultimo_disparo = pygame.time.get_ticks()
    lasers_temporales = [] # Lista para almacenar los láseres temporales
    
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player_group = pygame.sprite.Group()

    fondo_group = pygame.sprite.Group()

    jugador = player.Jugador("assets/img/player/naveJ1.png", WIDTH, HEIGHT)
    fondo = fondoPantalla.Pantalla("assets/img/fondo/galaxia.jpg", [0, 0])
    ps5Ctl = ps5Control.Controles()
    player_group.add(jugador)
    fondo_group.add(fondo)
    
    numero = 0

    # La maquina de Update con While
    while True:
        fases = cambioArmas(numero, ps5Ctl)
        teclado = pygame.key.get_pressed()
        ahora = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                for joystick in joysticks:
                    # apagarGatillos(ds)
                    ps5Ctl.apagarGatillos()
                    # time.sleep(2) # Esperar 2 segundos antes de cerrar
                    joystick.quit()
                    # ds.close()
                pygame.joystick.quit()
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 9:
                    # jugador.teletransporte("izquierda")
                    numero += 1
                    if numero > 10:
                        numero = 10
                  
                if event.button == 10:
                    # jugador.teletransporte("derecha")
                    numero -= 1
                    if numero < 0:
                        numero = 0
                
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 5 and fases == "fase1R2":
                    if event.value == 1.0:
                        ultimo_disparo = disparar_laser(jugador, player_group, lasers_temporales, ultimo_disparo, disparo_delay)
                        

        if teclado[K_RETURN]:
            ultimo_disparo = disparar_laser(jugador, player_group, lasers_temporales, ultimo_disparo, disparo_delay)
        
        if pygame.joystick.get_count() > 0:
            buttonJoy = pygame.joystick.Joystick(0)
            if buttonJoy.get_button(0):  # Botón "X"
                # ds.triggerL.setMode(TriggerModes.Rigid)
                # ds.triggerL.setForce(1, 200)
                print("Gatillo izquierdo configurado en modo rígido.")
            elif buttonJoy.get_button(1):  # Botón "O"
                print("Botón O presionado.")
            elif buttonJoy.get_button(2):  # Botón "Cuadrado"
                ultimo_disparo = disparar_laser(jugador, player_group, lasers_temporales, ultimo_disparo, disparo_delay)
            
                
        for laser_obj, tiempo in lasers_temporales[:]:  # Iterar sobre una copia de la lista
            if ahora >= tiempo:
                if laser_obj in player_group:
                    player_group.remove(laser_obj)
                lasers_temporales.remove((laser_obj, tiempo))

       

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