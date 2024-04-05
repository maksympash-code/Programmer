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
            for key,value in other.items():
                res[key] = value
                return ProtectedDictInt(res)








if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = "Hello"
    d3 = d + {34,"234"}
    print(d3)




