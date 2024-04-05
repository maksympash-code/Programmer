class Waiter:
    def __init__(self, name):
        self._waiter_name = name
        self.a = "Waiter: 0 "
        self.b = "Waiter: 1"


class Singer:
    def __init__(self, name):
        self._name = name
        self.a = 'Singer: Hello'
        self.b = 'Singer: World'


# class SingerWaiter(Singer, Waiter):
#     def __init__(self, name):
#         Singer.__init__(self, name)
#         Waiter.__init__(self, name)

class SingerWaiter():
    def __init__(self,name):
        self.singer = Singer(name)
        self.waiter = Waiter(name)


sw = SingerWaiter('Eduard')
# self._name = name #from Singer
# self._name = name # from Waiter

print(sw.singer.a)
print(sw.singer.b)
print(sw.waiter.a)
print(sw.waiter.b)