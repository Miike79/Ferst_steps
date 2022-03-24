# Моя зверюшка - апгрейд
# Доработать код, чтобы пользователь определял количество еды и время игры

# решено с подсказкой

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут ", self.name, " и сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food):
        print("Мррр.  Спасибо.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

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
            crit.talk()
        # кормление зверюшки
        elif choice == "2":
            EatNum = int(input("Сколько еды Вы дадите зверюшке?"))
            crit.eat(EatNum)

        # игра со зверюшкой
        elif choice == "3":
            PlayTime = int(input("Сколько часов Вы будете играть со зверюшкой?"))
            crit.play(PlayTime)

        # неправильный ввод
        else:
            print("\nИзвините, в меню нет пункта ", choice)


main()
input("\n\nНажмите enter, чтобы выйти.")
