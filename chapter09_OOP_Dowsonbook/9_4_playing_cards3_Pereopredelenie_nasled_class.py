# Карты 3.0
# Демонстрирует наследование в части переопределения методов.

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
class Unprintable_Card(Card):
    """Карта, номинал и масть которой не могут быть выведены на экран."""
    def __str__(self):
        return "<нельзя напечатать>"
class Positionable_Card(Card):
    """Карта, которую можно положить лицом или рубашкой вверх."""
    def __init__(self,rank,suit,face_up=True):
        # функция super вызывает метод базового класса - надкласса
        # добавляется новый атрибут face_up
        super(Positionable_Card,self).__init__(rank,suit)
        self.is_face_up=face_up
    def __str__(self):
        # этот метод сначала проверяет на истинность атрибут is_face_up
        # если True, значит карта лицом вверх, тогда возвращается
        # строковый метод __str__
        if self.is_face_up:
            rep=super(Positionable_Card,self).__str__()
        else:
            rep="XX"
        return rep
    def flip(self):
        self.is_face_up=not self.is_face_up
        # метод переворачивает карту, заменяя значение атрибута с True
        # на False и наоборот

# основная часть
# создание трех типов карт
card1=Card("A","c")
card2=Unprintable_Card("A","d")
card3=Positionable_Card("A","h")
print("Печатаю объект Card.")
print(card1)
print("\nПечатаю объект Unprintable_Card.")
print(card2)
print("\nПечатаю объект Positionable_Card.")
print(card3)
print("Переворачиваю объект Positionable_Card")
card3.flip()
print("\nПечатаю объект Positionable_Card.")
print(card3)


input("\nНажмите Enter, чтобы выйти")

