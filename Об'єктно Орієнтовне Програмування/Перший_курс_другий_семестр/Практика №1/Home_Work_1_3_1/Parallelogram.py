class Parallelogram:
    def __init__(self, a, b=None, h=None):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        if self.a < self.h:
            return self.b * self.h
        else:
            return self.a * self.h

    def is_Parallelogram(self):
        if self.a**2 + self.b**2 + self.h**2 == 0:
            return False
