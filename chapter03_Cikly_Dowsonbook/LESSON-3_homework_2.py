# Урок 3 Задание 2
# Подбрось монетку 100 раз и узнай сколько орлов и решек
import random
print("\tСчитаем 'орлы' и 'решки'")
die1=random.randint(1, 100)
die2=100-die1
input("\nНажмите Enter, чтобы бросить монетки...")
print("\nПосле 100 бросков 'Орел' выпал ",(die1)," раз(а), а 'решка' ",(die2),"раз(а)!")       
input("\nНажмите Enter, чтобы выйти.")

