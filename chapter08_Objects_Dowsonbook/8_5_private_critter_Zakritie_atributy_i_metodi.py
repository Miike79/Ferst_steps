# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы

# глава 8 учебника Доусона
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name  # ткрытый атрибут
        self.__mood = mood  # закрытый атрибут

    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()


# основная часть
crit = Critter(name="Бобик", mood="прекрасно")
crit.talk()
crit.public_method()
print()
# если написать команду print(crit.mood), то будет ошибка, т.к.
# напрямую атрибут mood извлечь нельзя, он закрыт
# вот такой есть технический способ открыть закрытый атрибут __mood
print(crit._Critter__mood)
input("\nНажмите Enter, чтобы выйти")
