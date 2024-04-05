from Equation import Equation

class QuadraticEquation(Equation):
    def __init__(self,a,b,c):
        super().__init__(b,c)
        self.a = a

    def __str__(self):
        return f"{self.a}x**2 + " + super().__str__()

    def disk(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else: # a != 0
            D = self.disk()
            if D < 0:
                return ()
            elif D == 0:
                x1 = -self.b / (2 * self.a)
                return (x1,)

            else: # D > 0
                d_sqr = D ** 0.5
                x1 = (-self.b + d_sqr) / (2 * self.a)
                x2 = (-self.b - d_sqr) / (2 * self.a)
                return (x1,x2)



if __name__ == '__main__':
    e1 = QuadraticEquation(0,  12,   18)
    print(e1)
    print(e1.solve())

    e2 = QuadraticEquation(0,0, 4)
    print(e2)
    print(e2.solve())

    e3 = QuadraticEquation(0,0, 0)
    print(e3)
    print(e3.solve())

    e4 = QuadraticEquation(0,5, 0)
    print(e4)
    print(e4.solve())

    e5 = QuadraticEquation(1, 3, 8)
    print(e5)
    print(e5.solve())

    e6 = QuadraticEquation(1,4,4)
    print(e6)
    print(e6.solve())

    e7 = QuadraticEquation(1,-3,2)
    print(e7)
    print(e7.solve())

    e8 = QuadraticEquation(2, -6,4)
    print(e8)
    print(e8.solve())
