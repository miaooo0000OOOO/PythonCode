import pygame
import numpy as np

G = 6.67e-11

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, v, m):
        self.pos = pos
        self.v = v
        self.m = m
        pygame.sprite.Sprite.__init__(self)

    def update(self, others):
        for particle in others:
            self.yongli(particle)


    def yongli(self, F):
        a = F/self.m
        self.v += a
        self.pos += self.v

    def get_yinli(self, B):
        r = B.pos - self.pos
        return (G*self.m*B.m)/r**2

