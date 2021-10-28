class Point3D:
    'Класс создает точки с координатами. По дефолту координаты равны 0'

    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.cor = [self.x, self.y, self.z]

    def read(self):
        print(tuple(self.cor))

list_inf = []
for i in range(5):
    x, y, z = input(), input(), input()
    i = Point3D(x, y, z).__dict__
    list_inf.append(i)

print(list_inf)