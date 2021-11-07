import math
from random import choice, randint
import pygame
from lab_9.modules.ball import Ball
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
tank_1 = Tank(WIDTH/10, HEIGHT/10, 'images/tank.png')
tank_2 = Tank(WIDTH/10, 9*HEIGHT/10, 'images/tank.png')

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
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
    plus = 1
    # для первой пушки
    V_ball_1 = 0
    if keys[pygame.K_s]:
        if V_ball_1 < 20:
            V_ball_1 += plus
    # для второй пушки
    V_ball_2 = 0
    if keys[pygame.K_l]:
        if V_ball_2 < 20:
            V_ball_2 += plus

    # Теперь будут создаваться снаряды-шарики пушек. Задаю все необходимое для этого
    balls = pygame.sprite.Group()
    # для первой пушки
    # if keys[pygame.K_q]:
    #     if tank_1.image == tank_1.right:






    sc.blit(bg, (0, 0))
    sc.blit(tank_1.image, tank_1.rect)
    sc.blit(tank_2.image, tank_2.rect)
    pygame.display.update()


pygame.quit()
