class Person:
    def __init__(self,name, last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Last name: {self.last_name}, Age:{self.age}"

p = Person("Volodymyr", "Avakumov", 18)
print(p)