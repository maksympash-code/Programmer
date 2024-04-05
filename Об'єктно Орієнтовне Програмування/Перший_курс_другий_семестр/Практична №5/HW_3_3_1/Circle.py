from Figure import *
from math import *
class Circle(Figure):
    def __init__(self,r):
        super().__init__()
        self.r = r
        assert r > 0

    def dimention(self):
        return 2

    def perimeter(self):
        self.p = 2*pi*self.r
        return self.p

    def square(self):
        return pi * (self.r ** 2)

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        return None

    def volume(self):
        return pi * (self.r ** 2)
