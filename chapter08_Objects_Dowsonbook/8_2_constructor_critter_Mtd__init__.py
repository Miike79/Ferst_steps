# Зверюшка с конструктором
# Демонстрирует метод-конструктор

# глава 8 учебника Доусона
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self):
        print("Появилась на свет новая зверюшка!")

    def talk(self):
        print("\nПpивeт. Я зверюшка - экземпляр класса Critter.")


# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nHaжмитe Enter. чтобы выйти.")
