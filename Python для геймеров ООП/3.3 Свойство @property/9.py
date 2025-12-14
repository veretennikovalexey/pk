class Hero:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
# hero = Hero("Зяблик")
# print(hero.name)
# hero.name = "KillByaz"