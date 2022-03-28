import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
clock=pygame.time.Clock()
done=False
white=(255,255,255)
red=(255,0,0)
screen.fill(white)
step=20
x=100
y=100
pygame.draw.circle(screen,red,(x,y),25)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            if y+step<400:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x,y+step), 25)
                y+=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            if y-step>0:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x,y-step), 25)
                y-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if x-step>0:
                screen.fill(white)
                pygame.draw.circle(screen,red,(x-step,y),25)
                x-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if x+step<400:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x+step,y), 25)
                x+=step
    pygame.display.flip()
    clock.tick(60)