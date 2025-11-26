class Hero:
    def info(self):
        print('Герой без имени')


class Warrior(Hero):
    def info(self):
        print('Герой с мечом')


class Paladin(Warrior):
    pass


p = Paladin()
print(*Paladin.__mro__, sep='\n')

