# Атрибуты экземпляра (у каждого героя свои)

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


