class rational_number:
    def __init__(self, n,d):
        self.n = n
        self.d = d


    def print(self):
        print(f"{self.n} / {self.d}")

    def add(self, other):
        n = self.n * other.d + other.n * self.d
        d = self.d * other
        return rational_number(n,d)

    def multi(self):
        n = self.n * n
        return rational_number(n,self.d)
r1 = rational_number(2,3)

