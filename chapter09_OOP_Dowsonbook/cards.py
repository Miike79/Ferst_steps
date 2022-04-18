# Модуль cards
# Набор базовых классов для карточной игры

# глава 9 учебника Доусона

class Card(object):
    """Одна игральная карта"""
    RANKS=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS=[' ♣',' ♦',' ♥',' ♠']
    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up
    def __str__(self):
        # если карта открыта, то отображается номинал/масть
        if self.is_face_up:
            rep=self.rank+self.suit
        else:
            rep="XX"
        return rep
    def flip(self):
        # методи зменения значения на противоположное
        self.is_face_up=not self.is_face_up
        
class Hand(object):
    """Рука - набор карт на руках одного игрока."""
    def __init__(self):
        # иниц. как список объектов карт
        self.cards=[]
    def __str__(self):
        # если есть хоть одна карта в руке
        if self.cards:
            # отображение карт (номинал/масть)+пробел
            rep=""
            for card in self.cards:
                rep+=str(card)+"\t"
        # если в руке нет карт
        else: 
            rep="<пусто>"
        return rep
    # СБРОСИТЬ КАРТЫ - метод для объекта класса Hand
    def clear(self):
        self.cards=[]
    # ДОБАВИТЬ КАРТУ - метод для объекта класса Hand
    def add(self,card):
        self.cards.append(card)
    # ПЕРЕДАТЬ КАРТУ ДРУГОМУ - метод для объекта класса Hand   
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# создание наследуемого класса на безе Hand
class Deck(Hand):
    """Колода игральных карт."""
    # СФОРМИРОВАТЬ - формируется колода всех комбинаций карт
    def populate(self):
        self.cards=[]
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    # ПЕРЕМЕШАТЬ - перетасовать колоду
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    # РАЗДАТЬ - указываются играющие "руки" и сколько карт на руки
    def deal(self,hands,per_hand=1):
        # для каждой операции в количестве операций
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Не могу больше сдавать, карты закончились!")

if __name__=="__main__":
    print("Это модуль, содержащий классы для карточных игр.")
    input("\nНажмите Enter, чтобы выйти")

