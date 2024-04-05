class Integer:
    def __init__(self,integer):
        self.integer = integer
        assert int(integer) == integer

    def print(self):
        print(self.integer)

    def add(self, other):
        return Integer(self.integer + other.integer)

i1 = Integer(7)
i2 = Integer(4)
i_res = i1.add(i2)
i_res.print()


class Rational(Integer):
    def __init__(self, integer, denominator):
        if type(integer) == Rational:
            super().__init__(integer)
            self.den = denominator
        else:
            super().__init__(integer)
            assert denominator !=0 and type(denominator) == int
            self.den = denominator


    def print(self):
        print(f"{self.integer} / {self.den}")

    def add(self,other):
        if type(other) == Integer:
            return Rational(self.integer + (other.integer * self.den), self.den)
        elif type(other) == Rational:
            num = self.integer * other.den + self.den * other.integer
            den = self.den * other.den
            return Rational(num, den)

r1 = Rational(2,3)
i3 = Integer(7)
r2 = Rational(15,2)

result = r1.add(i3).add(r2)
result.print()

