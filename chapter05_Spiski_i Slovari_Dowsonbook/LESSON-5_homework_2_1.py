# Генератор персонажей
# Пользователю дано 30 пунктов, которые он может распределить персонажу
# в характеристики -сила, здоровье,ловкость и мудрость
# пользователь может не только брать их, но и возвращать

# объяснение правил
print(
    """
             Добро пожаловать в редактор персонажа!
    Здесь вы можете создать персонажа с уникальными характеристиками:
           'Сила', 'Здоровье', 'Ловкость' и 'Мудрость'
     В эти характеристики можно внести суммарно 30 очков талантов.

                  Меню:
                0 - Выйти
                1 - Создание персонажа
                2 - Статистика персонажей
                3 - Перераспределить очки талантов
                4 - Удалить персонажа
    """)
choice = None
heroes = {}
scores = []
name = None
hero = None
new_hero = None
base_strength = ["Сила", 0]
strength = base_strength
base_health = ["Здоровье", 0]
health = base_health
base_agility = ["Ловкость", 0]
agility = base_agility
base_wisdom = ["Мудрость", 0]
wisdom = base_wisdom
while choice != "0":
    choice = input("\nВыберите пункт меню: ")
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        max = int("30")
        hero = input("Придумайте имя персонажу: ")
        if hero not in heroes:
            total = ""
            while total != max and total != 0:
                print("\nДоступно к распределению ", max, " очков талантов.")
                strength[1] = int(input("Сколько очков добавить к силе? "))
                ost1 = max - int(strength[1])
                print("\nОсталось не распределенных очков -", ost1)
                health[1] = int(input("Сколько очков добавить к здоровью? "))
                ost2 = int(ost1) - int(health[1])
                print("\nОсталось не распределенных очков -", ost2)
                agility[1] = int(input("Сколько очков добавить к ловкости? "))
                ost3 = int(ost2) - int(agility[1])
                print("\nОсталось не распределенных очков -", ost3)
                wisdom[1] = int(input("Сколько очков добавить к мудрости? "))

                total = int(strength[1]) + int(health[1]) + int(agility[1]) + int(wisdom[1])
                if total > 30:
                    print("Вы распределили больше очков, чем возможно, попробуйте заново.\n")
                elif total != 30:
                    print("У вас осталось не распределенных очков -", max - total, ", попробуйте заново.\n")
                else:
                    print("\nОтлично! Вы создали персонажа со следующими харктеристиками: ")
                    print("Герой '", hero, "': Сила -", strength[1], "Здоровье -", health[1], "Ловкость -", agility[1],
                          "Мудрость -", wisdom[1])
                    scores = [strength[1], health[1], agility[1], wisdom[1]]
                    heroes[hero] = scores
        else:
            print("Персонаж ", hero, " уже создан.")
    elif choice == "2":
        print("\nСписок созданных персонажей:")
        print("\nПерсонаж |\tСила |\tЗдоровье |\tЛовкость |\tМудрость")
        print(heroes)
    elif choice == "3":
        print("\nСписок созданных персонажей:")
        print("\nПерсонаж |\tСила |\tЗдоровье |\tЛовкость |\tМудрость")
        print(heroes)
        name = input("Введите имя персонажа, которого хотите изменить: ")
        if name in heroes:
            print("Распределите заново очки талантов для ", name, ": ")
            max = int("30")
            total = ""
            while total != max and total != 0:
                print("\nДоступно к распределению ", max, " очков талантов.")
                heroes[name][0] = int(input("Сколько очков добавить к силе? "))
                ost1 = max - int(heroes[name][0])
                print("\nОсталось не распределенных очков -", ost1)
                heroes[name][1] = int(input("Сколько очков добавить к здоровью? "))
                ost2 = int(ost1) - int(heroes[name][1])
                print("\nОсталось не распределенных очков -", ost2)
                heroes[name][2] = int(input("Сколько очков добавить к ловкости? "))
                ost3 = int(ost2) - int(heroes[name][2])
                print("\nОсталось не распределенных очков -", ost3)
                heroes[name][3] = int(input("Сколько очков добавить к мудрости? "))
                total = int(heroes[name][0]) + int(heroes[name][1]) + int(heroes[name][2]) + int(heroes[name][3])
                if total > 30:
                    print("Вы распределили больше очков, чем возможно, попробуйте заново.\n")
                elif total != 30:
                    print("У вас осталось не распределенных очков -", max - total, ", попробуйте заново.\n")
                else:
                    print("\nХарактеистики ", name, " изменены.")
        else:
            print("Персонажа ", name, " нет в списке созданных.")
    elif choice == "4":
        print("\nСписок созданных персонажей:")
        print(heroes)
        hero = input("\nКакого персонажа вы хотите удалить?: ")
        if hero in heroes:
            del heroes[hero]
            print("Персонаж ", hero, " удален.")
        else:
            print("Персонажа ", hero, " нет в списке.")
    else:
        print("Извините, в меню нет пункта", choice)
input("\n\nВведите Enter, чтобы выйти.")
# программа решает верно, но внешний вид ужасен