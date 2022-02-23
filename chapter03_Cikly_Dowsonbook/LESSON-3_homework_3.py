# Отгадай число за 5 попыток
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число и компьютер говорит
# предположение больше/меньше, чем заданное число
# или попало в точку

import random

print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число в диапазоне о 1 до 100.")
print("Постарайся отгадать его за 5 попыток.\n")
# начальные значения
the_number=random.randint(1, 100)
guess = 0
tries = 1
while guess == 0:
    try:
        guess=int(input("Ваше предположение: "))
    except ValueError:
        print('Это не число!')
    else:
        if guess==the_number:
            print("\nВам удалось отгадать число! Это в самом деле",the_number)
        # цикл отгадывания
        while guess != the_number:
            if guess>the_number:
                print("Меньше...")
            elif guess<the_number:
                print("Больше...")
            elif guess==the_number:
                print("Это правильный ответ!")
            guess=int(input("Ваше предположение: "))
            tries+=1
            if guess==the_number:
                print("\nВам удалось отгадать число! Это в самом деле",the_number)
            if tries==5 and guess!=the_number:
                print("\nВы не угадали, правильный ответ - ",the_number," !")
                print("ВЫ САМОЕ СЛАБОЕ ЗВЕНО, ПРОЩАЙТЕ!!!")
                break
                # команда break, чтобы прога не продолжала задавать вопросы
print("Вы затратили на отгадывание ",tries," попыток!\n")        
input("\nНажмите Enter, чтобы выйти.")