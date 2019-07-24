import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))
last_bagduy_spawn_time = 0

score = 0

shots = 0
hits = 0
misses = 0

font = pygame.font.Font(None,20)

badguy_image = pygame.image.load("images/badguy.png").convert()
badguy_image.set_colorkey((0,0,0))

fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))

missile_image = pygame.image.load("images/missile.png").convert()
missile_image.set_colorkey((255,255,255))

GAME_OVER = pygame.image.load("images/gameover.png").convert()

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

    def touching(self,missile):
        return (self.x+35-missile.x)**2+(self.y+22-missile.y)**2 <1225

    def score(self):
        global score
        score+=100
                
badguys = []

class Fighter:
    def __init__(self):
        self.x = 320

    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -=3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x +=3

    def draw(self):
        screen.blit(fighter_image,(self.x,591))

    def fire(self):
        global shots
        shots+=1
        missiles.append(Missile(self.x+50))
        

    def hit_by(self,badguy):
        return (
                badguy.y > 585 and 
                badguy.x > self.x - 55 and 
                badguy.x < self.x + 85
                )   


class Missile:
    def __init__(self,x):
        self.x = x
        self.y = 591

    def move(self):
        self.y -= 5

    def off_screen(self):
        return self.y < -8

    def draw(self):
        screen.blit(missile_image,(self.x-4,self.y))
   

missiles = []

fighter = Fighter()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            fighter.fire()
            time.wait(0.5)
            if event.type == KEYDOWN and event.key == K_SPACE:
                fighter.fire()
            
                        
    pressed_keys = pygame.key.get_pressed()    

    if time.time() - last_bagduy_spawn_time > 0.5:
        badguys.append(Badguy())
        last_bagduy_spawn_time = time.time()

    screen.fill((0,0,0))
    
    fighter.move()
    fighter.draw()

    
    i = 0
    while i < len(badguys):
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1
    
    i = 0
    while i < len(missiles):
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].off_screen():
            del missiles[i]
            misses += 1
            i -= 1
        i += 1

    i = 0
    while i <len(badguys):
        j = 0
        while j < len(missiles):
            if badguys[i].touching(missiles[j]):
                badguys[i].score()
                hits += 1
                del badguys[i]
                del missiles[j]
                i -= 1
                break
            j += 1
        i += 1
    
    screen.blit(font.render("Score: "+str(score),True,(255,255,255)),(5,5))

    for badguy in badguys:
        if fighter.hit_by(badguy):
            screen.blit(GAME_OVER,(170,200))

            screen.blit(font.render(str(shots),True,(255,255,255)),(266,320))
            screen.blit(font.render(str(score),True,(255,255,255)),(266,348))
            screen.blit(font.render(str(hits),True,(255,255,255)),(400,320))
            if misses + hits != shots:
                screen.blit(font.render(str(shots-hits),True,(255,255,255)),(400,337))
            else:
                screen.blit(font.render(str(misses),True,(255,255,255)),(400,337))
            
            if shots == 0:
                screen.blit(font.render("--",True(255,255,255)),(400,357))
            else:
                screen.blit(font.render(str((1000*hits/shots)/10.)+"%",True,(255,255,255)),(400,357))

            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                    
                pygame.display.update()



    pygame.display.update()