# setattr(object, name, value)

setattr(person, "id_2", "Vasya")  # "id_2" - правильно, потому что строка
setattr(car, "number", 123)       # "number" - правильно, потому что строка

id_1 = "attr"
setattr(person, id_1, "Vasya")    # id_1 - правильно, потому что переменная,а её значение строка

# 1) setattr(id_1, "name", "Vasya")  
# 2) id_1.name = "Vasya"

file = {'name': 'Alex', 'age': 18, 'hobby': 'films'}

class Person:
    pass

id_1 = Person()

for key, value in file.items():
    setattr(id_1, key, value)      # используем цикл по file и создаём атрибуты в id_1
    # id_1.key = value             # через точку так не получится

print(id_1.hobby)  # films