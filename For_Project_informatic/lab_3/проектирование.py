from turtle import *


x= -200
y=0
Vx = 15
Vy = 30
dt = 0.5
ay = -5
ax = -0.2
penup()
back(200)
pendown()

for i in range(100):
    goto(x,y)
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    Vx += ax*dt
    if y < 0:
        Vy = -Vy

    if Vx < 0:
        break
