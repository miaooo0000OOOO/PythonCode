import matplotlib.pyplot as plt
import numpy as np

N = 10
G = 6.67e-11

class Particle():
    def __init__(self, pos=np.zeros(2), v=np.zeros(2)):
        self.pos = pos
        self.v = v
        self.m = 1

    def yongli(self, F):
        a = F/self.m
        self.v += a

    def update(self, B):
        self.yongli(np.random.random(2)*N)
        self.yongli(self.yinli(B))

    def yinli(self, B):
        r = B.pos - self.pos
        return (G*self.m*B.m)/r**2

class World():
    def __init__(self):
        self.particles = []

    def add(self, particle):
        self.particles.append(particle)

    def detel(self, particle):
        self.particles.remove(particle)

    def update(self, *args, **kwargs):
        for i in range(len(self.particles)):
            self.particles[i].update(*args, **kwargs)


w = World()
w.add(Particle(pos=np.array()))