from ProtectedDictInt_iterator import ProtectedDictInt_iterator

class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}


    def __setitem__(self, key, value):
        assert type(key) == int, "Ключі мають бути цілими"
        assert key not in self, "Заборонена операція зміни значення за ключем"
        self.__dict[key] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __contains__(self, item):
        return item in self.__dict

    def __len__(self):
        return len(self.__dict)

    def __str__(self):
        return f"Protected dict: {self.__dict}"

    def __add__(self, other):
        res = ProtectedDictInt()
        for key, value in self.__dict.items():
            res[key] = value

        if type(other) == tuple:
            assert len(other) % 2 == 0
            for i in range(0,len(other),2):
                res[other[i]] = other[i+1]
                return res

        elif type(other) == dict:
            pass
            # for key,value in other.items():
            #     res[key] = value
            #     return ProtectedDictInt(res)

    def __iter__(self):# спеціальний клас, що повертає екземпляр із Класу Словник
        return ProtectedDictInt_iterator(self)
        # return self.__dict.__iter__() ще один метод що викликає магічний метод

    def keys(self):
        return self.__dict.keys()

    def values(self):
        return self.__dict.values()







if __name__ == '__main__':
    d = ProtectedDictInt()
    d[87] = 98
    d[45] = "333"
    d[23] = "Hello"


    for key in d: # it = iter(d)
        # key = next(it)
        print(key, d[key])




