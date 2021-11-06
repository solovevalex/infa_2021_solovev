import pygame as pg
import random as rd
from pygame.draw import *
pg.init()

FPS = 30
width = 600
height = 600
screen = pg.display.set_mode((width, height))
addscreen = pg.display.set_mode((width, height))

# colors
lightgrey = (224, 224, 235)
grey = (193, 193, 215)
darkgrey = (117, 117, 163)
black = (0, 0, 0)
verydarkgreen = (102, 102, 51)
green = (0, 153, 0)
yellow = (255, 255, 0)
darkyellow = (230, 230, 0)
darkbrown = (128, 85, 0)
brown = (179, 119, 0)
blue = (51, 102, 255)
darkred = (179, 0, 0)
pink = (255, 102, 204)


def random_color(color1, color2):
    index = rd.randint(0, 1)
    return((color1, color2)[index])

def Mypicture():
    background(width, height)
    houses(width, height)
    ghosts(width, height)
    clouds(width, height)
    pass

def background():
    """
    :return:разделяет фон пополам на землю и небо.
    """
    rect(screen, grey, (0, 0, width, height/2))
    rect(screen, black, (0, height/2, width, height/2))

def house(x, y, width, height, screen):
    """
    :param x: координата середины дома
    :param y: координата самой нижней точки дома
    :param width: ширина обшей картинки дома
    :param height: высота общей картинки дома исключая трубы
    :return: один дом
    """
    #bodyhouse
    rect(screen, random_color(verydarkgreen, darkbrown), (x - 5*width/14, y - 5*height/6, 5*width/7, 5*height/6))
    #balcony
    rect(screen, darkgrey, (x - width/2, y - height/2, width, height/6))
    #roof
    polygon(screen, random_color(green, darkred), [(x + width/2, y - 5*height/6), (x + 3*width/7, y - height),
                            (x - 3*width/7, y - height), (x - width/2, y - 5*height/6)])
    #pipe
    rect(screen, random_color(grey, darkyellow), (x + width/6, y - 13*height/12, width/6, height/6))
    #upwindows
    for z in x - 4*width/14, x - 2*width/14, x + width/14, x + 3*width/14:
        rect(screen, random_color(yellow, darkbrown), (z, y - 5*height/6, width/14, height/3))
    #downwindows
    for z in x - 2*width/7, x - width/14, x + width/7:
        rect(screen, random_color(darkyellow, brown), (z, y - height/3.5, width/7, 2*height/9))

def houses(number):
    """
    :return: рисует город состоящий из домов
    """
    for i in range(number):
        x = rd.randint(0, width)
        y = rd.randint(5*height/8, 5*height/6)
        height_house = rd.randint(height/8, height/4)
        width_house = rd.randint(width/8, width/4)
        house(x, y, width_house, height_house, screen)


def ghost(x, y, radius_head, screen):
    #head
    color = random_color(grey, darkbrown)
    circle(screen, color, (x, y), radius_head)
    r = radius_head
    #body
    polygon(screen, color, ([x-r, y], [x-7*r/3, y+3*r],
                            [x-6*r/4, y+3*r-r/5], [x-r/3, y+3*r+r/5],
                            [x, y+3*r-r/3], [x+3*r/3, y+3*r-r/2],
                            [x+5*r/3, y+3*r-r/5], [x+5*r/6, y-r/6]))
    #глаза
    circle(screen, blue, (x+r/2, y+r/8), r/5)
    circle(screen, black, (x + r / 2, y + r / 8), r / 5, 2)
    circle(screen, blue, (x-r/2, y-r/8), r/5)
    circle(screen, black, (x - r / 2, y - r / 8), r / 5, 2)

def ghosts(number):
    """
    :number: количество призраков
    :return: рисует заданное количество призраков.
    """
    for i in range(number):
        x = rd.randint(0, width)
        y = rd.randint(int(3*height/4), int(8*height/9))
        radius_head = rd.randint(int(min(width, height)/32), int(min(width, height)/16))
        ghost(x, y, radius_head, screen)

def clouds(number):
    """
    :return: рисует заданное количество облаков.
    """
    for i in range(number):
        x = rd.randint(0, width)
        y = rd.randint(0, int(2 * height / 6))
        width_cloud = rd.randint(int(height / 18), int(height / 12))
        lenght_cloud = rd.randint(int(width / 2), int(width))
        cloud(x, y, lenght_cloud, width_cloud, random_color(blue, pink), screen)
        #здесь какая-то проблема

def cloud(x, y, lenght, width, color, screen):
    """
    :param x: координата середины облака по горизонтали
    :param y: координата середины облака по вертикали
    :param lenght: длина облака
    :param width: ширина облика
    :param: color: цвет облака
    :return: собственно одно облако
    """
    ellipse(screen, color, (x-lenght/2, y-width/2, lenght, width))



background()
clouds(10)
houses(30)
ghosts(30)





pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()