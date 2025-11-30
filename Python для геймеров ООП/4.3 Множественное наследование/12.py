class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.coins = 0
        self.multiplier = 1

    def show_stats(self):
        print(f'Игрок {self.name}: {self.score} очков, {self.coins} монет, множитель x{self.multiplier}')     