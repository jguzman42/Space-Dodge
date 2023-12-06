import pygame
from random import randint
from constants import POWERUPS_IMAGE

class Powerups:
    def __init__(self):
        self.image = pygame.image.load(POWERUPS_IMAGE)
        self.rect = self.image.get_rect()
        #Starting position for obstacles

    def move(self):
        #Obstacles movement
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def generatePowerups():
    #Code that genreates powerups
    pass