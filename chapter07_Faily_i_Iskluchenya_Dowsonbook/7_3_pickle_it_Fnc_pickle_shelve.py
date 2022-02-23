# Законсервируем
# Демострирует консервацию данных и доступ к ним через
# интерфейс полки pickle.shelve

# глава 7 учебника Доусона
import pickle
import shelve

print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюэль"]
# Теперь открою на запись новый файл бинарных данных:
f = open("pickles1.dat", "wb")  # если файла нет, он будет создан
# команда dump консервирует (данные для сохр, файл для сохр) 
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print("Расконсервация списков.")
f = open("pickles1.dat", "rb")  # открыт только для чтения
variety = pickle.load(f)  # load звлечение/загрузка
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()
print("\nПомещение списков  на  полку.")
# создаем полку s
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]
s.sync()  # убедимся.  что данные записаны
print("\nИзвлечение списков  из файла  полки:")
print("торговые марки: ", s["brand"])
print("фopмы: ", s["shape"])
print("виды овощей: ", s["variety"])
# Наконец.  закроем файл:
s.close()

input("\nНажмите Enter, чтобы выйти.")
