# Обработаем
# Демострирует обработку исключительных ситуаций
# try/except

# глава 7 учебника Доусона

try:
    num = float(input("Введите число: "))
except:
    print("Похоже, это не число!")
# обработка исключений определенного типа
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Похоже, это не число!")
# обработка исключений нескольких разных типов
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки. составленные из цифр!")
# получение аргумента
try:
    num = float(input("\nBвeдитe число: "))
except ValueError as e:
    print("Этo не число! Интерпретатор как бы говорит нам:")
    print(e)
# try/except/else
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Этo не число!")
else:
    print("Bы ввели число", num)

input("\nНажмите Enter, чтобы выйти.")

# плохо усвоил, не до конца вник
