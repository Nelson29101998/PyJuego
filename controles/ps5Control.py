import pygame, time
from pygame.locals import *
from pydualsense import pydualsense, TriggerModes

class Controles(pygame.sprite.Sprite):  # Jugador del control para PS5
    def __init__(self):
        super().__init__()
        if pygame.joystick.get_count() > 0:
            self.ds = pydualsense()
            self.ds.init()
    
    def apagarGatillos(self):
        if pygame.joystick.get_count() > 0:
            self.ds.triggerL.setMode(TriggerModes.Off)
            self.ds.triggerR.setMode(TriggerModes.Off)
            time.sleep(2)
            self.ds.close()
    
    def desactivarGatillos(self):
        if pygame.joystick.get_count() > 0:
            self.ds.triggerL.setMode(TriggerModes.Off)
            self.ds.triggerR.setMode(TriggerModes.Off)
    
    def pistolaGatillo(self):
        if pygame.joystick.get_count() > 0:
            self.ds.triggerR.setForce(1, 200)
            self.ds.triggerR.setForce(2, 110)
            self.ds.triggerR.setForce(3, 30)
            self.ds.triggerR.setMode(TriggerModes.Pulse)
    
    def update(self):
        pass