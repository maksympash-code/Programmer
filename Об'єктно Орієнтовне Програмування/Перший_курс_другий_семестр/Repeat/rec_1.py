x = int(input("Введіть будь яке число:"))
k = int(input("Введіть k >= 1:"))

if k >= 1:
    x_k = (x ** k) / k
    print(x_k)
else:
    raise ValueError