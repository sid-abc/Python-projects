######### Creating enemy ##########

import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))    

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check wether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
        elif event.key == pygame.K_LEFT:
            playerX_change = -0.3
           
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0                    
    
    playerX += playerX_change
    # Boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()     