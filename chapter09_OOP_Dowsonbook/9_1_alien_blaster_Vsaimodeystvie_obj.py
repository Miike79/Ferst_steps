# ибель пришельца
# Демонстрирует взаимодействике объектов

# глава 9 учебника Доусона

class Player(object):
    """Игрок в экш-игре"""
    def blast(self,enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """Враждебный пришелец в экшн-игре."""
    def die(self):
        print("Тяжело дыша, пришелец произосит: Я УМИРАЮ!")

# Основная часть программы
print("\t\tГибель пришельца\n")
hero=Player()
invader=Alien()
hero.blast(invader)

input("\nНажмите Enter, чтобы выйти")
