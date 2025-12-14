class Game:
    def __init__(self, hp, xp, coins, path):
        self.__hp = hp
        self.__xp = xp
        self.__coins = coins
        self.__path = path
        self.__alive = True

    def run(self):
        for event in self.__path:
            match event:
                case '0':
                    pass
                case '1':
                    self.__add_coins()
                case '2':
                    self.__trap()
                case '3':
                    self.__monster()
                case '4':
                    self.__heal()
            if self.__alive:
                print(f'HP: {self.__hp} | XP: {self.__xp} | Coins: {self.__coins}')
            else:    
                return

    def __add_coins(self):
        self.__coins += 100

    def __trap(self):
        self.__hp -= 10
        self.__check_alive()

    def __monster(self):
        self.__hp -= 15
        self.__check_alive()
        if self.__alive:
            self.__xp += 100

    def __heal(self):
        self.__hp += 10

    def __check_alive(self):
        if self.__hp <= 0 and self.__alive: 
            print('Press F!')
            self.__alive = False

hp, xp, coins = map(int, input().split())
path = input()
game = Game(hp, xp, coins, path)
game.run()