# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы

# глава 3 учебника Доусона

print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегистрированных пользователей!\n")
security=0
username=""
while not username:
    username=input("Логин: ")
password=""
while not password:
    password=input("Пароль: ")
if username=="миша" and password=="егорцев":
   print("О здравствуйте, Господин и Властелин наш!")
   security=5
elif username=="аня" and password=="леонова":
   print("Здорово, Клунька!")
   security=3
elif username=="геля" and password=="данилова":
   print("Нам нужны твои Текила и Ириска!")
   security=3
elif username=="хуй" and password=="хуй":
   print("Опять Леонова пишет своё любимое слово!")
   security=3
elif username=="лера" and password=="никитина":
   print("Вход только после продажи хотя бы одного тура!")
   security=3
elif username=="гость" or password=="гость":
   print("Добро пожаловать к нам в гости!")
   security=1
else:
    print("Пшел нах, лох! Тебе тут не рады!\n")
input("\n\nНажмите Enter, чтобы выйти.")
