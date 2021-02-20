if __name__ == '__main__':
    print('env')

import pygame
import random as R
import numpy as np

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

class Env:
    def get_s(self):
        e_pos = [enemy.rect.topleft for enemy in self.enemy_group.sprites()]
        p_pos = self.collision_box.rect.center
        b_pos = [bullet.rect.topleft for bullet in self.enemy_bullet_group.sprites()]
        s = np.zeros([16, 2])

        s[0] = p_pos
        for i in range(5):
            if i >= len(e_pos):
                break
            s[i+1] = e_pos[i]
        for i in range(10):
            if i >= len(b_pos):
                break
            s[i+6] = b_pos[i]

        return s.flatten()




    def __init__(self):
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('Hello')
        self.steps = 0

        self.bg_img = pygame.image.load('background1.jpg')
        self.player_img = pygame.image.load('feiji1.png')
        self.bullet_img = pygame.image.load('bullet.jpg')
        enemy_img = pygame.image.load('feiji2.png')
        self.enemy_img = pygame.transform.scale(enemy_img, (80, 80))
        self.collision_box_img = pygame.image.load('collision_box.jpg')
        self.gg_img = pygame.image.load('gameover.jpg')

        self.player = Player(self.player_img, [200, 500])
        self.collision_box = CollisionBox(self.collision_box_img)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()

    def step(self, keys):
        clock = self.clock
        screen = self.screen
        player = self.player
        collision_box = self.collision_box
        steps = self.steps
        enemy_img = self.enemy_img
        enemy_group = self.enemy_group
        enemy_bullet_group = self.enemy_bullet_group
        bullet_img = self.bullet_img
        done = False
        r = 0

        clock.tick(60)

        #玩家移动

        player.move(keys)

        # 敌人生成
        if steps % 30 == 0:
            enemy = Enemy(enemy_img, [R.randint(0, SCREEN_WIDTH - enemy_img.get_width()),
                                      -enemy_img.get_height()])
            enemy_group.add(enemy)

        # 敌方子弹生成
        for enemy in enemy_group.sprites():
            if enemy.ticks == 30:
                enemy.ticks = 0
                enemy_bullet_group.add(Bullet(bullet_img, enemy.rect.midbottom,
                                              speed=get_speed(enemy.rect.midbottom, player.rect.center)))

        player.update(offset, bullet_img)
        collision_box.update(player.rect.center)
        player.bullet_group.update()
        pygame.sprite.groupcollide(enemy_group, player.bullet_group, True, True)
        a = pygame.sprite.spritecollide(collision_box, enemy_bullet_group, True)
        if a:
            player.hp -= 1
            r += -100
        if player.hp <= 0:
            done = True
            r += -200



        player.bullet_group.update()
        enemy_group.update(bullet_img)
        enemy_bullet_group.update()
        pygame.sprite.groupcollide(enemy_group, player.bullet_group, True, True)

        self.clock = clock
        self.screen = screen
        self.player = player
        self.collision_box = collision_box
        self.steps = steps + 1
        self.enemy_group = enemy_group
        self.enemy_bullet_group = enemy_bullet_group
        if r == 0:
            r = 100
        if done:
            r = self.steps
        s = self.get_s()
        return s, r, done


    def draw(self):
        screen = self.screen
        bg_img = self.bg_img
        player = self.player
        collision_box = self.collision_box
        enemy_group = self.enemy_group
        enemy_bullet_group = self.enemy_bullet_group


        screen.blit(bg_img, (0,0))
        screen.blit(player.image, player.rect)
        screen.blit(collision_box.image, collision_box.rect)
        show_text(screen,(0,0),"hp:{}".format(player.hp), font_size=40)

        collision_box.update(player.rect.center)

        player.bullet_group.draw(screen)

        enemy_group.draw(screen)

        enemy_bullet_group.draw(screen)
        pygame.display.flip()


    def reset(self):
        self.steps = 0
        self.player = Player(self.player_img, [200, 500])
        self.collision_box = CollisionBox(self.collision_box_img)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        return self.get_s()



def show_text(surface_handle, pos, text, color=(255, 255, 255), font_bold=False, font_size=13, font_italic=False):
    '''
    Function:文字处理函数
    Input：surface_handle：surface句柄
           pos：文字显示位置
           color:文字颜色
           font_bold:是否加粗
           font_size:字体大小
           font_italic:是否斜体
    Output: NONE
    '''
    cur_font = pygame.font.SysFont("simsunnsimsun", font_size)
    cur_font.set_bold(font_bold)
    cur_font.set_italic(font_italic)
    text_fmt = cur_font.render(text, 1, color)
    surface_handle.blit(text_fmt, pos)


def get_speed(A, B, r=8):
    '''
    已知点A，B,定长r
    作射线AB
    作以A为圆心，r为半径的圆
    射线与圆交于点C
    求向量AC
    '''
    x = B[0] - A[0]
    y = B[1] - A[1]
    k = ((r ** 2) / (x ** 2 + y ** 2)) ** 0.5
    r = [k * x, k * y]
    return r


class CollisionBox(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.center = pos


class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_surface, enemy_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos
        self.speed = 4
        self.ticks = 0

    def move(self):
        self.rect.top += self.speed

    def update(self, bullet_surface):
        self.ticks += 1
        self.move()
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet_surface, init_pos, speed=[0, -8]):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = speed

    def move(self):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

    def update(self):
        self.move()
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, surface, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 8
        self.hp = 3

        self.bullet_group = pygame.sprite.Group()
        self.ticks = 0

    def shoot(self, surface):
        bullet1 = Bullet(surface, self.rect.midtop)
        # bullet2 = Bullet(surface, self.rect.topright)
        self.bullet_group.add(bullet1)
        # self.bullet_group.add(bullet2)

    def move(self, keys):
        dx = 0
        dy = 0
        if pygame.K_UP == keys:
            dy -= self.speed
        if pygame.K_DOWN == keys:
            dy += self.speed
        if pygame.K_RIGHT == keys:
            dx += self.speed
        if pygame.K_LEFT == keys:
            dx -= self.speed
        x = self.rect.left + dx
        y = self.rect.top + dy
        if x < 0:
            self.rect.left = 0
        elif x > SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left = x

        if y < 0:
            self.rect.top = 0
        elif y > SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top = y

    def update(self, offset, bullet_surface):
        self.move(offset)
        self.ticks += 1
        if self.ticks == 10:
            self.shoot(bullet_surface)
            self.ticks = 0

if __name__ == '__main__':
    env = Env()
    KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    keys = []
    done = False
    while True:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in KEYS:
                        keys.append(event.key)
                if event.type == pygame.KEYUP:
                    if event.key in KEYS:
                        keys.remove(event.key)
            s, r, done = env.step(keys)
            print(s)
            env.draw()
        print('r:{}'.format(r))
        env.reset()
        s, r, done = 0, 0, 0
