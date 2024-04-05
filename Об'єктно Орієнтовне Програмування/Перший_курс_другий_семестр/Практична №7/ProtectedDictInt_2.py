class ProtectedDictInt(dict): # не рекомендований спосіб(можливо хакнути систему)
    def __setitem__(self, key, value):
        assert type(key) == int, "Ключі мають бути цілими"
        assert key not in self, "Заборонена операція зміни значення за ключем"

        # self[key] = value - не можемо робити, бо буде рекурсія
        # self.__setitem__(key, value) - не можемо робити, бо буде рекурсія
        super().__setitem__(key,value) # викликаємо квадратні дужки з батьківського класу


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "world"
    # d [23] = "world"
    # d["hello"] = "WORLD" # Заборонено
    print(d)
    print(23 in d)
    print(2323 in d)
    d.update({"Hello": "World"})
    print(d)
