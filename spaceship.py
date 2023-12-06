import pygame
from constants import screenWidth, screenHeight

class Spaceship:
    def __init__(spaceship):
        spaceship.image = pygame.image.load("spaceship_image.png")
        spaceship.rect = spaceship.image.get_rect()

        #Spaceship starting position
        spaceship.rect.x = 350
        spaceship.rect.y = 300

        #New Height and Width for the smaller spaceship
        new_width = 50
        new_height = 50

        #Scale down the image
        spaceship.image = pygame.transform.scale(spaceship.image, (new_width, new_height))

        #Speed the spaceship will move at
        spaceship.speed = 2

        # Radius for circular collision detection
        spaceship.radius = new_width // 2  # Assuming the spaceship is roughly circular

    def move(spaceship):
        #Calculates time between frames for consistent movement speed
        dt = pygame.time.Clock().tick(160) / 1000.0

        #Spaceships WASD and Arrow Key movement
        keys =pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            spaceship.rect.y -= spaceship.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            spaceship.rect.x -= spaceship.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            spaceship.rect.y += spaceship.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            spaceship.rect.x += spaceship.speed
        
    def draw(spaceship, screen):
        screen.blit(spaceship.image, spaceship.rect)