# Пример 1. Герой и питомец

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        if self.species == "дракон":
            print(f"{self.name} рычит и выпускает пламя! 🔥")
        elif self.species == "волк":
            print(f"{self.name} воет на луну! 🌕")
        else:
            print(f"{self.name} издаёт странные звуки... 😅")


class Hero:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

    def show_pet(self):
        if self.pet:
            print(f"У героя {self.name} есть питомец: {self.pet.species} по имени {self.pet.name}")
        else:
            print(f"У героя {self.name} пока нет питомца")

dragon = Pet("Алдуин", "дракон")
hero = Hero("Довакин", pet=dragon)

hero.show_pet()
del hero
dragon.sound()            

# Пример 2. Герой и союзники

class Character:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"{self.name}: Я готов к приключениям!")


class Hero:
    def __init__(self, name, allies=None):
        self.name = name
        self.allies = allies if allies else []

    def call_allies(self):
        print(f"{self.name} зовёт союзников в бой!")
        for ally in self.allies:
            ally.greet()

legolas = Character("Леголас")
gimli = Character("Гимли")
aragorn = Hero("Арагорн", allies=[legolas, gimli])

aragorn.call_allies()            