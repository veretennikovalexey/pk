class Enemy:
    ''' Общий счётчик объектов '''
    created = 0

    def __init__(self):
        Enemy.created += 1