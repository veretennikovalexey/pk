class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"{self.name}: здоровье {self.health} ❤️")


steve = Hero("Стив", 100)
alex = Hero("Алекс", 80)

steve.show_info()
alex.show_info()        

# Атрибуты класса (общие для всех)

class Hero:
    world = "Overworld"

    def __init__(self, name, health):
        self.name = name
        self.health = health

steve = Hero("Стив", 100)
alex = Hero("Алекс", 80)

print(steve.world)
print(alex.world)
print(Hero.world)        

Hero.world = "Nether"

print(steve.world)
print(alex.world)
print(Hero.world)

Hero.world = "Overworld"

steve.world = "End"

print(steve.world)
print(alex.world)
print(Hero.world)

# Проверим структуру с помощью __dict__

class Hero:
    world = "Minecraft"

    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    
Hero.world = "Overworld"
steve = Hero("Стив", 100)
steve.world = "End"

print(steve.__dict__)
print(Hero.__dict__)

# Изменяемые атрибуты класса

class Hero:
    items = []

    def __init__(self, name):
        self.name = name

    def add_item(self, item):
        self.items.append(item)

steve = Hero("Стив")
alex = Hero("Алекс")

steve.add_item("Меч")
alex.add_item("Щит")

print(steve.items)
print(alex.items)
print(Hero.items)        

# 
class Hero:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)