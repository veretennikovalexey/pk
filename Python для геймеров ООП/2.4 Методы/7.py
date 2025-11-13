class Monster:
    def __init__(self, name, hp, dmg):
        self.name, self.hp, self.dmg = name, hp, dmg

    def show_info(self):
        print(f'{self.name}\n❤️: {self.hp}\n⚔️: {self.dmg}')            