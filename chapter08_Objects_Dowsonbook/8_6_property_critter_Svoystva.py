# Зверюшка со свойствами
# Демонстрирует свойства

# глава 8 учебника Доусона
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name

    # свойство декорируется @
    @property
    def name(self):
        return self.__name

    @name.setter  # сначала @, потом имя свойства, потом атрибут свойства
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("\nПривет. Меня зовут", self.name)


# основная часть
crit = Critter("Бобик")
crit.talk()
print("\nМою зверушку зовут ", end="")
print(crit.name)
print("\nПопробую изменить имя зверюшки на Мурзик...")
# атрибут name благодаря свойству name.setter принимает новое значение
crit.name = "Мурзик"
print("\nМою зверушку зовут ", end="")
print(crit.name)
print("\nПопробую изменить имя зверюшки на пустую строку...")
crit.name = ""
print("\nМою зверушку зовут ", end="")
print(crit.name)
input("\nНажмите Enter, чтобы выйти")
