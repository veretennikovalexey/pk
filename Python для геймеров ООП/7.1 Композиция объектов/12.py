class Location:
    def __init__(self, name):
        print(f'Загрузка локации "{self.name}"')

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
        self.name = name
        print(f'Появился монстр: {self.name}')


