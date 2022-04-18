# Перемещение по локациям
# Создайте ООП-игру, в которой игрок сможет менять свое местонахождение
# перемещаясь каждый раз в одно из мест, ближайших данному

# глава 9 учебника Доусона

class Player(object):
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def __str__(self):
        rep = str(self.name)
        return rep

    def show_info(self):
        print("Покупатель ", self.name, ", локация", end="")
        if self.place:
            print(" -", self.place)
        else:
            print(" не определена")

    def change_location(self, new_location):
        self.place = new_location


class Place(object):
    def __init__(self, room, doors):
        self.room = room
        self.doors = doors
        self.persons = []

    def __str__(self):
        rep = str(self.room)
        return rep

    def show_info(self):
        print("Локация '", self.room, "',покупатели в локации: ", end="")
        if not self.persons:
            print("отсутствуют.")
        else:
            for player in self.persons:
                print(player.__str__())
        print("Доступные локации: ", self.doors[:])

    def add_person(self, player):
        self.persons.append(player)

    def remove_person(self, player):
        self.persons.remove(player)

    def clear_persons(self):
        self.persons.clear()


class Game(object):
    def __init__(self):
        self.player = Player(name, None)
        self.places = []

    def in_game(self):
        answer = None
        while answer != "н":
            answer = input("\nБудете делать следующий ход (д/н)? ")
            if answer == "д":
                self.change_place()
            elif answer != "н":
                print("Ответ не верный. Попробуйте ещё.")
            else:
                print("До свидания.")

    def change_place(self):
        stop_transfer = None
        while stop_transfer != 1:
            for place in self.places:
                if self.player in place.persons:
                    rooms = place.doors
                    print("\nПокупатель", self.player, " в локации", place.room,
                          ", доступные для перемещения локации: ", rooms)
                    choise = input("В какую локацию пройти? ")
                    while choise not in rooms[:]:
                        print("Такой локации не существует, выберите другую.")
                        choise = input("В какую локацию пройти? ")
                    else:
                        print("Покупатель", self.player, " перемещается в локацию ", choise)
                        place.remove_person(self.player)
                        self.player.change_location(choise)
                        for place in self.places:
                            if choise == place.room:
                                place.add_person(self.player)
                        stop_transfer = 1
                        break

    def actual_info(self):
        for place in self.places:
            place.show_info()

    def play(self):
        hunter = Place("Мясо", doors=["Рыночная площадь", "Рыба", "Бакалея", "Яйца"])
        self.places.append(hunter)
        fisher = Place("Рыба", doors=["Рыночная площадь", "Мясо", "Бакалея", "Яйца"])
        self.places.append(fisher)
        meal = Place("Бакалея", doors=["Рыночная площадь", "Мясо", "Рыба", "Яйца"])
        self.places.append(meal)
        eggs = Place("Яйца", doors=["Рыночная площадь", "Мясо", "Рыба", "Бакалея"])
        self.places.append(eggs)
        outdoor = Place("Рыночная площадь", doors=["Мясо", "Рыба", "Бакалея", "Яйца"])
        self.places.append(outdoor)
        if self.player:
            self.player.place = outdoor
            outdoor.add_person(self.player)
        self.in_game()


print("Перед Вами пошаговая игра \"Поход за продуктами\".\n")
name = input("Введите имя покупателя для начала игры: ")
print("\nПокупатель", name, " пришел(ла) на Рыночную площадь за продуктами.")
game = Game()
game.play()

input("\nНажмите Enter, чтобы выйти.")