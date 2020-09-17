# TITLE LOGO AND BACKGROUND COLOR

import pygame

#Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red, Green, Blue
    screen.fill((0, 255, 0)) # plain green color
    pygame.display.update()
