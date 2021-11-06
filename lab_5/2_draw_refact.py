import pygame
from pygame.draw import *

pygame.init()

# просто задача частоты и ширины/высоты открываемого экрана картинки
fps = 30
width = 600
high = 600


# задаю цвета
black = (0, 0, 0)
blue = (0, 20, 140)
rama = (150, 150, 150)
grey = (192, 192, 192)
brown = (153, 76, 0)
green = (0, 204, 0)
darkgreen = (50, 100, 0)
darkbrown = (102, 51, 0)
darkgrey = (96, 96, 96)
darkblue = (50, 50, 100)


screen = pygame.display.set_mode((width, high))

# ниже разделение экрана на две части с разными цветами
rect(screen, darkblue, (0, 0, width, high/2))
rect(screen, darkgreen, (0, high/2, width, high/2))


def window(x, y, size):
    '''
    Рисует окно. x и y задают координаты верхнего левого угла окна. size - это ширина окна.
    '''
    rect(screen, rama, (x, y, size, size*2+size/40))
    rect(screen, blue, (x+size/10, y + size/10, 4*size/5, 9*size/5))
    line(screen, rama, [x + size/2, y], [x+size/2, y+2*size], int(size/20))
    line(screen, rama, [x, y+2*size/3], [x+size-size/20, y + 2 * size/3], int(size/20))
    '''
    Сам код - чисто расчет для данногй модели окна
    '''

def cat(x, y, size, color1, color2):
    '''
    Рисует кота. x и y задают координаты центра головы. size - это ширина туловища.
    color1 - это цвет для туловища и ушей,
    color2 - это цвет для головы, ног и хвоста
    '''
    ellipse(screen, color1, (x, y, 3*size, size))  # туловище
    circle(screen, color2, (x, y), 4*size/5)  # голова
    for z in 0.3*size, 0.9*size, 1.8*size, 2.4*size:  # ноги
        ellipse(screen, color2, (x+z, y+3*size/6, 0.3*size, 1.3*size))
    ellipse(screen, color2, (x+9*size/4, y, 1.5*size, size/2))  # хвост
    for z in -size/4, size/4:  # уши
        ellipse(screen, color1, (x+1.4*z-x/15, y-1.5*size, size/3, 1.1*size))
    for z in size/6, -size/6-size/5:  # глаза
        ellipse(screen, blue, (x+z, y-size/4, size/5, size/8))
    line(screen, black, (x, y), (x, y+size/5), 3)  # нос
    line(screen, black, (x-size/10, y+size/3), (x+size/10, y+size/3))  # рот
    for z in -size/4, size/4:  # усы
        for s in 0, size/8, -size/8:
            line(screen, black, (x+z, y+s+size/3), (x+2*z, y+2*s+size/3), 2)
    '''
    код - чисто расчет для данной модели кота
    '''

def ooo(x, y, size, color):
    '''
    Рисует клубок x и y - это координаты центра клубка.
    size - это диаметр клубка
    color - это цвет клубка
    '''
    circle(screen, color, (x, y), size)
    arc(screen, black, (x+size/2**0.5, y+size/2.5, size, size), 0, 2.50)
    arc(screen, black, (x + 2.4*size / 2 ** 0.5, y + size / 2.2, size, size), 3, 6)
    arc(screen, black, (x-size/3, y-size/2, size, size), 0, 2)
    arc(screen, black, (x - size / 2, y - size / 5, size, size), 2, 4)
    arc(screen, black, (x - size / 4, y - size / 4, size, size), 4, 6)


for x in 100, 250, 400:
    window(x, 25, 100)

cat(100, 500, 40, grey, darkgrey)
cat(300, 350, 70, brown, darkbrown)
ooo(100, 350, 60, green)
ooo(450, 520, 30, blue)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()