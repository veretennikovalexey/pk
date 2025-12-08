class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Character:
    def __init__(self, name, pet):
        print(f'{name} завёл питомца: {pet.name} ({pet.species})')

        self.name = name
        self.pet = pet
        

pet = Pet('Кусь за бочок', 'волк')
hero = Character('Ваня', pet)