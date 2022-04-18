# Простая игра
# Демонстрирует импорт модулей.

# глава 9 учебника Доусона

# импортируем модуль games, который сами создали
import games,random

print("Добро пожаловать в самую-самую простую игру!\n")
# задаем переменную продолжения игры
again=None
while again!="n":
    players=[]
    # импорт с помощью точечной нотации: имя_модуля.имя_функции
    num=games.ask_number(question="Сколько игроков участвует? (2-5): ",low=2,high=5)
    # для каждого игрока из выбранного количества
    for i in range(num):
        name=input("Имя игрока: ")
        score=random.randrange(100)+1
        player=games.Player(name,score)
        players.append(player)
    print("\nВот результаты игры: ")
    for player in players:
        print(player)
    again=games.ask_yes_no("\nХотите сыграть ещё раз? (y/n): ")
input("Нажмите Enter, чтобы выйти.")
