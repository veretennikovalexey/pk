class Spaceship:
    ''' класс Spaceship '''
    def __init__(self, name, health, energy):
        self.__name = name
        self.__health = health
        self.__energy = energy

    def __take_damage(self, amount):
        self.__health -= amount
        if self.__health <= 0:
            print(f'{self.__name} уничтожен!')
        else:
            print(f'{self.__name} получил урон, осталось прочности: {self.__health}')


    def __use_energy(self, cost):
        if self.__energy >= cost:
            self.__energy -= cost
            return True
        else:
            return False

    def fire(self, target, laser):
        if self.__use_energy(laser.energy_cost):
            print(f'{self.__name} стреляет лазером!')
            laser.shoot(target)
        else:
            print(f'{self.__name}: Недостаточно энергии для выстрела!')    

    
class Laser:
    ''' класс Laser '''
    def __init__(self, damage, energy_cost):
        self.__damage = damage
        self.energy_cost = energy_cost

    def __impact(self, target):
        target._Spaceship__take_damage(self.__damage)

    def shoot(self, target):
        self.__impact(target)