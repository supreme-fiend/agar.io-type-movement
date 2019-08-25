"""

Game Development basic project. A character stays in the centre of the screen and the environment moves around him.

Author : Pranay Venkatesh

"""

import pygame


# Basic pygame parameters
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pranay.io")


# Background parameters

bg = pygame.image.load('bg.png')
imgposx = 0
imgposy = 0


# Character Parameters
posx = 250
posy = 250
velocity = 3

def refresh():
    win.fill((0,0,0))
    win.blit(bg, (imgposx, imgposy))
    pygame.draw.circle(win, (255, 0, 0), (250, 250), 10)
    pygame.display.update()

run = True

while run:
    refresh()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if posy > 0:
            posy -= velocity
            imgposy += velocity
    if pressed[pygame.K_DOWN]:
        if posy < 1200:
            posy += velocity
            imgposy -= velocity
    if pressed[pygame.K_LEFT]:
        if posx > 0:
            posx -= velocity
            imgposx += velocity
    if pressed[pygame.K_RIGHT]:
        if posx < 1920:
            posx += velocity
            imgposx -= velocity

exit()
