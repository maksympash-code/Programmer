def binary_to_decimal(binary_str):
    decimal_value = 0
    length = len(binary_str)

    for i in range(length):
        # Знаходимо позицію числа в зворотньому порядку
        position = length - 1 - i
        # Помножуємо цифру на 2 в ступені позиції і додаємо до суми
        decimal_value += int(binary_str[i]) * (2 ** position)

    return decimal_value

binary_number = input()
decimal_result = binary_to_decimal(binary_number)
print(decimal_result)
