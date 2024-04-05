from Figure import *

class Trapezoid(Figure):
    def __init__(self, a: float,b: float,c: float,d:float):
        super().__init__()
        assert a > 0 and b > 0 and c > 0 and d > 0
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def is_Trapeze(self):
        if (self.a**2 + self.b**2 + self.c**2 + self.d**2 == 0) or (self.a == self.b) or \
           (self.a + self.b <= self.c + self.d) or \
           (abs(self.a - self.b) + self.d <= self.c or self.c + self.d <= abs(self.a - self.b) or abs(self.a - self.b) + self.c <= self.d):
            return False

    def dimention(self):
        self.dim.append(self.a)
        self.dim.append(self.b)
        return len(self.dim)

    def perimeter(self):
        self.perimeter = self.a + self.b + self.c + self.d
        return self.perimeter

    def height(self):
        self.height = (self.c ** 2 - ((self.a - self.b) / 2)**2) ** 0.5
        return self.height
    def square(self):
        self.square = ( (self.a + self.b)/ 2 ) * self.height()
        return self.square

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def volume(self):
        return self.square


if __name__ == '__main__':
    tr = Trapezoid(5,8,6,9)
    print(f"Вимірність = {tr.dimention()}")
    print(f"Периметр = {tr.perimeter()}")
    print(f"Площа трапеції = {tr.square()}")
    print(f"Площа бічної поверхні = {tr.square_surface()}")
    print(f"Площа основи  = {tr.square_base()}")
    print(f"Висота = {tr.height}")
    print(f"Площа = {tr.volume()}")