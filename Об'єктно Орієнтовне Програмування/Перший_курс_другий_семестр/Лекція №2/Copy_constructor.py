import copy
triangle_id = 0

class Triangle:
    def __init__(self,a,b = None,c = None):
        global triangle_id
        if isinstance(a,Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = a
            self.c = a

        self.id = triangle_id
        triangle_id += 1


    def piv_per(self):
        return (self.a + self.b + self.c) / 2

    def square(self):
        p = self.piv_per()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def show(self):
        print("Triangle, id = ", self.id, self.a, self.b,self.c)


if __name__ == '__main__':
    t1 = Triangle(3,4,5)
    t1.show()
    t3 = Triangle(t1)
    t3.show()