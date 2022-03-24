# Создайте программу, имитирующую телевизор
# Регулируются каналы и громкость в заданных рамках

# решил с подсказкой из интернета

class Tv(object):
    """Имитация телевизора"""

    # создает объект, но не выводит информацию о нем на экран
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume
        print("Вы включили телевизор.")

    # выводит информацию об объекте на экран
    def __str__(self):
        rep = "Каналы " + str(self.channel) + " Громкость " + str(self.volume) + "\n"
        return rep

    def change_channel(self):
        self.channel = 0
        step_ch = None
        # отработка исключения, если будет введено не число, а строка
        while step_ch != int:
            try:
                step_ch = int(input("Выберите канал от 1 до 10: "))
                # цикл закончится, когда будет введено число, а не строка
                break
            except ValueError:
                print("Вы вводите не число!")
        while step_ch not in range(1, 11):
            print("Такого канала нет, попробуйте выбрать снова.")
            step_ch = int(input("\nВыберите канал от 1 до 10: "))
        new_channel = self.channel + step_ch
        self.channel = new_channel
        print("Вы включили ", new_channel, " канал")

    def up_volume(self):
        print("Регулируемый уровень громкости: 0-10")
        print("Сейчас гормкость на уровне ", self.volume)
        if self.volume >= 10:
            print("Это максимальная громкость.")
        else:
            up = None
            while up != int:
                try:
                    up = int(input("\nНа сколько прибавить громкость? "))
                    break
                except ValueError:
                    print("Вы вводите не число!")
            step_up = self.volume + up
            if step_up > 10:
                print("Максимальная громкость 10, нельзя увеличить на ", up)
            else:
                self.volume = step_up

    def down_volume(self):
        print("Регулируемый уровень громкости: 0-10")
        print("Сейчас гормкость на уровне ", self.volume)
        if self.volume <= 0:
            print("Это минимальная громкость.")
        else:
            down = None
            while down != int:
                try:
                    down = int(input("\nНа сколько убавить громкость? "))
                    break
                except ValueError:
                    print("Вы вводите не число!")
            step_down = self.volume - down
            if step_down < 0:
                print("Минимальная громкость 0, нельзя уменьшить на ", down)
            else:
                self.volume = step_down

    def show_all(self):
        new_channel = self.channel
        new_volume = self.volume
        print("\nВключен ", new_channel, " канал, Громкость ", new_volume)


def main():
    tv = Tv(0, 0)
    print(tv)
    choice = None
    while choice != "0":
        print \
            ("""
        Управление телевизором
    
        0 - Выключить
        1 - Регулирование каналов
        2 - Увеличить громкость
        3 - Уменьшить громкость
        4 - Проверка состояния
        
        """)

        choice = input("Выберите пункт: ")
        print()

        # выход
        if choice == "0":
            print("Вы выключили телевизор.")

        # переключение каналов
        elif choice == "1":
            tv.change_channel()

        # увеличить громкость
        elif choice == "2":
            tv.up_volume()

        # уменьшить громкость
        elif choice == "3":
            tv.down_volume()

        # проверка состояния
        elif choice == "4":
            tv.show_all()

        # неправильный ввод
        else:
            print("\nИзвините, в меню нет пункта ", choice)


main()
input("\n\nНажмите enter, чтобы выйти.")
