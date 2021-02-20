import pygame as p
import sys

p.init()

size = w, h = 600, 400
speed = [-2, 2]
bg = (255, 255, 255)

screen = p.display.set_mode(size)
p.display.set_caption("2333")


while True:
        for event in p.event.get():
                print(event)
                if event.type == p.QUIT:
                        sys.exit()
                        
