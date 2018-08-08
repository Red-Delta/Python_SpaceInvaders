import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Python Book Testing")
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
rain_y = 0
rain_x = 400

while 1:
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT    :
            sys.exit()
    screen.fill((255,255,255))
    rain_y +=4
    pygame.draw.line(screen,(0,0,0),(rain_x,rain_y),(rain_x,rain_y+5),1)

    pygame.display.update()