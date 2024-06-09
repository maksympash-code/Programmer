# Кількість тризначних чисел, які можна утворити з цифр 3, 4, 5, і 6
from itertools import product

# Всі можливі цифри
digits = [3, 4, 5, 6]

# Усі можливі комбінації з трьох цифр
combinations = list(product(digits, repeat=3))

# Кількість таких комбінацій
number_of_combinations = len(combinations)
print(number_of_combinations)
