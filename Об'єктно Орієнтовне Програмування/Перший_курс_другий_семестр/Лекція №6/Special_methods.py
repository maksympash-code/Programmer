class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # special method 1
        return f'Vector({self.x}, {self.y})'

    def __add__(self,other): # special method 2
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        elif type(other) == float or type(other) == int:
            x = self.x + other
            y = self.y
            return Vector(x,y)

    # def __call__(self,x):
    #     res = 0
    #     for i, a_i in self.coef.items():
    #         res += a_i * x**i
    #     return res

v = Vector(1,2) + Vector(3,4) + 6
print(v.__dict__)
print(Vector.__dict__)

