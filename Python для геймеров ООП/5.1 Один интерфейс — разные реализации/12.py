class Faction:
    def battle_cry(self):
        print('Народ готов к битве!')


class Orc(Faction):
    def battle_cry(self):
        print('За Орду!')


class Elf(Faction):
    def battle_cry(self):
        print('За Альянс!')


class Undead(Faction): 
    def battle_cry(self):
        print('Слава Королю-личу!')
