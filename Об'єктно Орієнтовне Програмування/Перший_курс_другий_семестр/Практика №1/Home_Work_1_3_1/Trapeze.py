class Trapeze:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def is_Trapeze(self):
        if (self.a**2 + self.b**2 + self.c**2 + self.d**2 == 0) or (self.a == self.b) or \
           (self.a + self.b <= self.c + self.d) or \
           (abs(self.a - self.b) + self.d <= self.c or self.c + self.d <= abs(self.a - self.b) or abs(self.a - self.b) + self.c <= self.d):
            return False

    def perimeter(self):
        return (self.a + self.b + self.c + self.d)

    def area(self):
        h = (self.c ** 2  - ((self.a - self.b) / 2)**2) ** 0.5
        return( (self.a + self.b)/ 2 ) * h

    def __str__(self) -> str:
        return f"Trapeze: a={self.a}, b={self.b}, c={self.c}, d={self.d}"


