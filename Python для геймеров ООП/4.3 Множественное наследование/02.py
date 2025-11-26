class Warrior:
    pass

class Archer:
    pass

class Ranger(Warrior, Archer):
    pass

for mro in Ranger.mro():
    print(mro) 