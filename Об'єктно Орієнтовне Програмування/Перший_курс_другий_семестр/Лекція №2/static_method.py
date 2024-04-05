import copy
from random import randint

class Triangle:
    triangle_id = 0 # Статичне поле класу
    @staticmethod # декоратор, що позначає використання статичного методу
    def get_triangle_id():
        return Triangle.triangle_id

    @staticmethod # декоратор, що позначає використання статичного методу
    def gen_triangle_id():
        return randint(1, 100000)
    def __init__(self,a,b = None,c = None):
        if isinstance(a,Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = a
            self.c = a

        self.id = Triangle.triangle_id # Звертаємось через ім'я класу(статичний метод) або
        Triangle.triangle_id += 1


    def piv_per(self):
        return (self.a + self.b + self.c) / 2

    def square(self):
        p = self.piv_per()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def show(self):
        print("Triangle, id = ", self.id, self.a, self.b,self.c)


if __name__ == '__main__':
    # t1 = Triangle(3,4,5)
    # t1.show()
    # t3 = Triangle(t1)
    # t3.show()
    print(Triangle.triangle_id)
    print(Triangle.get_triangle_id())
    print(Triangle.gen_triangle_id())