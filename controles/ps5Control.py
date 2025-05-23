import pygame, time
from pygame.locals import *
from pydualsense import pydualsense, TriggerModes

class Controles(pygame.sprite.Sprite):  # Jugador del control para PS5
    def __init__(self, joystick):
        super().__init__()
        self.joystick = joystick
        self.disparo_delay = 50  # En milisegundos (medio segundo)
        if joystick.get_name() == "DualSense Wireless Controller" and joystick.get_numaxes() > 5:
            self.ds = pydualsense()
            self.ds.init()
    
    def tiempoVibracion(self): # Se activa la vibración por un tiempo
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.setRightMotor(255)
            pygame.time.delay(self.disparo_delay)
            self.ds.setRightMotor(0)
    
    def manterVibracion(self): # Mantiene la vibración
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.setRightMotor(255)
    
    def desactivarManterVibracion(self): # Desactiva mantiene la vibración
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.setRightMotor(0)
    
    def apagarGatillos(self): # Apaga los control completamente
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.triggerL.setMode(TriggerModes.Off)
            self.ds.triggerR.setMode(TriggerModes.Off)
            time.sleep(2)
            self.ds.close()
    
    def desactivarGatillos(self): # Desactiva los gatillos
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.triggerL.setMode(TriggerModes.Off)
            self.ds.triggerR.setMode(TriggerModes.Off)
    
    def pistolaGatillo(self): # Activa el modo pistola
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            # buttonJoy = pygame.joystick.Joystick(0)
            self.ds.triggerR.setForce(1, 200)
            self.ds.triggerR.setForce(2, 110)
            self.ds.triggerR.setForce(3, 30)
            self.ds.triggerR.setMode(TriggerModes.Pulse)
            
    def otroGatillo(self): # Activa el modo otro gatillo
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            self.ds.triggerR.setMode(TriggerModes.Rigid)
            self.ds.triggerR.setForce(1, 200)
    
    def update(self): # Actualiza el estado del control
        if self.joystick.get_name() == "DualSense Wireless Controller" and self.joystick.get_numaxes() > 5:
            buttonJoy = pygame.joystick.Joystick(0)
            empujarR2 = buttonJoy.get_axis(5)  # Empujar R2
            r2_normalized = empujarR2 / 0.9 if empujarR2 > 0 else 0
            r2_normalized = float(min(max(r2_normalized, 0), 1))
            print("Empujar R2: ", r2_normalized)
            if r2_normalized > 0.9:
                print("Disparar")