class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    @property    
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if 0 <= value <= 1000:
            self.__health = value
        else:
            print('Ошибка: здоровье должно быть от 0 до 1000!')

hero = Character("Сон Джин-ву", 146)
hero.health = 93300
print(hero.health)            