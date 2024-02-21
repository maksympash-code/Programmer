class Trapeze:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def is_Trapeze(self):
        ls = [self.a, self.b, self.c, self.d]
        self.a,b,c,d = ls[0],ls[1],ls[2], ls[3]
        if self.a != self.b and self.a + self.d == self.c + self.b:
            return True
    def Perimeter(self):
        return (self.a + self.b + self.c + self.d)
    #def Squares(self):

