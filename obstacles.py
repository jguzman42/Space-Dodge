import pygame
import random
from constants import screenWidth, screenHeight

class Obstacle:
    def __init__(asteroid, screenWidth, screenHeight):

        asteroid.image = pygame.image.load("asteroid_image.png")
        asteroid.rect = asteroid.image.get_rect()

        # Resize the image to a smaller size
        new_width = 100 
        new_height = 100  
        asteroid.image = pygame.transform.scale(asteroid.image, (new_width, new_height))

        #Starting position for asteroids(Above Screen)
        #Max range the asteroid will spawn
        max_x_range = screenWidth
        asteroid.rect.x = random.uniform(1, max_x_range)
        asteroid.rect.y = random.randint(-asteroid.rect.height, -1)

        asteroid.collided = False #New attribute(TESTING)

        #Random Asteroid Speeds
        asteroid.speed = random.randint(2,3)

        # Radius for circular collision detection(TESTING)
        asteroid.radius = new_width // 2  # Assuming the asteroid is roughly circular

    def move(asteroid):

        #Moves asteroids down the screen
        asteroid.rect.y += asteroid.speed

        # Get the original center of the rect
        originalCenter = asteroid.rect.center

        #Set rect center to original center
        asteroid.rect.center = originalCenter

    def draw(asteroid, screen):
        screen.blit(asteroid.image, asteroid.rect)

def generateObstacles(screenWidth, screenHeight, maxAsteroids=4):
    asteroids = []

    #Randomly generates obstacles
    if random.random() < 0.01 and len(asteroids) < maxAsteroids :
        newAsteroids = Obstacle(screenWidth, screenHeight)
        asteroids.append(newAsteroids)

    return asteroids