class Polinom:
    def __init__(self):
        self.coef = {}

    def set_coef(self, i , a_i):
        self.coef[i] = a_i

    def __str__(self):
        s = ""
        for k in sorted(self.coef.keys())[:0:-1]:
            s += f"{self.coef[k]}x**{k} + "
        return s + f"{self.coef[0]}"

    def __call__(self,x):
        res = 0
        for i, a_i in self.coef.items():
            res += a_i * x**i
        return res



if __name__ == '__main__':
    p = Polinom()
    p.set_coef(0,7)
    p.set_coef(2,2)
    print(p)

    x = 5
    y = p(x) # Обчислюємо значення поліному при x = 5
    print(f"Значення полінома {p}: для x = {x} та y = {y}") # Значення