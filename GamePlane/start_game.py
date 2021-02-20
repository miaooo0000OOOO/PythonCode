try:
    import random as R
    import math as M
    import time as T
    import sys
    import pygame
    from pygame.locals import *


    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400
    offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

    def show_text(surface_handle, pos, text, color=(255,255,255), font_bold = False, font_size = 13, font_italic = False): 
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
        x = B[0]-A[0]
        y = B[1]-A[1]
        k = ((r**2)/(x**2+y**2))**0.5
        v = [k*x, k*y]
        return v

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
        
        def __init__(self, bullet_surface, init_pos, speed = [0,-8]):
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
            self.shift = False
            self.hp = 10

            self.bullet_group = pygame.sprite.Group()
            self.ticks = 0

        def shoot(self, surface):
            bullet1 = Bullet(surface, self.rect.midtop)
            #bullet2 = Bullet(surface, self.rect.topright)
            self.bullet_group.add(bullet1)
            #self.bullet_group.add(bullet2)

        def move(self, offset):
            dx = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
            dy = offset[pygame.K_DOWN] - offset[pygame.K_UP]
            if self.shift:
                dx *= 0.7
                dy *= 0.7
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

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT],FULLSCREEN)
    pygame.display.set_caption('Hello')
    ticks = 0

    bg_img = pygame.image.load('background1.jpg')
    player_img = pygame.image.load('feiji1.png')
    bullet_img = pygame.image.load('bullet.jpg')
    enemy_img = pygame.image.load('feiji2.png')
    enemy_img = pygame.transform.scale(enemy_img,(80,80))
    collision_box_img = pygame.image.load('collision_box.jpg')
    gg_img = pygame.image.load('gameover.jpg')

    player = Player(player_img, [200,500])
    collision_box = CollisionBox(collision_box_img)
    enemy_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()

    ticks = 0
    start_time = T.time()
    while True:
        ticks += 1
        clock.tick(60)
        screen.blit(bg_img, (0,0))
        screen.blit(player.image, player.rect)
        screen.blit(collision_box.image, collision_box.rect)
        show_text(screen,(0,0),"hp:{}".format(player.hp), font_size=40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.shift = True
                if event.key in offset:
                    offset[event.key] = player.speed
            elif event.type == pygame.KEYUP:
                if event.key in offset:
                    offset[event.key] = 0
                if event.key == pygame.K_LSHIFT:
                    player.shift = False

        #敌人生成
        if ticks%30 == 0:
            enemy = Enemy(enemy_img, [R.randint(0, SCREEN_WIDTH-enemy_img.get_width()),
                                      -enemy_img.get_height()])
            enemy_group.add(enemy)
        
        #敌方子弹生成
        for enemy in enemy_group.sprites():
            if enemy.ticks == 30:
                enemy.ticks = 0
                enemy_bullet_group.add(Bullet(bullet_img, enemy.rect.midbottom,
                                              speed=get_speed(enemy.rect.midbottom, player.rect.center)))
                #enemy_bullet_group.add(Bullet(bullet_img, enemy.rect.midbottom,
                #                              speed=[3,8]))

        player.update(offset, bullet_img)
        collision_box.update(player.rect.center)
        player.bullet_group.update()
        player.bullet_group.draw(screen)
        enemy_group.update(bullet_img)
        enemy_group.draw(screen)
        enemy_bullet_group.update()
        enemy_bullet_group.draw(screen)
        pygame.display.flip()
        pygame.sprite.groupcollide(enemy_group, player.bullet_group, True, True)
        a = pygame.sprite.spritecollide(collision_box, enemy_bullet_group, True)
        if a:
            player.hp -= 1
        if player.hp <= 0:
            break
    end_time = T.time()
    while True:
        screen.blit(gg_img,(0,0))
        show_text(screen,(0,0),u"按任意键退出", font_size=40)
        show_text(screen,(0,40),u'你坚持了{}秒'.format(int(end_time-start_time)), font_size=40)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
except BaseException as err:
    print(err)
    f = open('rizhi.txt', 'w')
    f.write(str(err))
    f.close()
finally:
    pygame.quit()
    sys.exit()

            
