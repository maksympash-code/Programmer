
def simple_calculator():
    print("Простий калькулятор")
    print("Виберіть дію, яку потрібно виконати з двома числами('+' '-' '*' '/' '%'):")
    operation = input('Виберіть операцію: ')

    if operation in ['+', '-', '*', '/']:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return ValueError("Ділити на 0 не можливо")
        elif operation == '%':
            result = num1 % num2

        return f"Результат: {result}"
    else:
        return "Неправильно введена операція"

print(simple_calculator())
