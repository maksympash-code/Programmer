class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def trykytnik(self):
        ls = [self.a,self.b,self.c]
        ls.sort()
        a,b,c = ls
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        pivper = self.perimetr() / 2
        return (pivper *(pivper - self.a) * (pivper - self.b) * (pivper- self.c))**0.5

    def __str__(self):
        return "Triangle: a = "
tryk = Triangle(2, 4,5)
