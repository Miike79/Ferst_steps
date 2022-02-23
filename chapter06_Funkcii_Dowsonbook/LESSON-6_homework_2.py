# Компьютер должен отгадать загаданное число, нужно применить формулу ask_number
import random

X = 1
Y = 100
z = random.randrange(X, Y)
answer = None
tries = 1


def intro():
    """ Вступительное слово """
    print("\tЗдравствуйте! Давайте поиграем!")
    print("\nЗагадайте число от ", X, " до ", Y, ", а я попробую его отгадать.")
    print("Я называю число, а вы даете три варианта ответа: ")
    print("Если я угадал - отвечаете 'да'.")
    print("Если я не угадал, то отвечаете -'больше' или 'меньше'.")
    print("\nНачали... ")


def ask_number(question):
    response = None
    while response not in ("да", "больше", "меньше"):
        response = input(question).lower()
    return response


intro()
print("Вы загадали число ", z, " ?")
answer = ask_number("Отвечайте только 'да','больше' или'меньше')")
the_number = z
while answer != "да":
    if answer == "больше":
        X = z + 1
        tries += 1
        if Y - X <= 1:
            X = z + 1
            the_number = X
            print("Вы загадали число ", the_number, "?")
            answer = ask_number("Отвечайте только 'да','больше' или'меньше')")
        else:
            z = random.randrange(X, Y)
            the_number = z
            print("Вы загадали число ", the_number, " ?")
            answer = ask_number("Отвечайте только 'да','больше' или'меньше')")
    elif answer == "меньше":
        Y = z - 1
        tries += 1
        if Y - X <= 1:
            Y = z - 1
            the_number = Y
            print("Вы загадали число ", the_number, "?")
            answer = ask_number("Отвечайте только 'да','больше' или'меньше')")
        else:
            z = random.randrange(X, Y)
            the_number = z
            print("Вы загадали число ", the_number, " ?")
            answer = ask_number("Отвечайте только 'да','больше' или'меньше')")
print("Я угадал! Это число - ", the_number, " ")
print("Потрачено попыток на отгадывание - ", tries, ".")
input("\nНажите Enter, чтобы завершить.")
