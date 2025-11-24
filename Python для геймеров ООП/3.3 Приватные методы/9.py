class Button:
    def __init__(self):
        self.__clickCounter = 0

    def __animate(self):
        print('Анимация клика...')

    def click(self):
        self.__animate()
        self.__clickCounter += 1
        if self.__clickCounter % 2 == 0:
            print('Инвентарь закрыт')
        else:
            print('Инвентарь открыт')