class QadratQuestion:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminant(self):
        return (self.b ** 2 - 4 * self.a * self.c)

    def solved(self):
        if self.diskriminant() < 0:
            return "Not solved"
        elif self.diskriminant() == 0:
            x = -self.b / 2 * self.a
            return [x]
        elif self.diskriminant() > 0:
            x1 = ((-self.b) - (self.diskriminant())**0.5) / 2 * self.a
            x2 = ((-self.b) + (self.diskriminant())**0.5) / 2 * self.a
            ls = [x1,x2]
            ls.sort()
            return ls




