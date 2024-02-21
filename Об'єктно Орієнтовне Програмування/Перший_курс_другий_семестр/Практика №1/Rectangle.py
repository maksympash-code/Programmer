class Rectangle:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def is_Rectangle(self):
        if self.a == self.c and self.b == self.d :
            return True

    def perimeter(self):
        return (self.a + self.b) * 2
    def squere(self):
        return (self.a * self.b)