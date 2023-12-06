import pygame
import random
from spaceship import Spaceship
#from powerups import Powerups, generatePowerups
from obstacles import Obstacle, generateObstacles
from constants import screenWidth, screenHeight, titleScreen
from highscore import addScore, getHighScores, updateHighScores, displayScore, saveHighScores, loadHighScores

pygame.init()
loadHighScores()

#Window for Launch Screen
launchScreen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Dodge")

#Loads launch screen background and start button
launchBackground = pygame.image.load("star_image.jpg")
launchBackground = pygame.transform.scale(launchBackground, (screenWidth, screenHeight))
startButton = pygame.image.load("startbtn_image.png")

#Get rect of the start button
button_rect = startButton.get_rect()

# Set the title of the game
title_font = pygame.font.Font(None, 36)
title_text = title_font.render("Space Dodge: Python Edition", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(screenWidth // 2, screenHeight // 4))

#Main loop for launch screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Checks left mouse button
            #Checks if button is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_rect = startButton.get_rect(center=(screenWidth // 2, screenHeight // 2))
            if button_rect.collidepoint(mouse_x, mouse_y):
                running = False

    launchScreen.blit(launchBackground, (0,0))
    launchScreen.blit(title_text, title_rect)
    launchScreen.blit(startButton, (screenWidth // 2 - button_rect.width // 2, screenHeight // 2))
    pygame.display.flip()

score = 0
playerSpaceship = Spaceship()

#Game Window
gameScreen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(titleScreen)

#Background Image loaded to fit entire game screen
backgroundImage = pygame.image.load("star_image.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (700,700))
gameScreen.blit(backgroundImage, (0, 0))

#Game Over Screen
gameOverScreen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game Over")

gameOverBackground = pygame.image.load("star_image.jpg")
gameOverBackground = pygame.transform.scale(gameOverBackground, (screenWidth, screenHeight))

#Load exit button image
exitButton = pygame.image.load("exitbtn_image.png")

exit_button_width = 100
exit_button_height = 50

#Resize button
exitButton = pygame.transform.scale(exitButton, (exit_button_width, exit_button_height))

#List to store asteroids
asteroids = []

#Players Lives
lives = 3

def check_collision(spaceship, asteroid):
    if not asteroid.collided:  # Check if the asteroid has not already collided
        distance = pygame.math.Vector2(spaceship.rect.center) - pygame.math.Vector2(asteroid.rect.center)
        if distance.length() < spaceship.radius + asteroid.radius:
            asteroid.collided = True
            return True
    return False

#Main Game Loop
running = True
asteroids = generateObstacles(screenWidth, screenHeight, maxAsteroids=4)
while running and lives > 0: #Exit loop if lives reaches zero
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Clears screen with black background
    gameScreen.fill((0,0,0))

    #Draws Background image
    gameScreen.blit(backgroundImage, (0,0))

    #Game elements and drawing them
    playerSpaceship.move()
    playerSpaceship.draw(gameScreen)

    # Generate new asteroids only if the current ones are almost off the screen
    if all(asteroid.rect.y > screenHeight * 0.9 for asteroid in asteroids):
        newAsteroids = generateObstacles(screenWidth, screenHeight, maxAsteroids=4)
        asteroids.extend(newAsteroids)

    #Generate Asteroids
    newAsteroids = generateObstacles(screenWidth, screenHeight, maxAsteroids=4)
    asteroids.extend(newAsteroids)

    #Move and Draw Asteroids
    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw(gameScreen)

    #Remove asteroids that are off screen
    asteroids = [asteroid for asteroid in asteroids if asteroid.rect.y < screenHeight]

    # Check for collision with spaceship
    for asteroid in asteroids:
        if check_collision(playerSpaceship, asteroid):
            asteroid.collided = True
            lives -= 1  # Decrement lives

            # Remove the collided asteroid from the list
            asteroids.remove(asteroid)

            # Respawn spaceship if lives remain
            if lives > 0:
                playerSpaceship = Spaceship()

    # Check if any asteroid has gone off the screen
    for asteroid in asteroids:
        if asteroid.rect.bottom >= screenHeight:
            #Increment the score and remove the asteroid
            asteroid.rect.y = random.randint(-50, -10)
            score += 10
            asteroids.remove(asteroid)


    #Display Score
    displayScore(gameScreen, score, lives, screenWidth)

    # Generate new asteroids
    newAsteroids = generateObstacles(screenWidth, screenHeight, maxAsteroids=4)
    asteroids.extend(newAsteroids)

    #Update the display
    pygame.display.flip()

    # Clock tick to control the frame rate
    pygame.time.Clock().tick(160)

#Game Over Loop
if lives <= 0:
    game_over = True

    exitButtonRect = exitButton.get_rect(center=(screenWidth // 2, screenHeight // 2))
    exitButtonRect.y += 100

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the exit button is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if exitButtonRect.collidepoint(mouse_x, mouse_y):
                    game_over = False

        # Display the game over background
        gameOverScreen.blit(gameOverBackground, (0, 0))

        # Display the game over message
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screenWidth // 2, screenHeight // 10))
        gameOverScreen.blit(text, text_rect)

        # Display the exit button
        gameOverScreen.blit(exitButton, exitButtonRect)

        # Display the leaderboard
        #font = pygame.font.Font(None, 24)
        #leaderboard_text = font.render("Leaderboard:", True, (255, 255, 255))
        #leaderboard_rect = leaderboard_text.get_rect(center=(screenWidth // 2, screenHeight // 6))
        #gameOverScreen.blit(leaderboard_text, leaderboard_rect)

        # Get the high scores
        high_scores = getHighScores()

        # Display each high score
        #for i, (player_name, score) in enumerate(high_scores):
            #score_text = font.render(f"{i + 1}. {player_name}: {score}", True, (255, 255, 255))
            #score_rect = score_text.get_rect(center=(screenWidth // 2, screenHeight // 5 + i * 30))
            #gameOverScreen.blit(score_text, score_rect)

        pygame.display.flip()

    #Update High Score
    #updateHighScores(player_name, score)

#Quit pygame and exit
pygame.quit()