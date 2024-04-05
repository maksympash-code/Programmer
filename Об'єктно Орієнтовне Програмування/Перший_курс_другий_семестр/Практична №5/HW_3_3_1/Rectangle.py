from Figure import *

class Rectangle(Figure):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b
        assert self.a > 0 and self.b > 0
    def dimention(self):
            self.dim.append(self.a)
            self.dim.append(self.b)
            return len(self.dim)

    def perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter
    def square(self):
        return self.a*self.b

    def square_surface(self):
        return None

    def square_base(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.a * self.b


if __name__ == '__main__':
    r1 = Rectangle(2,3)
    print(f"Вимірність = {r1.dimention()}")
    print(f"Периметр = {r1.perimeter()}")
    print(f"Площа прямокутника = {r1.square()}")
    print(f"Площа бічної фігури = {r1.square_surface()}")
    print(f"Площа основи фігури = {r1.square_base()}")
    print(f"Висота = {r1.height()}")
    print(f"Площа фігури = {r1.volume()}")
