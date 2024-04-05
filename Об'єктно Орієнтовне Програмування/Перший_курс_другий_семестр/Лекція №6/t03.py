class Copier:
    def copy(self):
        print("Copier is coping")


class Xerox(Copier):
    pass


class Scaner:
    def copy(self):
        print("Scanner is coping")

    def send(self):
        print("Scanner is sending file via email")

class MFD(Xerox, Scaner):
    pass

    # def copy(self):
    #     print("MFD is coping")
# scanner = Scaner()
# xerox = Xerox()
# xerox.copy()
# scanner.copy()

mfd = MFD()
mfd.copy()
mfd.send()

print(MFD.__mro__) # Функція, яка показує як шукається метод