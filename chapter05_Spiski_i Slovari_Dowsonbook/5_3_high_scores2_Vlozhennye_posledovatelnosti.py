# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores=[]
choice=None
while choice != "0":
    print(
    """
    Рекорды 2.0
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    """
    )
    choice=input("Ваш выбор: ")
    print()
    # выход
    if choice=="0":
        print("До свидания.")
    # вывод таблицы рекордов
    elif choice=="1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            # эта строка кода не понятна
            score,name=entry
            print(name,"\t",score)
    # добавление результата как вложенного кортежа
    elif choice=="2":
        name=input("Впишите имя игрока: ")
        score=int(input("Впишите его результат: "))
        entry=(score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores=scores[:5] # в списке остается только 5 рекордов
    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта",choice)
input("\nНажмите Enter, чтобы выйти.")        
    
    
