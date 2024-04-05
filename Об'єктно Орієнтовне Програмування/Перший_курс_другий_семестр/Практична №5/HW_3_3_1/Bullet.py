import math
from Figure import *

class Bullet(Figure):
    def __init__(self,r):
        super().__init__()
        self.r = r
        assert self.r > 0

    def dimention(self):
        return 3

    def perimeter(self):
        self.p = 2 * math.pi * self.r
        return self.p

    def square(self):
        self.square = math.pi * (self.r**2)
        return self.square

    def square_surface(self):
        return 4 * math.pi * self.r

    def square_base(self):
        return self.square

    def height(self):
        return self.r
    def volume(self):
        return (4/3) * math.pi * (self.r ** 3)

if __name__ == '__main__':
    b = Bullet(8)
    print(f"Вимірність = {b.dimention()}")
    print(f"Довжина кола = {b.perimeter()}")
    print(f"Площа кола = {b.square()}")
    print(f"Площа бічної поверхні = {b.square_surface()}")
    print(f"Площа основи кулі = {b.square_base()}")
    print(f"Висота = {b.height()}")
    print(f"Об'єм кулі = {b.volume()}")
