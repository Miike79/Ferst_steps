# Карты
# Демонстрирует сочетание объектов

# глава 9 учебника Доусона

class Card(object):
    """Одна игральная карта"""
    RANKS=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS=['c','d','h','s']
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    # как выглядит строка карты на экране
    def __str__(self):
        rep=self.rank+self.suit
        return rep
class Hand(object):
    """Рука - набор карт на руках одного игрока."""
    def __init__(self):
        self.cards=[]
    def __str__(self):
        # если есть хоть одна карта в руке
        if self.cards:
            # вот тут не понял
            rep=""
            for card in self.cards:
                rep+=str(card)+" "
        # если в руке нет карт
        else: 
            rep="<пусто>"
        return rep
    # метод для объекта класса Hand - очистить
    def clear(self):
        self.cards=[]
    # метод для объекта класса Hand - добавить карту
    def add(self,card):
        self.cards.append(card)
    # метод для объекта класса Hand - передать карту в др руку   
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# основная часть:
# создание (инициализация) объектов-карт
card1=Card(rank='A',suit='c')
print("Вывожу на экран объект-карту:")
print(card1)
card2=Card(rank='2',suit='c')
card3=Card(rank='3',suit='c')
card4=Card(rank='4',suit='c')
card5=Card(rank='5',suit='c')
print("\nВывожу на экран ещё четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)

# создание Руки

my_hand=Hand()
print("\nПечатаю карты, которые у меня на руках раздачи:")
print(my_hand)
# атрибут cards равен пустому списку, поэтому будет значение <пусто>
# добавим в объект my_hand 5 объектов класса card
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю 5 карт, которые появились у меня на руках:")
print(my_hand)

# создаем ещё один объект your_hand, и применить метод передачи из рук в руки
your_hand=Hand()
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print("\nПервые две из моих карт я передал вам.")
print("Теперь у вас на руках: ")
print(your_hand)
print("А у меня на руках:")
print(my_hand)

# вывожу метод clear к объекту my_hand
my_hand.clear()
print("У меня на руках после того, как я сбросил все карты:")
print(my_hand)

input("\nНажмите Enter, чтобы выйти")
