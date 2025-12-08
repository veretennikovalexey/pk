class Location:
    def __init__(self, name):
        self.name = name
        print(f'Загрузка локации "{self.name}"')


class Dungeon:
    def __init__(self):
        print('Генерация подземелья...')
        _1 = Location('Гнойная бухта')
        _2 = Location('Ужасная лощина (Вымершая деревня)')
        _3 = Location('Обветшалая деревня')
        self.locations = [_1, _2, _3]
        print('Подземелье создано!')
