class Integer:
    def __init__(self,integer):
        self.integer = integer
        assert int(integer) == integer

    def __str__(self):
        return (f"Integer :{self.integer}")

    def __add__(self, other):
        return Integer(self.integer + other.integer)


i_res = Integer(7) + Integer(4)
print(i_res)


class Rational(Integer):
    def __init__(self, integer, denominator):
        if type(integer) == Rational:
            super().__init__(integer)
            self.den = denominator
        else:
            super().__init__(integer)
            assert denominator !=0 and type(denominator) == int
            self.den = denominator


    def __str__(self):
        return f"Rational : {self.integer} / {self.den}"

    def __add__(self, other):
        if type(other) == Integer:
            return Rational(self.integer + (other.integer * self.den), self.den)
        elif type(other) == Rational:
            num = self.integer * other.den + self.den * other.integer
            den = self.den * other.den
            return Rational(num, den)


result = Rational(2,3) + Integer(7) + Rational(15,2)
print(result)