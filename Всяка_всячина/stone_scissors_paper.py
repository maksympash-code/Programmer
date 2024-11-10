from random import *

choices = ['Камінь', 'Ножиці', 'Папір']
print("Це гра 'Камінь, Ножиці, Папір'")

def stone_scissors_paper():
    while True:
        user_answer = input("Виберіть (Камінь, Ножиці, Папір): ")
        if user_answer in choices:
            return user_answer
        else:
            return ValueError("Ви неправильно ввели значення")


player_answer = stone_scissors_paper()
random_answer = choice(choices)

print(f"Ваш вибір: {player_answer}")
print(f"Вибір_компютера: {random_answer}")

if player_answer == random_answer:
    print("Нічия")
elif player_answer == "Камінь" and random_answer == "Ножиці" or player_answer == "Ножиці" and random_answer == "Папір" or player_answer == "Папір" and random_answer == "Камінь":
    print('Ви виграли!')
else:
    print("Ви програли")

