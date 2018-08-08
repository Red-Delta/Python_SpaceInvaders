import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))
last_bagduy_spawn_time = 0

badguy_image = pygame.image.load("images/badguy.png").convert()
badguy_image.set_colourkey((0,0,0))

class Badguy:

    def __init__(self):
        self.x =  random.randint(0,520)
        self.y = -100
        self.dy = random.randint(2,6)
        self.dx = random.choice ((-1,1))*self.dy
        
    def move(self):
        
        self.x += self.dx
        self.y += self.dy
        
        #if self.y > 50 and self.y < 150:
           # self.x -=5
        #if self.y > 150 and self.y < 250:
           # self.x +=10
        #if self.y > 250 and self.y < 350:
           # self.x -=10
        #if self.y > 350 and self.y < 450:
           # self.x +=10
        #if self.y > 450 and self.y < 550:
           # self.x -=10
        #if self.y > 550 and self.y < 640:
            #self.x +=10
        
    def draw(self):
        screen.blit(badguy_image,(self.x,self.y))
        
    def bounce(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1
            
    def off_screen(self):
        return self.y > 640
        
badguys = []

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    screen.fill((0,0,0))
    
    # badguy.move()
    # badguy.bounce()
    # badguy.draw()
    
    i = 0
    while i < len(badguys):
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1
    
    pygame.display.update()