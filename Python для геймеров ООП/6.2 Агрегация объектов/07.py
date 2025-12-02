class Ammo:
    def __init__(self, count):
        self.count = count

    def use(self):
        self.count -= 1
        self.count = max(self.count, 0)
        if self.count == 0:
            print('Патроны закончились!')
        else:
            print(f'Остаток патронов: {self.count}') 