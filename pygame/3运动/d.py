import pygame
from sys import exit

pygame.init()
screen =pygame .display.set_mode((1000,1000),0,32)
pygame.display.set_caption("运动")
zidan = pygame.image.load('zidan.jpg')
feiji = pygame.image.load('feiji.jpg')
bg = pygame.image.load('bg.jpg')
zx,zy = (0,1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    x,y = pygame.mouse.get_pos()
    fx = x - feiji.get_width()/2
    fy = y - feiji.get_height()/2
    if zy>0:
        zx = x - feiji.get_width()/2
        zy = y - feiji.get_height()/2
    else:
        zy+=5
    screen.blit(bg,(0,0))
    screen.blit(zidan,(zx,zx))
    screen.blit(feiji,(fx,fy))

    pygame.display.update()
    print('0')
