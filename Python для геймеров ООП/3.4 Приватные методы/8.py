class Mage:
    def __init__(self, mana):
        self.__mana = mana

    def cast_spell(self, required):
        if self.__check_energy(required):
            self.__mana -= required
            print('Зольтраак!')
        else:
            print('Недостаточно маны!')    

    def __check_energy(self, required):
        return self.__mana >= required # True Зольтраак!


