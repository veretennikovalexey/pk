class Ammo:
    '''Пиф-паф! Ой-ой-ой! Часть 1'''
    def __init__(self, count):
        self.count = count

    def use(self):
        self.count -= 1
        self.count = max(self.count, 0)
        if self.count == 0:
            print('Патроны закончились!')
        else:
            print(f'Остаток патронов: {self.count}') 


class Weapon:
    '''Пиф-паф! Ой-ой-ой! Часть 2'''
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def shoot(self):
        if self.ammo and self.ammo.count > 0:
            print(f'{self.name} делает выстрел!')
            self.ammo.use()
        else:
            print('Нет патронов!')