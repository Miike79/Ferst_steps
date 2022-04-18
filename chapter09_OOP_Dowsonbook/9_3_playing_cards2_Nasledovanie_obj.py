# Карты 2.0
# Демонстрирует расширение класса через наследование

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
                rep+=str(card)+"\t"
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

# создание наследуемого класса на безе Hand
class Deck(Hand):
    """Колода игральных карт."""
    def populate(self):
        self.cards=[]
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Не могу больше сдавать, карты закончились!")
  

# основная часть:
# создание (инициализация) нового объекта класса Deck
deck1=Deck()
print("Создана новая колода.")
print("Вот эта колода: ")
print(deck1)
# колода пуста, вызываем метод populate(), чтобы ее наполнить
deck1.populate()
print("\nВ колоде появились карты.")
print("Вот как она выглядит теперь: ")
print(deck1)
# перемешаем колоду
deck1.shuffle()
print("\nКолода перемешана.")
print("Вот как она выглядит теперь: ")
print(deck1)

# создадим два объекта класса hands
my_hand=Hand()
your_hand=Hand()
hands=[my_hand,your_hand]
# раздадим в каждую руку по 5 карт
deck1.deal(hands,per_hand=5)
print("\nМне и вам на руки роздано по 5 карт.")
print("У меня на руках: ")
print(my_hand)
print("У вас на руках.")
print(your_hand)
print("Осталось в колоде: ")
print(deck1)
# возврат колоды в пустое состояние
deck1.clear()
print("\nКолода очищена.")
print("Вот как она выглядит тепрерь: ",deck1)


input("\nНажмите Enter, чтобы выйти")

