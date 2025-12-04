# Пример 1. Обычный метод (instance method)

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"{self.name}: здоровье {self.health} ❤️")


steve = Hero("Стив", 100)
steve.show_info()

'''Обычный метод — это метод, который работает с конкретным героем.'''

# Пример 2. Метод класса @classmethod

class Hero:
    world = "Minecraft"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_world(cls, new_world):
        cls.world = new_world
        print(f"Мир изменён на {cls.world}")