from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2

    def is_Circle(self):
        if self.r == 0:
            return False

