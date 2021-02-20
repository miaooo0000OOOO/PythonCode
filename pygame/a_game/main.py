import pygame as pg
from sys import exit

size = (600,170)

pg.init()
screen = pg.display.set_mode(size, 0, 32)
pg.display.set_caption("A game")
bg = pg.image.load("背景.jpg")
plane = pg.image.load("飞机.jpg")

while True:
    for event in pg.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

