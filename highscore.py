import pygame
import os

pygame.font.init()

#Font that will be used to display the score
font = pygame.font.Font(None, 30)

#Initialize an empty list for high score
highScores = []

# File path to save/load high scores
HIGHSCORES_FILE = "highscores.txt"

def saveHighScores():
    file_path = os.path.abspath(HIGHSCORES_FILE)

    with open(HIGHSCORES_FILE, "w") as file:
        for playerName, score in highScores:
            file.write(f"{playerName},{score}\n")

def loadHighScores():

    global highScores  # Add this line to access the global variable
    highScores = []  # Clear the list before loading scores from the file

    if os.path.exists(HIGHSCORES_FILE):
        with open(HIGHSCORES_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                playerName, score = line.strip().split(',')
                highScores.append((playerName, int(score)))

#Function that adds players score to the high scores list
def addScore(playerName, score):
    global highScores

    for i, (name, _) in enumerate(highScores):
        if name == playerName:
            # Update the score if the player exists
            highScores[i] = (playerName, score)
            break
    else:
        #If a player doesnt exist add a new entry
        highScores.append((playerName, score))

#Function to get the top high scores
def getHighScores():
    return sorted(highScores, key = lambda x: x[1], reverse = True)

#Function to update the high scores if a player gets a new high score
def updateHighScores(playerName, score):
    print(f"Updating high scores for {playerName} with score {score}")
    addScore(playerName, score)

    #Limits high score list to top 10 scores
    highScores.sort(key = lambda x: x[1], reverse = True)
    if len(highScores) > 10:
        highScores.pop()

    saveHighScores()

#Function to display the players score on screen
def displayScore(screen, score, lives, screenWidth):
    text = font.render(f"Score: {score}", True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text, (10,10)) #Score in top left corner

    #Display Lives
    livesText = font.render(f"Lives: {lives}", True, (255,255,255))
    screen.blit(livesText,(screenWidth - 150,10))