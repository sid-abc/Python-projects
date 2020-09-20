######### Enemy movements ##########

import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

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
enemyX_change = 4
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))    

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0,0,0))
    # Background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check wether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        elif event.key == pygame.K_LEFT:
            playerX_change = -5
           
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0                    
    
    playerX += playerX_change
    # Boundries of player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change        
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
