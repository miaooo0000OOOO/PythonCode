import pygame as p
import sys

p.init()

size = w, h = 600, 400
speed = [-2, 2]
bg = (255, 255, 255)

screen = p.display.set_mode(size)
p.display.set_caption("2333")

tu = p.image.load("ceshi.png")
position = tu.get_rect()

while True:
        print("x;" + str(list(position)[0]), end=' ')
        print("y:" + str(list(position)[1]))
        for event in p.event.get():
                if event.type == p.QUIT:
                        sys.exit()

        position = position.move(speed)

        if position.left < 0 or position.right > w:
                tu = p.transform.flip(tu, True, False)
                speed[0] = -speed[0]

        if position.top < 0 or position.bottom > h:
                speed[1] = -speed[1]

        screen.fill(bg)
        screen.blit(tu, position)
        p.display.flip()
        p.time.delay(10)
