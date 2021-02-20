import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
dt = np.array(0.001)
T = 50

def xiangxin(P, O, F):
    return get_vector(P, O, F)

def G(m):
    return np.array([0, -m*9.8])

def F_(t, r =10):
    a = t*10
    x = r*np.cos(a)
    y = r*np.sin(a)
    return np.array([x,y])

def get_vector(P, O, F):
    '''
    已知点O，P,定长F
    作射线OP
    作以O为圆心，F为半径的圆
    射线与圆交于点P
    求向量OC
    '''
    OP = O - P
    k = ((F ** 2) / (OP[0] ** 2 + OP[1] ** 2)) ** 0.5
    OC = OP * k
    return OC


def gravitational(m1, m2, p1, p2, G = 6.67e-11):
    '''万有引力公式'''
    r = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return (G*m1*m2)/(r**2)

'''
class CollisionBox(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.center = pos
'''

class Particle():
    def __init__(self, pos, v, m):
        self.pos = pos
        self.v = v
        self.m = m

    def _yongli_(self, F, t):
        a = F / self.m
        s1 = a * (t ** 2)
        s2 = self.v * t
        s = s1 + s2
        self.pos += s
        v1 = a * t
        self.v += v1

    def yongli(self, F, t):
        a = F/self.m
        s = self.v*t+0.5*a*t**2
        self.v = self.v+a*t
        self.pos = self.pos+s

def main():
    p = Particle(np.array([0,10.]), np.array([10,0.]), 1)
    x, y, z = [], [], []
    t = 0
    i = 0
    F = np.array([0,0.])
    while t<= T: 
        i +=1
        t += dt
        F = -get_vector(p.pos, np.array([0,0.]), gravitational(1, 1, p.pos, np.array([0,0.]), G=1))
        #F = get_vector(p.pos, np.array([0,0.]), 10)
        p.yongli(F, dt)
        if i%1000 == 0:
            print(p.pos, F)
        x.append(p.pos[0]), y.append(p.pos[1]), z.append(t)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x, y, z)
    ax.set(xlabel='x', ylabel='y', zlabel='z')
    plt.show()
main()

'''p = Particle(np.array([0,10.]),
             np.array([10, 0.]),
             np.array(1.))

#plt.ion()
i = 0
fig = plt.figure()
lx, ly, lz = [], [], []
t = np.array(0.)
for j, h in enumerate([5, 10, 15, 20]):
    t = 0
    p = Particle(np.array([0,10.]),
             np.array([h, 0.]),
             np.array(1.))
    lx.append([]), ly.append([]), lz.append([])
    while t <= T:
        t += dt
        i += 1
        F = G(p.m)
        r = (p.pos[0]**2 + p.pos[1]**2)**0.5
        F = xiangxin(p.pos,
                     np.array([0, 0.]),
                     gravitational(1, 1, r, G=1))
        p.yongli(F, dt)
        #print(F, p.pos, t)
        #ax.append(float(t)), ay.append(p.pos[1])
        #if i%10 == 0:
        lx[j].append(p.pos[0]), ly[j].append(p.pos[1]), lz[j].append(float(t))
            #lx.append(F[0]),ly.append(F[1])
            #plt.plot(lx, ly)
            #plt.pause(0.001)
        #plt.clf()
plt.plot(lx[0], ly[0],
        lx[1], ly[1],
        lx[2], ly[2],
        lx[3], ly[3]) 
#ax = Axes3D(fig)
#ax.plot3D(lx, ly, lz)
#ax.set(xlabel='x', ylabel='y', zlabel='t')
plt.show()
'''
'''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Hello')
box_img = pygame.image.load('collision_box.jpg')
box = CollisionBox(box_img)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            F = event.pos - p.pos
            p.yongli(F, dt)
            pos = xianwei(pos)
    box.update(p.pos)
    screen.blit(box.image, box.rect)
    print(p.pos)
'''













'''
plt.ion()
ax = []
ay = []
t = 0
for i in range(100):
    t += dt
    r = (((p.pos[0]-sun.pos[0])**2)+((p.pos[1]-sun.pos[1])**2))**0.5
    #F = get_vector(p.pos, sun.pos, gravitational(p.m, sun.m, p.pos, 1))
    F1 = F(t)
    p.yongli(F1, dt)
    ax.append(p.pos[0])
    ay.append(p.pos[1])
    plt.plot(ax, ay)
    plt.pause(0.1)
    plt.clf()
'''
