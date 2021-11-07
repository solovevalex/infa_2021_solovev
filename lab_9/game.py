import math
from random import choice, randint
import pygame
from ball import Ball

from tank import Tank
from target import Target
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

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    # создание и движение танков
    tank_1 = Tank(WIDTH/10, HEIGHT/10, 'images/tank.png')
    tank_2 = Tank(WIDTH/10, 9*HEIGHT/10, 'images/tank.png')
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        tank_1.rect.y -= tank_1.V
    elif keys[pygame.K_x]:
        tank_1.rect.y += tank_1.V
    elif keys[pygame.K_d]:
        tank_1.rect.x += tank_1.V
    elif keys[pygame.K_a]:
        tank_1.rect.x -= tank_1.V
    elif keys[pygame.K_p]:
        tank_2.rect.y -= tank_2.V
    elif keys[pygame.K_SLASH]:
        tank_2.rect.y += tank_2.V
    elif keys[pygame.K_l]:
        tank_2.rect.x -= tank_2.V
    elif keys[pygame.K_QUOTEDBL]:
        tank_2.rect.x += tank_2.V
    sc.blit(bg, (0, 0))
    sc.blit(tank_1.image, tank_1.rect)
    sc.blit(tank_1.image, tank_1.rect)
    pygame.display.update()


pygame.quit()
