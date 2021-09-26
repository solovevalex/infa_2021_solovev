import pygame
from pygame.draw import *

pygame.init()

size = (400, 400)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
fps = 30

circle(screen, (255, 255, 0), (200,200,), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 3)
circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (255, 0, 0), (250, 175), 25)
circle(screen, (0, 0, 0), (150, 175), 20, 3)
circle(screen, (0, 0, 0), (250, 175), 25, 3)
circle(screen, (0, 0, 0), (150, 175), 10)
circle(screen, (0, 0, 0), (250, 175), 12)

polygon(screen, (0, 0, 0), [(175, 175), (180, 172), (80,80), (65,85), (175, 175)])
polygon(screen, (0, 0, 0), [(210, 175), (220, 172), (300,80), (285,85), (210, 175)])

rect(screen, (0,0,0), (150, 230,50,10))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
