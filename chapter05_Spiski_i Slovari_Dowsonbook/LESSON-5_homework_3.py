# Программа "Кто твои мама и папа?"
# пользователь вводит имя, программа пишет имя родителей
# пользователь может добавлять, заменять и удалять пары "ребенок-родители"

print(
    """
        Перед вами игра-справочник по родственным связям
                     "Кто твои папа и мама?"
    Игрок задает имя ребенка, а программа отвечает, кто его отец и мать.
     Игрок может добавлять, заменять и удалять пары "ребенок-родители""")

choice = None
family = {}

while choice != "0":
    choice = input("""\t
                        0. Выход
                        1. Добавить пару
                        2. Узнать пару
                        3. Заменить пару
                        4. Удалить пару
                        
                       Выберите пункт меню: """)

    if choice == "0":
        print("До свидания.")

    elif choice == "1":
        name = input("Введите имя ребенка: ")
        if name in family:
            print("Эта семья уже существует, попробуйте новое имя.")
        else:
            dad = input("Введите имя отца: ")
            mom = input("Введите имя матери: ")
            fam = [dad, mom]
            family[name] = fam
            print("Создана новая пара: у ребенка -", name, ": отец -", fam[0], ", а мать -", fam[1])

    elif choice == "2":
        name = input("Введите имя ребенка: ")
        if name not in family:
            print("Пара ", name, "- отец и мать не создана или не известна.")
        else:
            parents = family[name]
            daddy = parents[0]
            mommy = parents[1]
            print("У ребенка -", name, "родители : отец - ", daddy, ", мать - ", mommy)

    elif choice == "3":
        print("Вы можете поменять имена родителей в паре.")
        name = input("Введите имя ребенка: ")
        if name not in family:
            print("Такого варианта ответа нет, попробуте другой.")
        else:
            parents = family[name]
            daddy = parents[0]
            mommy = parents[1]
            print("У ребенка -", name, "родители : отец - ", daddy, ", мать - ", mommy)
            new_dad = input("Введите новое имя отца: ")
            new_mom = input("Введите новое имя матери: ")
            new_fam = [new_dad, new_mom]
            family[name] = new_fam
            print("Изменена пара: теперь у ребенка -", name, "родители : отец - ", new_dad, ", мать - ", new_mom)

    elif choice == "4":
        delete_name = input("Какую пару Вы хотите удалить? Напишите имя ребенка: ")
        if delete_name in family:
            del family[delete_name]
            print("Пара удалена.")
        else:
            print("Такого варианта ответа нет, попробуте другой.")
    else:
        print("Извините, в меню нет пункта", choice)

input("\n\nВведите Enter, чтобы выйти.")
