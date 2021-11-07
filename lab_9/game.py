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
        tank_1.rect.y -= tank_1.V
        tank_1.image_tank('up')
        if tank_1.rect.y < 0:
            tank_1.rect.y = 0
    elif keys[pygame.K_x]:
        tank_1.rect.y += tank_1.V
        tank_1.image_tank('down')
        if tank_1.rect.y > HEIGHT - tank_1.rect.width:
            tank_1.rect.y = HEIGHT - tank_1.rect.width
    elif keys[pygame.K_d]:
        tank_1.rect.x += tank_1.V
        tank_1.image_tank('right')
        if tank_1.rect.x > WIDTH - tank_1.rect.width:
            tank_1.rect.x = WIDTH - tank_1.rect.width
    elif keys[pygame.K_a]:
        tank_1.rect.x -= tank_1.V
        tank_1.image_tank('left')
        if tank_1.rect.x < 0:
            tank_1.rect.x = 0
    elif keys[pygame.K_o]:
        tank_2.rect.y -= tank_2.V
        tank_2.image_tank('up')
        if tank_2.rect.y < 0:
            tank_2.rect.y = 0
    elif keys[pygame.K_PERIOD]:
        tank_2.rect.y += tank_2.V
        tank_2.image_tank('down')
        if tank_2.rect.y > HEIGHT - tank_2.rect.width:
            tank_2.rect.y = HEIGHT - tank_2.rect.width
    elif keys[pygame.K_SEMICOLON]:
        tank_2.rect.x += tank_2.V
        tank_2.image_tank('right')
        if tank_2.rect.x > WIDTH - tank_2.rect.width:
            tank_2.rect.x = WIDTH - tank_2.rect.width
    elif keys[pygame.K_k]:
        tank_2.rect.x -= tank_2.V
        tank_2.image_tank('left')
        if tank_2.rect.x < 0:
            tank_2.rect.x = 0

    sc.blit(bg, (0, 0))
    sc.blit(tank_1.image, tank_1.rect)
    sc.blit(tank_2.image, tank_2.rect)
    pygame.display.update()


pygame.quit()
