# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1000, 600), 0, 32)
pygame.display.set_caption("鼠标移动")
plane = pygame.image.load('feiji.jpg').convert()
black = pygame.image.load('bg.jpg')
#加载飞机图像
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(black,(0,0))
    x, y = pygame.mouse.get_pos()
    #获取鼠标位置
    x-= plane.get_width() / 2
    y-= plane.get_height() / 2
    #计算飞机的左上角位置
    screen.blit(plane, (x,y))
    #把飞机画到屏幕上
    pygame.display.update()
