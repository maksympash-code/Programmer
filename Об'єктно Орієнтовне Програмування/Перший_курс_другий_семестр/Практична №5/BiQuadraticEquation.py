from QuadraticEquation import QuadraticEquation

class  BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

    def solve(self):
        set_solutions = set() # множина розв'зківб потім перетворимо результат у кортедж
        solutions_qudratic = super().solve()
        if solutions_qudratic == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        for solution in solutions_qudratic:
            if solution >= 0:
                t1 = solution ** 0.5
                t2 = -t1
                set_solutions.add(t1)
                set_solutions.add(t2)

        return tuple(set_solutions)

if __name__ == '__main__':
    e1 = BiQuadraticEquation(16, -12, 0)
    print(e1)
    print(len(e1.solve()))

    e2 = BiQuadraticEquation(0, 0, 4)
    print(e2)
    print(e2.solve())

    e3 = BiQuadraticEquation(0, 0, 0)
    print(e3)
    print(e3.solve())

    e4 = BiQuadraticEquation(0, 5, 0)
    print(e4)
    print(e4.solve())

    e5 = BiQuadraticEquation(1, 3, 8)
    print(e5)
    print(e5.solve())

    e6 = BiQuadraticEquation(1, 4, 4)
    print(e6)
    print(e6.solve())

    e7 = BiQuadraticEquation(1, -3, 2)
    print(e7)
    print(e7.solve())

    e8 = BiQuadraticEquation(2, -6, 4)
    print(e8)
    print(e8.solve())