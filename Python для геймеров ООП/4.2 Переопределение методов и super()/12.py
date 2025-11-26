class Weapon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f'{self.name} наносит урон!')

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        print(f'{self.name} наносит {self.damage} урона!')

s = Sword("Night’s Edge", 25)
s.attack()