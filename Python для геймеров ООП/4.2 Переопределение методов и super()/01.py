# Переопределение методов и super()

# override переопределить метод

# super() дополнить метод

class Character:
    def speak(self):
        print("Я обычный герой.")

class Elf(Character):
    def speak(self):
        print("Я эльф!")

hero = Elf()
hero.speak()

# Пример 2. Как вернуть поведение родителя? 

class Character:
    def speak(self):
        print("Я обычный герой.")

class Elf(Character):
    def speak(self):
        super().speak()
        print("Я эльф!")

hero = Elf()
hero.speak()

# MRO (Method Resolution Order)
# цепочка наследования

print(Elf.__mro__)

# Пример 3. Вызов метода определённого класса

class Flyable:
    def move(self):
        print("Летит 🕊️")

class Swimmable:
    def move(self):
        print("Плывёт 🐟")

class Duck:
    def __init__(self, on_water=False):
        self.on_water = on_water

    def move(self):
        if self.on_water:
            Swimmable.move(self)
        else:
            Flyable.move(self)

duck1 = Duck(on_water=True)
duck1.move()

duck2 = Duck(on_water=False)
duck2.move()

# Пример 4. Переопределение конструктора

class Character:
    def __init__(self):
        self.health = 100

class Vampire(Character):
    def __init__(self):
        self.health = 120
        print("Создан вампир с особыми параметрами!")

v = Vampire()
print(v.health)

class Character:
    def __init__(self):
        self.health = 100

class Vampire(Character):
    def __init__(self):
        super().__init__()
        self.health += 5
        print("Создан вампир с особыми параметрами!")

v = Vampire()
print(v.health)