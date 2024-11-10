from random import *

def guess_number():
    print("Це гра вгадай число!")
    random_number = randint(1, 100)
    counter = 1

    while True:
        try:
            guess_number = int(input('Введіть число від 1 до 100: '))
            counter += 1

            if guess_number == random_number:
                print(f'Ви вгадали число {random_number} за {counter} разів')
                break
            elif guess_number < random_number:
                print('Ви не вгадали! Число більше за те що ви назвали.')
            elif guess_number > random_number:
                print('Ви не вгадали! Число менше за те що ви назвали.')
        except ValueError:
            print('Введіть коректно число.')

guess_number()