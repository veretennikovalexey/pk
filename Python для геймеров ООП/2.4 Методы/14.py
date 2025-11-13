class Zombie:
    def __init__(self, name, hp):
          self.name = name
          self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp          