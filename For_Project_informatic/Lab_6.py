import pygame as pg
from random import randint

pg.init()

# количество объектов на экране, одновременно находящихся (шариков и квадратов)
number_balls = 5
number_rects = 5
# размер игрового окна
W = 1000
H = 500
# цена за попадание в шарик и квадрат
rent_ball = 1
rent_rect = 10
# максимальный и минимальный возможный размер объекта на экране
max_size = 50
min_size = 20

FPS = 10
screen = pg.display.set_mode((W, H))

# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
rects = []


def new_ball():
    '''
    Создаёт новый шарик
    x, y - координаты центра шарика
    r - радиус
    color - цвет
    dx - скорость по оси х
    dy - скорость по оси у
    '''
    r = randint(int(min_size / 2), int(max_size / 2))
    x = randint(r, W - r)
    y = randint(r, H - r)
    dx = randint(0, int(r / 2))
    dy = randint(0, int(r / 2))
    color = COLORS[randint(0, 5)]
    ball = {'color': color, 'r': r, 'p': {'x': x, 'y': y}, 'v': {'dx': dx, 'dy': dy}}
    balls.append(ball)


def new_rect():
    '''
    Создаёт новый квадрат
    x, y - координаты левого верхнего угла объекта
    l - длина стороны
    color - цвет
    '''
    l = randint(min_size, max_size)
    x = randint(l, W - l)
    y = randint(l, H - l)
    dx = randint(0, int(l / 2))
    dy = randint(0, int(l / 2))
    color = COLORS[randint(0, 5)]
    rect = {'color': color, 'l': l, 'p': {'x': x, 'y': y}, 'v': {'dx': dx, 'dy': dy}}
    rects.append(rect)


def draw_ball(x, y, r, color):
    '''
    Рисует шарик.
    x, y - координаты центра шарика.
    r - радиус шарика.
    color - цвет шарика.
    '''
    pg.draw.circle(screen, color, (x, y), r)


def draw_rect(x, y, l, color):
    '''
    Рисует объект.
    x, y - координаты левого верхнего угла объекта.
    l - характерный линейный размер объекта.
    color - цвет объекта.
    '''
    pg.draw.rect(screen, color, (x, y, l, l))


# Загоняю данные о заданном количестве шариков в список, состоящий из словарей
for i in range(number_balls):
    new_ball()

# Загоняю данные о заданном количестве объектов в список, состоящий из словарей
for i in range(number_rects):
    new_rect()

# Запрашиваю имя игрока
print("Введите имя: ")
name = input()

clock = pg.time.Clock()
finished = False
S = 0  # количество очков
pos = [0, 0]

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()

    for ball in balls:
        # Работа с левой и правой стенкой. Изменяю направление скорости в слючае, если стенка рядом
        if ball['p']['x'] >= W - ball['r'] or ball['p']['x'] <= ball['r']:
            ball['v']['dx'] *= - 1
        # Работа с нижней и верхней стенкой. Изменяю направление скорости в слючае, если стенка рядом
        if ball['p']['y'] >= H - ball['r'] or ball['p']['y'] <= ball['r']:
            ball['v']['dy'] *= - 1
        # Задается новое положение шарика
        ball['p']['x'] += ball['v']['dx']
        ball['p']['y'] += ball['v']['dy']
        # Рисуется старый шарик с новыми координатами
        draw_ball(ball['p']['x'], ball['p']['y'], ball['r'], ball['color'])

        # Проверка на попадание. Удаление шарика, в который попали. Создание нового. Добавление очков
        if (ball['p']['x'] - pos[0]) ** 2 + (ball['p']['y'] - pos[1]) ** 2 <= ball['r'] ** 2:
            S += rent_ball
            balls.remove(ball)
            new_ball()

    for rect in rects:
        # Работа с левой и правой стенкой. Изменяю направление скорости в слючае, если стенка рядом
        if rect['p']['x'] >= W - rect['l'] or rect['p']['x'] <= 0:
            rect['v']['dx'] *= - 1
        # Работа с нижней и верхней стенкой. Изменяю направление скорости в слючае, если стенка рядом
        if rect['p']['y'] >= H - rect['l'] or rect['p']['y'] <= 0:
            rect['v']['dy'] *= - 1
        # Задается новое положение квадрата:
        rect['p']['x'] += rect['v']['dx']
        rect['p']['y'] += rect['v']['dy']
        # Рисоване квадрата:
        draw_rect(rect['p']['x'], rect['p']['y'], rect['l'], rect['color'])

        # Проверка на попадание. Удаление квадрата, в который попали. Создание нового. Добавление очков
        if (rect['p']['x'] - pos[0]) ** 2 + (rect['p']['y'] - pos[1]) ** 2 <= rect['l'] ** 2:
            S += rent_rect
            rects.remove(rect)
            new_rect()

    pg.display.update()
    screen.fill(BLACK)
pg.quit()

print('Ты набрал: ', S)
print('!!!')

