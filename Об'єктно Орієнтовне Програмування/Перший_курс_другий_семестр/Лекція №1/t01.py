class Cat:
    def __init__(self,name):
        self.name = name
        self.age = 0
        pass

    def growUp(self):
        self.age += 1

    def bite(self, other):
        print(f"Cat{self.name} bite{other.name}")


    def miu(self):
        print(f"{self.name} says: Miu")

cat_Vasya = Cat(" Vasya")
cat_Kuzia = Cat(" Kuzia")

# cat_Vasya.miu()
# cat_Kuzia.miu()

print(cat_Kuzia.age)
cat_Kuzia.growUp()
cat_Kuzia.growUp()
cat_Kuzia.growUp()
cat_Kuzia.growUp()
print(cat_Kuzia.age)

# print(cat_Vasya.name)

# cat_Vasya.bite(cat_Kuzia)