class Rectangle:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return (self.a * self.b)

    def is_Rectangle(self):
        if self.a == 0 or self.b == 0:
            return False
        else:
            return True

    def __str__(self) -> str:
        return f"Rectangle: a={self.a}, b={self.b}"
