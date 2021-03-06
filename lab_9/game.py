from random import random
import pygame
from lab_9.modules.ball import Ball, start_speed_x, start_speed_y
from lab_9.modules.bomb import Bomb
from lab_9.modules.tank import Tank
from lab_9.modules.target import Target

pygame.init()

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

sc = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('images/back_ground.jpg').convert()
tank_1 = Tank(WIDTH / 10, HEIGHT / 10, 'images/tank.png')
tank_2 = Tank(WIDTH / 10, 9 * HEIGHT / 10, 'images/tank.png')
target_1 = Target(random()*WIDTH, random()*HEIGHT, 10, 10, 'images/bee.png')
target_2 = Target(random()*WIDTH, random()*HEIGHT, 10, 10, 'images/cry.png')
balls = pygame.sprite.Group()
bombs = pygame.sprite.Group()
control = 0
time_control = 5
time_1 = 0
time_2 = 0
V_ball_1 = 0
V_ball_2 = 0
plus = 1
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if control == 1:
                # для первого танка
                if event.key == pygame.K_q:
                    balls.add(Ball(tank_1.rect.centerx, tank_1.rect.centery, start_speed_x(position_tank_1, V_ball_1),
                                   start_speed_y(position_tank_1, V_ball_1), 'images/ball_1.png'))
                if event.key == pygame.K_e:
                    balls.add(Ball(tank_1.rect.centerx, tank_1.rect.centery, start_speed_x(position_tank_1, V_ball_1),
                                   start_speed_y(position_tank_1, V_ball_1), 'images/ball_2.png'))
                # для второго танка
                if event.key == pygame.K_i:
                    balls.add(Ball(tank_2.rect.centerx, tank_2.rect.centery, start_speed_x(position_tank_2, V_ball_2),
                                   start_speed_y(position_tank_2, V_ball_2), 'images/ball_1.png'))
                if event.key == pygame.K_p:
                    balls.add(Ball(tank_2.rect.centerx, tank_2.rect.centery, start_speed_x(position_tank_1, V_ball_2),
                                   start_speed_y(position_tank_1, V_ball_2), 'images/ball_2.png'))
            else:
                control += 1

    # создание и движение танков
    # первый танк управляется клавишами: 'w', 'x', 'd', 'a'
    # второй танк управляется клавишами: 'o', '.', 'k', ';'

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        tank_1.image_tank('up')
    elif keys[pygame.K_x]:
        tank_1.image_tank('down')
    elif keys[pygame.K_d]:
        tank_1.image_tank('right')
    elif keys[pygame.K_a]:
        tank_1.image_tank('left')
    elif keys[pygame.K_o]:
        tank_2.image_tank('up')
    elif keys[pygame.K_PERIOD]:
        tank_2.image_tank('down')
    elif keys[pygame.K_SEMICOLON]:
        tank_2.image_tank('right')
    elif keys[pygame.K_k]:
        tank_2.image_tank('left')
    # теперь задам начальную скорость снаряда.

    # для первой пушки

    if keys[pygame.K_s]:
        if V_ball_1 < 40:
            V_ball_1 += plus
    if not keys[pygame.K_s]:
        V_ball_1 = 0
    # для второй пушки

    if keys[pygame.K_l]:
        if V_ball_2 < 40:
            V_ball_2 += plus
    if not keys[pygame.K_l]:
        V_ball_2 = 0

    # теперь задам движение этой группы шариков и их удаление через определенное время
    balls.update(WIDTH, HEIGHT)
    # шарики должны жить определенное время
    for ball in balls:
        ball.kill_ball()
    target_1.update(WIDTH, HEIGHT)
    target_2.update(WIDTH, HEIGHT)

    # теперь буду создавать бомбочки которые будут сбрасывать цели
    # бомбочка от цели 1:
    if time_1 == time_control:
        bombs.add(Bomb(target_1.rect.centerx, target_1.rect.centery, 'images/bomb.png'))
        time_1 = 0
    else:
        time_1 += plus
    # бомбочка от цели 2:
    if time_2 == time_control:
        bombs.add(Bomb(target_2.rect.centerx, target_2.rect.centery, 'images/bomb.png'))
        time_2 = 0
    else:
        time_2 += plus
    bombs.update(WIDTH, HEIGHT)

    # сделаю контроль столкновения снаряда и цели. Удаляю цель и создаю новую в случае попадания
    for ball in balls:
        if target_1.rect.colliderect(ball.rect):
            target_1.kill()
            target_1 = Target(random() * WIDTH, random() * HEIGHT, 10, 10, 'images/bee.png')

        if target_2.rect.colliderect(ball.rect):
            target_2.kill()
            target_2 = Target(random() * WIDTH, random() * HEIGHT, 10, 10, 'images/cry.png')






    sc.blit(bg, (0, 0))
    balls.draw(sc)
    bombs.draw(sc)
    sc.blit(tank_1.image, tank_1.rect)
    sc.blit(tank_2.image, tank_2.rect)
    sc.blit(target_1.image, target_1.rect)
    sc.blit(target_2.image, target_2.rect)

    pygame.display.update()
    # сюда сохраняется позиция танка (нужно для создания снаряда)
    position_tank_1 = tank_1.position()
    position_tank_2 = tank_2.position()
pygame.quit()
