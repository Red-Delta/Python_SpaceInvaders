import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
xpos = 50
while 1:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT    :
            sys.exit()
    xpos += 1
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,255,0),(150,150),75)
    pygame.display.update()