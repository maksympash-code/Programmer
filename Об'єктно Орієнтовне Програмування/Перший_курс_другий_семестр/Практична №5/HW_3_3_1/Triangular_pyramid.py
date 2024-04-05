import math

from Triangle import *

class Triangular_pyramid(Triangle):
    def __init__(self,h,a):
        super().__init__(x1 = None, x2 = None, x3 =None)
        self.a = a
        self.h = h


    def dimention(self):
        return 3

    def perimeter(self):
        self.p = self.a * 3
        return self.p

    def square(self):
        self.s = (math.sqrt(3)/ 4) * self.x1 ** 2
        return self.s

    def square_surface(self):
        self.surface = 1/2 * (self.p * self.h)
        return self.surface

    def square_base(self):
        self.base = self.s
        return self.base

    def height(self):
        return self.h

    def volume(self):
        self.volume = 1/3 * (self.base * self.h)
        return self.volume

if __name__ == '__main__':
    t_p = Triangular_pyramid(7,5)
    print(f"Вимірність = {t_p.dimention()}")
    print(f"Периметр основи = {t_p.perimeter()}")
    print(f"Площа = {t_p.square()}")
    print(f"Площа бічної поверхні = {t_p.square_surface()}")
    print(f"Площа основи піраміди = {t_p.square_base()}")
    print(f"Висота = {t_p.height()}")
    print(f"Об'єм піраміди = {t_p.volume()}")