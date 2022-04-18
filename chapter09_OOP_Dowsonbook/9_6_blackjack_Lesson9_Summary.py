# BlackJack
# От 1 до 7 игроков против дилера.

# глава 9 учебника Доусона

# импортируем модули, который сами создали
import cards,games

class BJ_Card(cards.Card):
    """Карта для игры в блекджек."""
    ACE_VALUE=1
    @property
    # метод номинал карты
    def value(self):
        if self.is_face_up:
# метод для карты начинает вычислять в списке RANKS индекс карты+1
# +1 т.к. первый индекс=0, а номинала "0" в игре нет
            v=BJ_Card.RANKS.index(self.rank)+1
# все, что выше 10 (J,Q,K) приравнивается к 10
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """Колода для игры."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank,suit))

class BJ_Hand(cards.Hand):
    """Рука - набор карт у одного игрока"""
    def __init__(self,name):
        # переопределил конструктор cards, добавив атрибут name
        super(BJ_Hand,self).__init__()
        self.name=name
# переопределен метод __str__, чтобы отображались очки
    def __str__(self):
        rep=self.name+":\t"+super(BJ_Hand,self).__str__()
        if self.total:
            rep+="("+str(self.total)+")"
        return rep
    @property
    # свойство total представляет сумму очков игрока
    def total(self):
        #если у одной карты value=None, то все свойство None
        for card in self.cards:
            if not card.value:
                return None
            # суммируем очки, считая каждый туз за 1 очко
            t=0
            for card in self.cards:
                t += card.value
            # определяем есть ли туз на руках
            contains_ace=False
            for card in self.cards:
                if card.value==BJ_Card.ACE_VALUE:
                    contains_ace=True
    #если на руках есть туз и сумма очков<11, туз как 11
            if contains_ace and t<=11:
                # прибавить только 10, т.к. 1 уже вошла в сумму
                t+=10
            return t
    # метод, если перебор карт
    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Игрок"""
    def is_hitting(self):
        response=games.ask_yes_no("\n"+self.name+", будете брать ещё карты? (Y/N): ")
        return response == "y"
    def bust(self):
        print(self.name," перебрал.")
        self.lose()
    def lose(self):
        print(self.name," проиграл.")
    def win(self):
        print(self.name," выиграл.")
    def push(self):
        print(self.name," сыграл с компьютером вничью.")

class BJ_Dealer(BJ_Hand):
    """Дилер"""
    def is_hitting(self):
        return self.total<17
    def bust(self):
        print(self.name," перебрал.")
    def flip_first_card(self):
        first_card=self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Игра в блекджек"""
    def __init__(self,names):
        self.players=[]
        for name in names:
            player=BJ_Player(name)
            self.players.append(player)
        self.dealer=BJ_Dealer("Дилер")
        self.deck=BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    # свойство возвращает список игроков, кто в игре
    def still_playing(self):
        sp=[]
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    # етод сдает игроку дополнительные карты
    def __additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    # метод содержит основной цикл игры
    def play(self):
        # сдача всем по 2 карты
        self.deck.deal(self.players+[self.dealer],per_hand=2)
        self.dealer.flip_first_card()
        # первая карта дилера переворачивается рубашкой вверх
        for player in self.players:
            print(player)
        print(self.dealer)
        # сдача дополнительных карт игрокам
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card() # первая карта дилера раскрывается
        if not self.still_playing:
            # все игроки перебрали, покажем только "руку" дилера
            print(self.dealer)
        else:
            # сдача доп карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                # выигрывают все, кто остался в игре
                for player in self.still_playing:
                    player.win()
            else:
            # сравниваем очки у дилера и оставшихся игроков
                for player in self.still_playing:
                    if player.total>self.dealer.total:
                        player.win()
                    elif player.total<self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tДобро пожаловать за игровой стол Блек-Джека!\n")
    names=[]
    number=games.ask_number("Сколько всего игроков? (1-7): ",low=1,high=8)
    for i in range(number):
        name=input("Введите имя игрока: ")
        names.append(name)
        print()
    game=BJ_Game(names)
    again=None
    while again!="n":
        game.play()
        again=games.ask_yes_no("\nХотите сыграть ещё раз? ")
    input("\nНажмите Enter, чтобы выйти.")
    
main()


