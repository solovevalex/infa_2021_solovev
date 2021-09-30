import pygame
from pygame.draw import *

pygame.init()

fps = 30
width = 600
length = 600
black = (0,0,0)
blue = (0,20,140)
rama = (150, 150, 150)
screen = pygame.display.set_mode((width, length))
rect(screen, (50, 50, 100), (0,0,length,width/2))
rect(screen, (50,100,0), (0,width/2,length, width/2))


def window(x, y, size):
    rect(screen, rama, (x, y, size, size*2+size/40))
    rect(screen, blue, (x+size/10, y + size/10, 4*size/5, 9*size/5))
    line(screen, rama, [x + size/2, y], [x+size/2, y+2*size], int(size/20))
    line(screen, rama, [x, y+2*size/3], [x+size-size/20, y + 2 * size/3], int(size/20))

def cat (x, y, size, с):
    ellipse(screen, (с, с, с - 100), (x, y, 3*size, size)) # туловище
    circle(screen, (с+50, с+50, с-100), (x, y), 4*size/5) # голова
    for z in 0.3*size, 0.9*size, 1.8*size, 2.4*size: # ноги
             ellipse(screen, (с+50, с+50, с-100), (x+z, y+3*size/6, 0.3*size, 1.3*size))
    ellipse(screen, (с+50, с+50, с-100), (x+9*size/4, y, 1.5*size, size/2)) # хвост
    for z in -size/4, size/4: # уши
        ellipse(screen, (с, с, с - 100), (x+1.4*z-x/15, y-1.5*size, size/3, 1.1*size))
    for z in size/6, -size/6-size/5: # глаза
        ellipse(screen, (с-100, с-100, с), (x+z,y-size/4, size/5,size/8))
    line(screen, (0,0,0), (x,y), (x,y+size/5),3) # нос
    line(screen, (0,0,0), (x-size/10,y+size/3),(x+size/10,y+size/3)) # рот
    for z in -size/4, size/4:
        for s in 0, size/8, -size/8:
            line(screen, (0,0,0), (x+z, y+s+size/3), (x+2*z, y+2*s+size/3), 2)

def ooo(x, y, size1):
    circle(screen, (150,200,200), (x,y), size1)
    arc(screen, black, (x+size1/2**0.5, y+size1/2.5, size1, size1), 0, 2.50)
    arc(screen, black, (x + 2.4*size1 / 2 ** 0.5, y + size1 / 2.2, size1, size1), 3, 6)
    arc(screen, black, (x- size1/3,y-size1/2,size1, size1), 0,2)
    arc(screen, black, (x - size1 / 2, y - size1 / 5, size1, size1), 2, 4)
    arc(screen, black, (x - size1 / 4, y - size1 / 4, size1, size1), 4, 6)


window(250, 25, 130)
cat(320,410,70,200)
ooo(100, 450, 60)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()