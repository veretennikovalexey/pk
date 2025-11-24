class Game:
    def __init__(self, hp, xp, coins, path):
        self.__hp = hp
        self.__xp = xp
        self.__coins = coins
        self.__path = path
        self.__alive = True

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
