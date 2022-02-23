# Рекорды
# Демонстрирует списочные методы

# глава 5 учебника Доусона

scores=[]
choice=None
while choice !="0":
    print(
        """
        Рекорды
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - Сортировать список
        """
        )
    choice=input("Ваш выбор: ")
    print()
    # выход
    if choice=="0":
        print("До свидания.")
    # вывод лучших результатов на экран
    elif choice=="1":
        print("Рекорды")
        for score in scores:
            print(score)
    # добавление рекорда - append
    elif choice=="2":
        score=int(input("Впишите свой рекорд: "))
        scores.append(score)
    # удаление рекорда - remove
    elif choice=="3":
        score=int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат",score,"не содержится в списке рекордов.")
    # сортировка рекордов - sort
    elif choice=="4":
        # значение reverse True делает верной сортировку с обратного конца
        scores.sort(reverse=True)
    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта",choice)
input("\nНажмите Enter, чтобы выйти.")        
        
                
               
        
