class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.coins = 0
        self.multiplier = 1

    def show_stats(self):
        print(f'Игрок {self.name}: {self.score} очков, {self.coins} монет, множитель x{self.multiplier}')     


class Enhancement:
    def use(self, player):
        pass


class SuperSneakers(Enhancement):
    def use(self, player):
        print('Супер кроссовки активированы! Прыжок выше!')
        player.multiplier += 1
        super().use(player)


class Jetpack(Enhancement): 
    def use(self, player):
        print('Реактивный ранец включён! Взлетаем над поездами!')
        player.score += 10
        super().use(player)


class CoinMagnet(Enhancement): 
    def use(self, player):
        print('Магнит монет активирован! Притягиваем монеты!')
        player.coins += 20
        super().use(player)        


class Multiplier2x(Enhancement): 
    def use(self, player):
        print('Удвоитель очков! Множитель увеличен в 2 раза!')
        player.multiplier *= 2
        super().use(player)        


class MegaBoost(SuperSneakers, Jetpack, CoinMagnet, Multiplier2x):
    def activate(self, player):
        print('Игрок собирает Мега-улучшение!')    
        super().use(player)
        player.show_stats()