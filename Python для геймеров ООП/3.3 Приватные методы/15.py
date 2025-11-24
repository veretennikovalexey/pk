class Spaceship:
    ''' класс Spaceship '''
    def __init__(self, name, health, energy):
        self.__name = name
        self.__health = health
        self.__energy = energy

    def __take_damage(self, amount):
        pass

    def __use_energy(self, cost):
        pass

    def fire(self, target, laser):
        pass
    
class Laser:
    ''' класс Laser '''
    def __init__(self, damage, energy_cost):
        self.__damage = damage
        self.energy_cost = energy_cost

    def __impact(self, target):
        pass

    def shoot(self, target):
        pass