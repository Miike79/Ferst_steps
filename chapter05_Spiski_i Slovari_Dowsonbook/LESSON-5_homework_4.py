# Программа "Кто твои мама и папа? - 2"
# пользователь вводит имя, программа пишет имя родителей
# пользователь может добавлять, заменять и удалять пары "ребенок-родители"
# добавляется дедушка и бабушка

print(
    """
                 Перед вами игра-справочник по родственным связям
                            "Кто твои родственники?"
    Игрок задает имя ребенка, а программа отвечает, кто его отец, мать, бабушка и дедушка.
          Игрок может добавлять, заменять и удалять имена родственников.
          
          *при написании в точности соблюдайте раскладку и размер букв""")

choice = None
family = {}
PERSONS = ("отец","мать","дедушка отца","бабушка отца","дедушка матери","бабушка матери")
while choice != "0":
    choice = input("""\t
                        0. Выход
                        1. Добавить родственников
                        2. Узнать родственников
                        3. Заменить родственников
                        4. Удалить родственников
                        
                       Выберите пункт меню: """)

    if choice == "0":
        print("До свидания.")

    elif choice == "1":
        name = input("Введите имя ребенка: ")
        if name in family:
            print("Эта семья уже существует, попробуйте новое имя.")
        else:
            dad = input("Введите имя отца: ")
            dad_dad = input("Введите имя дедушки отца: ")
            dad_mom = input("Введите имя бабушки отца: ")
            grand_dad = [dad_dad, dad_mom]
            mom = input("Введите имя матери: ")
            mom_dad = input("Введите имя дедушки матери: ")
            mom_mom = input("Введите имя бабушки матери: ")
            grand_mom = [mom_dad, mom_mom]
            dad_fam = [dad, grand_dad]
            mom_fam = [mom, grand_mom]
            fam = [dad_fam, mom_fam]
            family[name] = fam
            print("\nСоздана новая семья: у ребенка -", name, ": ",PERSONS[0]," -", dad, ", а ",PERSONS[1]," -", mom)
            print("Родители отца ",dad,": ",PERSONS[2]," - ",dad_dad,", ",PERSONS[3]," - ",dad_mom)
            print("Родители матери ",mom,": ",PERSONS[4]," - ", mom_dad, ", ",PERSONS[5]," - ", mom_mom)

    elif choice == "2":
        name = input("Введите имя ребенка: ")
        if name not in family:
            print("Родственники ребенка ", name, " не известны.")
        else:
            parents = family[name]
            dad = parents[0][0]
            mom = parents[1][0]
            dad_dad = parents[0][1][0]
            dad_mom = parents[0][1][1]
            mom_dad = parents[1][1][0]
            mom_mom = parents[1][1][1]
            print("\nУ ребенка -", name, ": ", PERSONS[0], " -", dad, ", а ", PERSONS[1], " -", mom)
            print("Родители отца ", dad, ": ", PERSONS[2], " - ", dad_dad, ", ", PERSONS[3], " - ", dad_mom)
            print("Родители ", mom, ": ", PERSONS[4], " - ", mom_dad, ", ", PERSONS[5], " - ", mom_mom)

    elif choice == "3":
        print("Вы можете поменять имена родственников ребенка.")
        name = input("Введите имя ребенка: ")
        if name not in family:
            print("Такого варианта ответа нет, попробуте другой.")
        else:
            parents = family[name]
            dad = parents[0][0]
            mom = parents[1][0]
            dad_dad = parents[0][1][0]
            dad_mom = parents[0][1][1]
            mom_dad = parents[1][1][0]
            mom_mom = parents[1][1][1]
            print("\nУ ребенка -", name, ": ", PERSONS[0], " -", dad, ", а ", PERSONS[1], " -", mom)
            print("Родители отца ", dad, ": ", PERSONS[2], " - ", dad_dad, ", ", PERSONS[3], " - ", dad_mom)
            print("Родители ", mom, ": ", PERSONS[4], " - ", mom_dad, ", ", PERSONS[5], " - ", mom_mom)
            change_name = input("\nИмя какого родственника вы хотите изменить?: ").lower()
            while change_name not in PERSONS:
                print("Такого родственника в семье нет.")
                change_name = input("\nИмя какого родственника вы хотите изменить?: ").lower()
            if change_name == PERSONS[0]:
                print("\nИмя отца ",parents[0][0])
                new_dad = input("\nВведите новое имя отца: ")
                parents[0][0] = new_dad
                name = change_name
                dad_fam = [new_dad, grand_dad]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")
            elif change_name == PERSONS[1]:
                print("\nИмя матери ", parents[1][0])
                new_mom = input("\nВведите новое имя матери: ")
                parents[1][0] = new_mom
                name = change_name
                mom_fam = [new_mom, grand_mom]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")
            elif change_name == PERSONS[2]:
                print("\nИмя дедушки отца ", parents[0][1][0])
                new_dad_dad = input("\nВведите новое имя дедушки отца: ")
                parents[0][1][0] = new_dad_dad
                name = change_name
                grand_dad = [new_dad_dad, dad_mom]
                dad_fam = [dad, grand_dad]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")
            elif change_name == PERSONS[3]:
                print("\nИмя бабушки отца ", parents[0][1][1])
                new_dad_mom = input("\nВведите новое имя бабушки отца: ")
                parents[0][1][1] = new_dad_mom
                name = change_name
                grand_dad = [dad_dad, new_dad_mom]
                dad_fam = [dad, grand_dad]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")
            elif change_name == PERSONS[4]:
                print("\nИмя дедушки матери ", parents[1][1][0])
                new_mom_dad = input("\nВведите новое имя дедушки матери: ")
                parents[1][1][0] = new_mom_dad
                name = change_name
                grand_mom = [mom, new_mom_dad]
                mom_fam = [mom, grand_mom]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")
            elif change_name == PERSONS[5]:
                print("\nИмя бабушки матери ", parents[1][1][1])
                new_mom_mom = input("\nВведите новое имя бабушки матери: ")
                parents[1][1][1] = new_mom_mom
                name = change_name
                grand_mom = [mom, new_mom_mom]
                mom_fam = [mom, grand_mom]
                fam = [dad_fam, mom_fam]
                family[name] = fam
                print("Изменения внесены в базу")

    elif choice == "4":
        delete_name = input("\nКакую семью Вы хотите удалить? Напишите имя ребенка: ")
        if delete_name in family:
            del family[delete_name]
            print("Семья ребенка ",delete_name," удалена.")
        else:
            print("\nТакой семьи нет в базе, попробуте другое имя ребенка.")
    else:
        print("Извините, в меню нет пункта", choice)

input("\n\nВведите Enter, чтобы выйти.")