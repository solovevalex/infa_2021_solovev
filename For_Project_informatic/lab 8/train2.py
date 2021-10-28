list_obj = []

class Point3D:
    'Класс создает точки с координатами. По дефолту координаты равны 0'

    x = 0
    y = 0
    z = 0
    cor =[0,0,0]
    def __init__(self, x=0, y=0, z=0):
        if list_obj == []:
            self.x = x
            self.y = y
            self.z = z
            self.cor = [x, y, z]
        else:

            self.x = list_obj[0]
            self.y = list_obj[1]
            self.z = list_obj[2]
            self.cor = [self.x, self.y, self.z]
    def change(self, x=0, y=0, z=0):
        self.cor = [x, y, z]

    def read(self):
        print(tuple(self.cor))


pt = Point3D(4, 5, 6)
for i in pt.x, pt.y, pt.z:
    list_obj.append(i)
pt1 = Point3D(1,1,1)
print(pt.read())
print(pt1.read())