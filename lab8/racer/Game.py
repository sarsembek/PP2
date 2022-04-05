import pygame, sys
from pygame.locals import *
import random, time
#i have used path to extract files
path='C:\\Users\\777\\Desktop\pp2\lab8\\racer\\'
pygame.init()
#settings for display,color,fps and etc
FPS = 60
FramePerSec = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 2
SCORE = 0
#initializing font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
#loading background
background = pygame.image.load(path+"AnimatedStreet.png")
dy=0
#setting display and caption
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
#creating class for enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
#function to move opposite to the player
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#creating class for enemy
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
#function to move player image with move_ip
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
#creating first player and enemy
P1 = Player()
E1 = Enemy()
#defining sprites and adding
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
#new user event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
#setting music
pygame.mixer.music.load(path+'background.wav')
pygame.mixer.music.play(-122)
#setting coins
score_coins=0
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(path+'coin.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40), 0)
    def move(self):
        global score_coins
        global P1
        self.rect.move_ip(0, SPEED)
        if(self.rect.bottom>600 or pygame.sprite.collide_rect(P1, self)):
            score_coins+=1
            self.rect.top=0
            self.rect.center=(random.randint(40,SCREEN_WIDTH-40), 0)
C1=coin()
coins=pygame.sprite.Group()
coins.add(C1)
#main loop
while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#infinite scrolling
    rel_dy=dy%background.get_rect().height
    DISPLAYSURF.blit(background, (0,rel_dy-background.get_rect().height))
    if rel_dy<SCREEN_HEIGHT:
        DISPLAYSURF.blit(background,(0,rel_dy))
    dy+=1
#moving in main loop
    for value in coins:
        value.move()
        DISPLAYSURF.blit(value.image, value.rect)
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
#showing score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    SCORE_COINS=font_small.render(str(score_coins), True, BLACK)
    DISPLAYSURF.blit(SCORE_COINS, (370,10))
#finding any collide between sprites
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(path+'crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
