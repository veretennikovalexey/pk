class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def show(self):
        print(self.name, self.hp)

class Plant(Unit):
    def heal(self):
        self.hp += 5

class Zombie(Unit):
    def attack(self, target):
        target.hp -= 10

pea = Plant("Gorohostrel", 40)
zombie = Zombie("An ordinary zombie", 50)

zombie.attack(pea)
pea.heal()

pea.show()
zombie.show()