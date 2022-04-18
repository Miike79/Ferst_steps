# Игры
# Демонстрирует создание модуля.

# глава 9 учебника Доусона

class Player(object):
    """Участник игры."""
    def __init__(self,name,score=0,wallet=0):
        self.name=name
        self.score=score
        self.wallet=wallet
    def __str__(self):
        rep=self.name+"\t"+str(self.score)+"\t"+str(self.wallet)
        return rep
        
class Amount(object):
    
    """Банковский счёт"""
    def __init__(self):
        self.balance=0
        self.temp=0
    def __str__(self):
        rep="на счёте : "+str(self.balance)+"."
        return rep
    
    # пополнение счета
    def deposite(self):
        deposite=0
        while deposite<=0:
            try:
                deposite=int(input("\nКакую сумму хотите внести? "))
                while deposite<0:
                    print("Не корректная сумма.")
                    deposite=int(input("\nКакую сумму хотите внести? "))
                else:
                    self.balance+=deposite
                    return deposite
            except ValueError:
                print("Это не число.")
            
    # снятие со счета
    def withdraw(self):
        withdraw=0
        while not withdraw >0:
            try:
                withdraw=int(input("\nКакую сумму хотите снять? "))
                while withdraw<0:
                    print("Некорректная сумма.")
                    withdraw=int(input("\nКакую сумму хотите снять? "))
                else:
                    while withdraw > self.balance:
                        print("Недостаточно средств.")
                        print("На вашем счёте только ",self.balance)
                        withdraw=int(input("\nКакую сумму хотите снять? "))
                    else:
                        self.balance-=withdraw
                        return withdraw
            except ValueError:
                print("Это не число.")

    # показать баланс
    def show_balance(self):
        balance=self.balance
        print("на вашем счёте: ",balance)

    # показать временный баланс
    def show_temp(self):
        temp=self.temp
        print("на временном балансе: ",temp)

    # перевод с временного на основной баланс
    def temp_in_balance(self):
        self.balance+=self.temp

    # обнулить баланс
    def clear_balance(self):
        self.balance=0
        
    # обнулить временный баланс
    def clear_temp(self):
        self.temp=0

    # выравнивание
    def make_one_level(self,other_bank):
        difference=other_bank.temp
        self.balance-=difference
        self.temp+=difference
        other_bank.temp+=difference
        
    # выплата выигрыша со счета
    def return_from_bank(self,other_bank):
        prise=self.temp
        other_bank.balance-=prise
        self.balance+=prise

    # выплата выигрыша с временного счёта
    def return_from_temp(self,other_bank):
        prise=self.temp
        other_bank.temp-=prise
        self.balance+=prise

    # перевод проигрыша в банк
    def return_to_winner(self,other_bank):
        prise=self.temp
        other_bank.balance+=prise
        self.temp-=prise

    # возврат остатка
    def remain_balance(self):
        remain=self.temp
        self.balance+=self.temp

    # сделать ставку
    def add_cost(self,other_bank):
        cost=0
        while not cost>0:
            try:
                cost=int(input("\nДелайте вашу ставку : "))
                while cost<=0:
                    print("Некорректная сумма.")
                    cost=int(input("\nДелайте вашу ставку : "))
                else:
                    while cost>self.balance:
                        print("На вашем счёте не достаточно средств.")
                        print("Сейчас ",Amount.__str__(self))
                        cost=int(input("\nДелайте вашу ставку : "))
                    else:
                        print("Ставка ",cost," принята.\n")
                        self.balance-=cost
                        self.temp+=cost
                        other_bank.temp+=cost
                        return cost
            except ValueError:
                print("Это не число.\n")
        
def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'"""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response
    
def ask_number(question,low,high):
    """Просит ввести число из заданного диапазона."""
    response=None
    while response not in range(low,high):
        try:
            response=int(input(question))
        except ValueError:
            print("Это не число.\n")
    else:
        return response

def ask_money(question):
    """Просит сделать ставку"""
    response=None
    while not response or response<=0:
        try:
            response=int(input(question))
            if response<=0:
                print("Ставка не может быть меньше 0.")
                response=int(input(question))
        except ValueError:
            print("Это не число.")
    return response    
    
# условие истинно только тогда, когда программа запускается напрямую
if __name__=="__main__":
    print("Вы запустили этот модуль напрямую, а не импортировали его.")
    input("\nНажмите Enter, чтобы выйти")

