class Location:    
    def __init__(self, name):      
        print(f'Загрузка локации "{name}"')

        self.name = name
        self.monsters = []

        if name == 'Гнойная бухта':
            self.monsters.append( Monster('Миконид') )
        if name == 'Ужасная лощина (Вымершая деревня)':
            self.monsters.append( Monster('Гоблин') )
            self.monsters.append( Monster('Паук') )
        if name == 'Обветшалая деревня':
            self.monsters.append( Monster('Гоблин') )
            self.monsters.append( Monster('Миконид') )           


class Dungeon:
    def __init__(self):
        print('Генерация подземелья...')

        _1 = Location('Гнойная бухта')
        _2 = Location('Ужасная лощина (Вымершая деревня)')
        _3 = Location('Обветшалая деревня')
        self.locations = [_1, _2, _3]
        
        print('Подземелье создано!')


class Monster:
    def __init__(self, name):
        print(f'Появился монстр: {name}')

        self.name = name

        if name == 'Миконид':
            self.loot = Loot('Куски плоти миконида')
        if name == 'Паук':
            self.loot = Loot('Немного золота')
        if name == 'Гоблин':
            self.loot = Loot('Грязная броня')

        

class Loot:
    def __init__(self, name):
        print(f'Лут: {name}')

        self.name = name




