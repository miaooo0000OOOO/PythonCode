# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('bg.jpg').convert()
plane = pygame.image.load('feiji.jpg').convert_alpha()
bullet = pygame.image.load('zidan.jpg').convert_alpha()
#加载子弹图像
bullet_x = 0
bullet_y = -1
#初始化子弹位置
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    x, y = pygame.mouse.get_pos()
    if bullet_y < 0:
        #如果子弹位置超出了屏幕上端
        bullet_x = x - bullet.get_width() / 2
        bullet_y = y - bullet.get_height() / 2
        #把子弹的中心位置设为鼠标坐标
    else:
        bullet_y -= 5
        #子弹的位置往上移
    screen.blit(bullet, (bullet_x, bullet_y))
    #把子弹画到屏幕上
    x-= plane.get_width() / 2
    y-= plane.get_height() / 2
    screen.blit(plane, (x, y))
    pygame.display.update()
