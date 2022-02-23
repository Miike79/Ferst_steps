# Компьютер должен отгадать загаданное число

import random

X = 1
Y = 100
z = random.randrange(X, Y)
tries = 1

print("\tЗдравствуйте! Давайте поиграем!")
print("\nЗагадайте число от ", X, " до ", Y, ", а я попробую его отгадать.")
print("Я называю число, а вы даете три варианта ответа: ")
print("Если я угадал - отвечаете 'да'.")
print("Если я не угадал, то отвечаете -'больше' или 'меньше'.")
input("\nПридумали число? Нажмите Enter, чтобы начать игру.")
print("\nНачали... ")
print("\nВы загадали это число? - ", z)

answer = input("Ваш ответ : ")
while answer != "да":

    if answer == "больше":
        X = z + 1
        if X == Y:
            print("\nЯ не угадал! Вы загадали число ", X, "!")
            break
        else:
            z = random.randrange(X, Y)
            print("\nВы загадали это число? - ", z)

    elif answer == "меньше":
        Y = z - 1
        if Y == X:
            print("\nЯ не угадал! Вы загадали число ", Y, "!")
            break
        else:
            z = random.randrange(X, Y)
            print("\nВы загадали это число? - ", z)
    answer = input("Ваш ответ : ")
    tries += 1

if answer == "да":
    print("\nУра! Я угадал! Это число ", z, "!")

print("Количество попыток: ", tries)
input("\nНажмите Enter, чтобы выйти.")
