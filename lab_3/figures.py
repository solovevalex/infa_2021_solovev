from turtle import *

size = 20  # это ширина буквы
speed = 1
# координаты верхнего левого угла цифры для начального момента
x = -100
y = 0
pos1 = x, y
pos2 = x + size, y
pos3 = x, y - size
pos4 = x + size, y - size
pos5 = x, y - 2 * size
pos6 = x + size, y - 2 * size

# ниже задается список из кортежей. индекс списка указывает на ту цифру, которая рисуется по указанным позициямю

numbers = [(pos1, pos2, pos4, pos6, pos5, pos3, pos1),
           (pos3, pos2, pos4, pos6),
           (pos1, pos2, pos4, pos5, pos6),
           (pos1, pos2, pos3, pos4, pos5),
           (pos1, pos3, pos4, pos2, pos6),
           (pos2, pos1, pos3, pos4, pos6, pos5),
           (pos2, pos3, pos5, pos6, pos4, pos3),
           (pos1, pos2, pos3, pos5),
           (pos1, pos2, pos4, pos6, pos5, pos3, pos1, pos3, pos4),
           (pos5, pos4, pos3, pos1, pos2, pos4)
           ]

figures = str(input('Введите число: '))

for figure in figures:
    figure = int(figure)
    comand = numbers[figure]
    penup()
    goto(comand[0])
    pendown()
    for pos in comand:
        goto(pos)
    x = x + 2 * size
    y = y
    pos1 = x, y
    pos2 = x + size, y
    pos3 = x, y - size
    pos4 = x + size, y - size
    pos5 = x, y - 2 * size
    pos6 = x + size, y - 2 * size
    numbers = [(pos1, pos2, pos4, pos6, pos5, pos3, pos1),
               (pos3, pos2, pos4, pos6),
               (pos1, pos2, pos4, pos5, pos6),
               (pos1, pos2, pos3, pos4, pos5),
               (pos1, pos3, pos4, pos2, pos6),
               (pos2, pos1, pos3, pos4, pos6, pos5),
               (pos2, pos3, pos5, pos6, pos4, pos3),
               (pos1, pos2, pos3, pos5),
               (pos1, pos2, pos4, pos6, pos5, pos3, pos1, pos3, pos4),
               (pos5, pos4, pos3, pos1, pos2, pos4)
               ]
