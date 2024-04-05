from Figure import *
from math import sqrt
class Triangle(Figure):
    def __init__(self,x1,x2,x3):
        super().__init__()
        assert x1 > 0 and x2 > 0 and x3 > 0
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.sort = [x1, x2, x3]
        self.sort.sort()
        assert self.sort[0] + self.sort[1] > self.sort[2]

    def dimention(self):
        self.dim.append(self.x1)
        self.dim.append(self.x2)
        return len(self.dim)


    def perimeter(self):
        self.perimeter = self.x1 + self.x2 + self.x3
        return self.perimeter

    def square(self):
        self.p = self.perimeter / 2
        self.square = sqrt(self.p * (self.p - self.sort[0]) * (self.p - self.sort[1]) * (self.p - self.sort[2]))
        return self.square

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        self.height = (2 * self.square) / self.x1
        return self.height

    def volume(self):
        return self.square

if __name__ == '__main__':
    triangle = Triangle(3,4,5)
    print(f"Вимірність = {triangle.dimention()}")
    print(f"Периметр = {triangle.perimeter()}")
    print(f"Площа трикутника = {triangle.square()}")
    print(f"Площа бічної фігури = {triangle.square_surface()}")
    print(f"Площа основи фігури = {triangle.square_base()}")
    print(f"Висота = {triangle.height()}")
    print(f"Площа фігури = {triangle.volume()}")
