# Создание объектов по названию класса

# Пример 1. Через if

class Weapon:
    pass

name = input()

if name == "Weapon":
    obj = Weapon()

# Пример 2. Через словарь
 
classes = {
    "Weapon": Weapon
}

obj = classes[name]()

# Пример 3. Через eval

obj = eval(name)()