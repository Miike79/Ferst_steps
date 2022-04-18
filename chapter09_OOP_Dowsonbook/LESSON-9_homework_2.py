# игра "Война"
# Игрок вытягивает одну карту, побеждает тот, у кого больше номинал.

# глава 9 учебника Доусона

from itertools import chain
import cards
import games


class Playcard(cards.Card):
    """Карта для игры в войну."""

    @property
    # метод номинал карты
    def value(self):
        if self.is_face_up:
            # метод для карты начинает вычислять в списке RANKS индекс карты+1
            # +1 т.к. первый индекс=0, а номинала "0" в игре нет
            v = Playcard.RANKS.index(self.rank) + 1
            # все, что выше 10 (J,Q,K) увеличивается значение
            if v == 'J':
                v = 11
            elif v == 'Q':
                v = 12
            elif v == 'K':
                v = 13
                # не работает
            elif v == 'A':
                v = 14
        else:
            v = None
        return v


class Playdeck(cards.Deck):
    """Колода для игры."""

    def populate(self):
        for suit in Playcard.SUITS:
            for rank in Playcard.RANKS:
                self.cards.append(Playcard(rank, suit))


class Playhand(cards.Hand):
    """Рука - набор карт у одного игрока"""

    def __init__(self, name):
        # переопределил конструктор cards, добавив атрибут name
        super(Playhand, self).__init__()
        self.name = name

    # переопределен метод __str__, чтобы отображались очки
    def __str__(self):
        rep = self.name + ":\t" + super(Playhand, self).__str__()
        # если есть сумма очков, то она добавляется в конце в ()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    # свойство total представляет сумму очков игрока
    def total(self):
        # если у одной карты value=None, то все свойство None
        for card in self.cards:
            if not card.value:
                return None
            # суммируем очки
            t = 0
            t += card.value
            return t


class Warplayer(Playhand):
    """Игрок"""

    def __init__(self, name):
        # переопределил конструктор cards, добавив атрибут name
        super(Playhand, self).__init__()
        self.name = name

    def __str__(self):
        rep = "Игрок " + str(self.name) + ":\t" + super(Playhand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + " очков)"
        return rep

    # ПРОИГРЫШ
    def lose(self):
        print("Игрок ", self.name, " проиграл.")

    # ВЫИГРЫШ
    def win(self):
        print("Игрок ", self.name, " выиграл.")

    # НИЧЬЯ
    def push(self):
        print("Игрок ", self.name, " сыграл вничью.")


class Wargame(object):
    """Игра в Войну"""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = Warplayer(name)
            self.players.append(player)
        self.deck = Playdeck()
        self.deck.populate()
        self.deck.shuffle()

    # ИГРА
    def play(self):
        # сдача всем по карте
        self.deck.deal(self.players, per_hand=1)
        Scores = {}
        for player in self.players:
            print(player)
            igrok = player.name
            score = player.total
            Scores[igrok] = score

        rev_dict = {}

        for key, value in Scores.items():
            rev_dict.setdefault(value, set()).add(key)

        result = set(chain.from_iterable(

            values for key, values in rev_dict.items()

            if len(values) > 1))

        print()
        if result:
            for player in self.players:
                if player.name in result:
                    player.push()

                else:
                    player.lose()
        else:
            leader = max(Scores, key=Scores.get)
            for player in self.players:
                if player.name == leader:
                    player.win()
                else:
                    player.lose()

        # удаление всех карт
        for player in self.players:
            player.clear()


def main():
    print("\t\tДобро пожаловать в игру \"Война!\"""\n")
    print("Игра очень простая, тяни карту, у кого номинал больше, тот и выиграл.")
    names = []
    number = games.ask_number("Сколько будет всего игроков? (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        print()
    game = Wargame(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть ещё раз? ")
    input("\nНажмите Enter, чтобы выйти.")


main()
