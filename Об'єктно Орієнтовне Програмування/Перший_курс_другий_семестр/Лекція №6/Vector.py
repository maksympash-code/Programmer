class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): # special method
        return f'Vector({self.x}, {self.y})'

    def __add__(self,other): # special method
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        elif type(other) == float or type(other) == int:
            x = self.x + other
            y = self.y
            return Vector(x,y)

    @staticmethod
    def add(v1,v2):
        return Vector(v1.x+v2.x,v1.y+v2.y)

v = Vector(1,2) + Vector(3,4)
print(v)

# v1 = Vector(1,2)
# v2 = Vector(3,4)
# print(v1)
# print(v2)
# v3 = Vector.add(v1,v2)
# print(v3)