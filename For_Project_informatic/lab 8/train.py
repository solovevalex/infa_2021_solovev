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

    def change(self, x=0, y=0, z=0):
        self.cor = [x, y, z]

    def read(self):
        print(tuple(self.cor))


pt = Point3D(4, 5, 6)
pt.read()
pt.change(1, 1, 1)
pt.read()
