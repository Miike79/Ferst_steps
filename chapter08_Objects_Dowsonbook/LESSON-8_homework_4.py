# Моя зверюшка - апгрейд
# Доработать код, чтобы пользователь манипулировал объектами через список

import random

the_number = random.randrange(1, 5)

dict_crit = {}


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, position, hunger=0, boredom=0):
        self.name = name
        self.position = position
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        print("Появился новый объект ", self.name)

    def __pass_time(self):
        self.hunger -= the_number
        self.boredom -= the_number

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness >= 90:
            m = "прекрасно"
        elif 89 >= unhappiness >= 60:
            m = "неплохо"
        elif 59 >= unhappiness >= 30:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Зверюшка", self.name, ": голод", self.hunger, ", бодрость", self.boredom, ", чувствует себя", self.mood)
        self.__pass_time()

    def show_info(self):
        print(self.position, "-", self.name)
        self.__pass_time()

    def eat(self, food):
        print("Мррр.  Спасибо.")
        self.hunger += food
        if self.hunger < 0:
            self.hunger = 0

    def play(self, fun):
        print("Уиии!")
        self.boredom += fun
        if self.boredom < 0:
            self.boredom = 0


def main():
    position = 0
    count = 0
    print("Вы организовали питомник для зверюшек.\n")

    crit_count = int(input("Сколько зверюшек Вы хотите в него поместить? "))

    for i in range(crit_count):
        count += 1
        position += 1
        if position not in dict_crit:
            name = input("\nВведите имя зверюшки: ")
            crit = Critter(name, position, hunger=50, boredom=50)
            Critter.__str__(crit)
            dict_crit[position] = crit

    choice = None
    while choice != "0":
        print \
            ("""
        Моя Зверюшка

        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            for crit in dict_crit:
                Critter.talk(dict_crit[crit])

        # кормление зверюшки
        elif choice == "2":
            print("Список зверюшек.")
            for position in dict_crit:
                name = dict_crit[position]
                name.show_info()
            crit_choose = int(input("Выберите номер зверюшки, которую будете кормить: "))
            while crit_choose not in dict_crit:
                print("Такого номера нет в списке")
                crit_choose = int(input("Выберите номер зверюшки, которую будете кормить: "))
            else:
                if crit_choose in dict_crit:
                    EatNum = int(input("Сколько еды дать этой зверюшке? "))
                    dict_crit[crit_choose].eat(EatNum)

        # игра со зверюшкой
        elif choice == "3":
            print("Список зверюшек.")
            for position in dict_crit:
                name = dict_crit[position]
                name.show_info()

            crit_choose = int(input("Выберите номер зверюшки, с которой будете играть: "))
            while crit_choose not in dict_crit:
                print("Такого номера нет в списке")
                crit_choose = int(input("Выберите номер зверюшки, с которой будете играть: "))
            else:
                if crit_choose in dict_crit:
                    PlayTime = int(input("Сколько раз поиграть с этой зверюшкой? "))
                    dict_crit[crit_choose].play(PlayTime)

        # неправильный ввод
        else:
            print("\nИзвините, в меню нет пункта ", choice)


main()
input("\n\nНажмите enter, чтобы выйти.")
